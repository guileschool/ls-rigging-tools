'''
Created on Aug 23, 2014

@author: Leon
'''

import pymel.core as pm
from pymel.core.language import Mel
mel = Mel()

def getClickedFace():
    '''
    use a scriptJob to call this when the mouse is
    clicked int he viewport
    '''
    

def setFaceToFaceGrpMap(ctlFaceGrpMap):
    '''
    '''
    # convert control-face map to face-faceGrp map
    faceGrpMap = {}
    for ctl, faceGrp in ctlFaceGrpMap.items():
        for faceId in faceGrp:
            faceGrpMap[faceId] = faceGrp, ctl
            
    return faceGrpMap

def setup():
    '''
    define relationship bt controls and faces
    '''
    # define faces for each control
    fkFacesMap = {}
    
    fkFacesMap['Mathilda_lf_upArm_fk_ctrl'] = [comp.index() for comp in pm.ls(sl=True)]
    fkFacesMap['Mathilda_lf_elbow_fk_ctrl'] = [comp.index() for comp in pm.ls(sl=True)]
    fkFacesMap['Mathilda_lf_wrist_fk_ctrl'] = [comp.index() for comp in pm.ls(sl=True)]
    
    # result
    fkFacesMap = {'Mathilda_lf_elbow_fk_ctrl': [4206,
                               4207,
                               4208,
                               4209,
                               4210,
                               4211,
                               4215,
                               4216,
                               4217,
                               4218,
                               4219,
                               4220,
                               4221,
                               4222,
                               4223,
                               4224,
                               4225,
                               4226,
                               4227,
                               4228,
                               4229,
                               4230,
                               4231,
                               4232,
                               4235,
                               4237,
                               4238,
                               4240,
                               4242,
                               4250,
                               4251,
                               4253,
                               4255,
                               4259,
                               4260,
                               4261,
                               4262,
                               4265,
                               4279,
                               4280,
                               4281,
                               4282,
                               4283,
                               4289,
                               4290,
                               4291,
                               4293,
                               4296,
                               4297,
                               4298,
                               4299,
                               4300,
                               4301,
                               4302,
                               4303,
                               4304,
                               4305,
                               4306,
                               4307,
                               4308,
                               4310,
                               4311,
                               4312,
                               4313,
                               4314,
                               4315,
                               4316,
                               4318,
                               4319,
                               4320,
                               4321,
                               4322,
                               4323,
                               4324,
                               4325,
                               4326,
                               4327,
                               4328,
                               4329,
                               4330,
                               4331,
                               4333,
                               4334,
                               4336,
                               4337,
                               4338,
                               4340,
                               4341,
                               4344,
                               4345,
                               4346,
                               4347,
                               4348,
                               4349,
                               4350,
                               5115,
                               5726,
                               5727,
                               5728,
                               5729,
                               5730,
                               5731,
                               5732,
                               5733,
                               5734,
                               5735],
 'Mathilda_lf_upArm_fk_ctrl': [260,
                               362,
                               363,
                               3552,
                               3553,
                               3558,
                               3559,
                               3560,
                               3561,
                               3562,
                               3564,
                               3565,
                               3566,
                               3567,
                               3570,
                               3572,
                               3573,
                               3604,
                               3605,
                               3606,
                               3607,
                               3608,
                               3609,
                               3610,
                               3611,
                               3612,
                               3613,
                               3614,
                               3615,
                               3616,
                               3617,
                               3618,
                               3619,
                               3620,
                               3621,
                               3622,
                               3623,
                               3624,
                               3625,
                               3629,
                               3630,
                               3632,
                               3635,
                               3636,
                               3637,
                               3638,
                               3639,
                               3640,
                               3641,
                               3670,
                               3671,
                               3672,
                               3673,
                               3674,
                               3675,
                               3676,
                               3677,
                               3678,
                               3701,
                               3702,
                               3703,
                               3704,
                               3705,
                               3706,
                               3707,
                               3708,
                               3709,
                               3710,
                               3711,
                               3712,
                               3713,
                               3714,
                               3715,
                               3716,
                               3717,
                               3718,
                               3719,
                               3720,
                               4198,
                               4199,
                               4200,
                               4201,
                               4202,
                               4203,
                               4204,
                               4205,
                               4212,
                               4213,
                               4214,
                               4239,
                               4241,
                               4243,
                               4244,
                               4245,
                               4246,
                               4247,
                               4248,
                               4249,
                               4252,
                               4254,
                               4256,
                               4257,
                               4258,
                               4263,
                               4264,
                               4266,
                               4267,
                               4268,
                               4269,
                               4270,
                               4271,
                               4272,
                               4273,
                               4274,
                               4275,
                               4276,
                               4277,
                               4278,
                               4284,
                               4285,
                               4286,
                               4287,
                               4288,
                               4292,
                               5105,
                               5710,
                               5711,
                               5712,
                               5713,
                               5714,
                               5715,
                               5716,
                               5717,
                               5718,
                               5719,
                               5720,
                               5721,
                               5722,
                               5723,
                               5724,
                               5725,
                               5736,
                               5737,
                               5738,
                               5739,
                               5740,
                               5741,
                               5742,
                               5743,
                               5744,
                               5745],
 'Mathilda_lf_wrist_fk_ctrl': [4233,
                               4234,
                               4236,
                               4309,
                               4317,
                               4332,
                               4335,
                               4339,
                               4342,
                               4343,
                               4471,
                               4472,
                               4473,
                               4474,
                               4475,
                               4476,
                               4477,
                               4478,
                               4479,
                               4480,
                               4481,
                               4999,
                               5000,
                               5001,
                               5002,
                               5003,
                               5004,
                               5005,
                               5006,
                               5007,
                               5008,
                               5011,
                               5013,
                               5015,
                               5016,
                               5017,
                               5018,
                               5019,
                               5020,
                               5021,
                               5022,
                               5023,
                               5024,
                               5025,
                               5026,
                               5027,
                               5028,
                               5029,
                               5030,
                               5031,
                               5032,
                               5033,
                               5034,
                               5035,
                               5036,
                               5037,
                               5038,
                               5039,
                               5040,
                               5041,
                               5042,
                               5043,
                               5044,
                               5045,
                               5046,
                               5047,
                               5048,
                               5057,
                               5058,
                               5059,
                               5060,
                               5061,
                               5062,
                               5063,
                               5064,
                               5065,
                               5066,
                               5067,
                               5068,
                               5069,
                               5070,
                               5071,
                               5072,
                               5073,
                               5074,
                               5075,
                               5077,
                               5078,
                               5079,
                               5080,
                               5081,
                               5082,
                               5083,
                               5084,
                               5085,
                               5086,
                               5087,
                               5089,
                               5090,
                               5091,
                               5093,
                               5095,
                               5096,
                               5101,
                               5102,
                               5103,
                               5104,
                               5138,
                               5139,
                               5140,
                               5141,
                               5142]} # 

    
    fkGrpMap = setFaceToFaceGrpMap(fkFacesMap)

def updateHighlight(faces):
    '''
    faces - list of faces to add to shadingEngine
    if None, just hide the mesh
    
    TODO: implement different types of highlights, for 
    ik, fk, tweaks, etc
    '''
    # mesh = pm.PyNode('CT_mesh_hilight_shd')
    sg = pm.PyNode('lambert3SG')
    
    pm.sets(sg, add=faces)
    pm.refresh()