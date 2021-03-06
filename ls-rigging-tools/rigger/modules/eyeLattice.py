'''
Created on May 26, 2014

@author: Leon
'''
import pymel.core as pm
import pymel.core.nodetypes as nt
import pymel.core.datatypes as dt
import rigger.lib.controls as controls
import rigger.modules.localReader as localReader
reload(localReader)

def buildEyeShaper():
    createLattice([nt.Transform(u'LT_eyeball_geo'),
                    nt.Transform(u'RT_eyeball_geo')], 
                    [nt.Mesh(u'CT_face_geoShape'),
                    nt.Mesh(u'LT_brow_geoShape'),
                    nt.Mesh(u'RT_brow_geoShape')])
    
    # add placement locs
    pGrp = nt.Transform(u'CT_eyeLattice_placement_grp')
    import rigger.modules.placementGrp as placementGrp
    reload(placementGrp)
    placementGrp.mirrorAllPlacements(pGrp)
    
    # create bnds
    import rigger.modules.face as face
    bndGrp = face.createBndsFromPlacement(pGrp)
    # motion sys
    # mesh is passed in for legacy reasons
    face.buildSecondaryControlSystem(pGrp, bndGrp, mesh=None)
    
    priCtlMappings = {'LT_midUp_eyeShaper_pri_ctrl': {u'LT_inUp_eyeShaper_bnd':1,
                                                        u'LT_midUp_eyeShaper_bnd':1,
                                                        u'LT_outUp_eyeShaper_bnd':1},
    'LT_midLow_eyeShaper_pri_ctrl': {u'LT_inLow_eyeShaper_bnd':1,
                                                        u'LT_midLow_eyeShaper_bnd':1,
                                                        u'LT_outLow_eyeShaper_bnd':1},
    'RT_midUp_eyeShaper_pri_ctrl': {u'RT_inUp_eyeShaper_bnd':1,
                                                        u'RT_midUp_eyeShaper_bnd':1,
                                                        u'RT_outUp_eyeShaper_bnd':1},
    'RT_midLow_eyeShaper_pri_ctrl': {u'RT_inLow_eyeShaper_bnd':1,
                                                        u'RT_midLow_eyeShaper_bnd':1,
                                                        u'RT_outLow_eyeShaper_bnd':1}}
    import rigger.modules.priCtl as priCtl
    reload(priCtl)
    priCtl.setupPriCtlSecondPass(priCtlMappings)

def createLattice(eyeGeos, faceGeos):
    '''
    eyeGeos - list of meshes for eye etc (define bounding box for lattice)
    faceGeos - list of meshes for face, eyelashes, etc
    '''
    dfm, lat, base = pm.lattice(eyeGeos, n='CT_eyeLattice_dfm', objectCentered=True,
                                dv=[9,6,2], ldv=[4,2,2], commonParent=True)
               
    dfm.local.set(True)
    
    for faceGeo in faceGeos:
        dfm.addGeometry(faceGeo)
        
    dfmGrp = lat.getParent()
    dfmGrp.centerPivots()
    pm.select(dfmGrp)
    return dfmGrp

def createLatticeControls():
    '''
    assume lattice is already created and xformed
    '''
    lat = nt.Transform(u'CT_eyeLattice_dfmLattice')
    
    # defining lattice points
    lf_in_col = 5
    lf_mid_col = 6
    lf_out_col = 7
    rt_out_col = 1
    rt_mid_col = 2
    rt_in_col = 3
    up_row = 3
    dn_row = 2
    
    deformPoints = {'LT_eyeUpIn': [lat.pt[lf_in_col][up_row][0], lat.pt[lf_in_col][up_row][1]],
    'LT_eyeUpMid': [lat.pt[lf_mid_col][up_row][0], lat.pt[lf_mid_col][up_row][1]],
    'LT_eyeUpOut': [lat.pt[lf_out_col][up_row][0], lat.pt[lf_out_col][up_row][1]],
    'LT_eyeDnIn': [lat.pt[lf_in_col][dn_row][0], lat.pt[lf_in_col][dn_row][1]],
    'LT_eyeDnMid': [lat.pt[lf_mid_col][dn_row][0], lat.pt[lf_mid_col][dn_row][1]],
    'LT_eyeDnOut': [lat.pt[lf_out_col][dn_row][0], lat.pt[lf_out_col][dn_row][1]],
    'RT_eyeUpIn': [lat.pt[rt_in_col][up_row][0], lat.pt[rt_in_col][up_row][1]],
    'RT_eyeUpMid': [lat.pt[rt_mid_col][up_row][0], lat.pt[rt_mid_col][up_row][1]],
    'RT_eyeUpOut': [lat.pt[rt_out_col][up_row][0], lat.pt[rt_out_col][up_row][1]],
    'RT_eyeDnIn': [lat.pt[rt_in_col][dn_row][0], lat.pt[rt_in_col][dn_row][1]],
    'RT_eyeDnMid': [lat.pt[rt_mid_col][dn_row][0], lat.pt[rt_mid_col][dn_row][1]],
    'RT_eyeDnOut': [lat.pt[rt_out_col][dn_row][0], lat.pt[rt_out_col][dn_row][1]]}
    
    
    # create clusters
    clusters = {}
    dfg = pm.group(em=True, n='CT_eyeLatticeClusters_dfg')
    for name, components in deformPoints.items():
        dfm, hdl = pm.cluster(components[1], n=name+'_cluster_dfm', relative=True)
        # above: use relative - the cluster handles will be parented with the face/head control
        # so parentConstraint will only drive offset values to the handles
        # so we'll make sure to only use the local offset values
        dfm.setGeometry(components[0])
        dfg | hdl
        clusters[name] = dfm, hdl
    
    # create controls
    controlZOffset = 0
    childEyeShapers = []
    localReadersGrp = pm.group(em=True, n='CT_eyeLatticeClusters_localReadersGrp')
    for name, (dfm, hdl) in clusters.items():
        pt = hdl.getRotatePivot(space='world')
        pt = dt.Point(pt + (0, 0, controlZOffset))
        ctl = pm.circle(n=name+'_eyeShaper_ctl')
        ctg = pm.group(ctl, n=name+'_eyeShaper_ctg')
        cth = pm.group(ctg, n=name+'_eyeShaper_cth')
        cth.setTranslation(pt)
        # shape ctl
        ctl[1].radius.set(0.5)
        ctl[1].sweep.set(359)
        ctl[1].centerZ.set(0)
        pm.delete(ctl, ch=True)
        # scale transform
        ctl[0].sy.set(0.333)
        pm.makeIdentity(ctl[0], s=True, a=True)
        # color shape
        if 'LT_' in name:
            controls.setColor(ctl[0], 18)
        elif 'RT_' in name:
            controls.setColor(ctl[0], 20)
        else:
            pm.warning('unknown side %s' % name)
        # parent constraint cluster (using matrices)
        reader = localReader.create(hdl, localReadersGrp)
        pm.parentConstraint(ctl[0], reader, mo=True)
        childEyeShapers.append(cth)
        
    # control parents
    parentEyeShapers = []
    for parentCtlName in('RT_eyeUp', 'RT_eyeDn', 'LT_eyeUp', 'LT_eyeDn'):
        # create parent control at cluster location
        clusHdl = clusters[parentCtlName+'Mid'][1]
        pt = clusHdl.getRotatePivot(space='world')
        pt = pt + (0, 0, controlZOffset)
        ctl = pm.circle(n=parentCtlName+'_eyeShaper_ctl')
        ctg = pm.group(ctl, n=parentCtlName+'_eyeShaper_ctg')
        cth = pm.group(ctg, n=parentCtlName+'_eyeShaper_cth')
        cth.setTranslation(pt)
        # shape ctl
        ctl[1].radius.set(2.5)
        ctl[1].sweep.set(359)
        ctl[1].centerZ.set(0)
        pm.delete(ctl, ch=True)
        # scale transform
        ctl[0].sy.set(0.1)
        pm.makeIdentity(ctl[0], s=True, a=True)
        # color shape
        if 'LT_' in parentCtlName:
            controls.setColor(ctl[0], 18)
        elif 'RT_' in parentCtlName:
            controls.setColor(ctl[0], 20)
        else:
            pm.warning('unknown side %s' % name)
        # parent other controls
        children = [n for n in childEyeShapers if parentCtlName in n.name()]
        pm.parent(children, ctl[0])
        parentEyeShapers.append(cth)
        
    # group both controls and clusters under the CTG,
    # so cluster will only use local offsets
    eyeShaperCtg = pm.group(parentEyeShapers, localReadersGrp, n='CT_eyeLatticeControls_ctg')
    return eyeShaperCtg