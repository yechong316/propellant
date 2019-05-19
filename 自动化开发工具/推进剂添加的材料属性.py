# coding:utf-8
'''
给推进剂添加的材料属性
'''
# 力学
from abaqus import *
from abaqusConstants import *

def propellant_property():
    mdb.models['Model-1'].Material(name='propeller')
    mdb.models['Model-1'].materials['propeller'].Viscoelastic(domain=TIME,
        time=PRONY, table=((100.0, 200.0, 0.01), ))
    mdb.models['Model-1'].materials['propeller'].viscoelastic.Trs(table=((20.0,
        -20.09, 403.61), ))
    mdb.models['Model-1'].materials['propeller'].viscoelastic.setValues(
        domain=TIME, time=PRONY, table=((0.2, 0.5, 0.1), (0.1, 0.2, 0.2)))
    mdb.models['Model-1'].materials['propeller'].Elastic(temperatureDependency=ON,
        table=((5143.68, 0.271, 306.0), (4292.0, 0.28, 316.0), (3530.0, 0.271,
        326.0)))
    mdb.models['Model-1'].materials['propeller'].Density(table=((1.65e-06, ), ))
    # 热学
    mdb.models['Model-1'].materials['propeller'].SpecificHeat(
        temperatureDependency=ON, table=((1421.0, 23.0), (1486.0, 33.0), (1532.0,
        43.0), (1598.0, 53.0), (1634.0, 63.0), (1645.0, 73.0)))
    mdb.models['Model-1'].materials['propeller'].Conductivity(table=((0.000173, ),
        ))
    mdb.models['Model-1'].materials['propeller'].Expansion(table=((0.0001263, ),
        ))
    # 将构件作为一个集进行定义,
    pickedCells = mdb.models['Model-1'].parts['propeller'].cells[:]
    p = mdb.models['Model-1'].parts['propeller']
    p.Set(cells=pickedCells, name='Set_' + 'propeller')
    region = p.sets['Set_' + 'propeller']
    # 生成截面
    mdb.models['Model-1'].HomogeneousSolidSection(name='propeller' + '-1',
                                                  material='propeller', thickness=None)
    # 将截面属性赋予给前文定义的集(abaqus不可以直接给某一个构件赋予材料属性
    # 必须先将构件定义为一个set,然后赋予到set上面
    p.SectionAssignment(region=region, sectionName='propeller' + '-1', offset=0.0,
                        offsetType=MIDDLE_SURFACE, offsetField='',
                        thicknessAssignment=FROM_SECTION)
propellant_property()