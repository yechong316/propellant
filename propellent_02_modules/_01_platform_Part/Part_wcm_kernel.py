# coding:utf-8 
from abaqus import *
from abaqusConstants import *
import os

from propellent_03_function.propellent_03_function import *
from ABAQUSFunction import *

def part_var(
    # 3个构件文件路径
    filepath_c=None,filepath_b=None, filepath_f=None, filepath_h=None
    # 1-复合材料的材料参数
    ,desity_c=None, Elastic_c=None, Poisson_c=None, Conductivity_c=None,SpecificHeat_c=None, Expansion_c=None,size_c=None
    # 2-包覆层的材料参数
    ,desity_b=None, Elastic_b=None, Poisson_b=None, Conductivity_b=None, SpecificHeat_b=None, Expansion_b=None,size_b=None
    # 3-封头的材料参数
    ,desity_f=None, Elastic_f=None, Poisson_f=None, Conductivity_f = None,SpecificHeat_f = None, Expansion_f = None, size_f = None
    # 4-推进剂的材料参数                                                                                                                                   
    ,desity_h=None, Elastic_h=None, Poisson_h=None,Conductivity_h = None,SpecificHeat_h = None, Expansion_h = None, size_h = None
    # 开关函数
     ,var_export=False, var_input=False, var_WCM=False, inputfile=None
):
    
    if var_export:
        return exportXXX()

    if var_input:

        read = Read()
        read.plug_1(inputfile)

        part_property = read.mat()
        mesh_size = read.mesh_size()

    else:

        part_property = [
            [desity_c, Elastic_c, Poisson_c, Conductivity_c, SpecificHeat_c, Expansion_c],
            [desity_c, Elastic_c, Poisson_c, Conductivity_c, SpecificHeat_c, Expansion_c],
            [desity_c, Elastic_c, Poisson_c, Conductivity_c, SpecificHeat_c, Expansion_c],
            [desity_c, Elastic_c, Poisson_c, Conductivity_c, SpecificHeat_c, Expansion_c]
        ]

    # 导入构件
    part_name = ('shell', 'bfc', 'fengtou', 'propeller')
    part_path = [filepath_c, filepath_b, filepath_f, filepath_h]

    for name, path in zip(part_name, part_path):
        p = Part(name)
        p.input_part(path)
        p.instance()

    for name, mat in zip(part_name, part_property):
        p = Property(name)
        p.creat_property(mat)
        p.SetSectionAssignment()


