# coding:utf-8
'''
前言:新版本插件特点:代码简洁优雅,可读性强,最重要的扩展性强

本代码的思路:
   ---> 1. 导入必备的方法和包,包含自己写的方法文件
   ---> 2. 定义函数part_var 接收界面的所有参数
   ---> 3. 当用户导入外部文本数据时,则写一个方法,将数据导入内部,不再使用part_var中的参数
   ---> 4. 将界面参数分为两大类,模型路径和材料参数,分别定义两个类进行处理
   

'''

from abaqus import *
from abaqusConstants import *
import os

from propellent_03_function.propellent_03_function import *
from propellent_03_function.ABAQUSFunction import *

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

    if var_input:

        read = Read()
        read.plug_1(inputfile)
        part_property = read.mat()
        mesh_size = read.mesh_size()

    else:

        part_property = [
            [desity_c, Elastic_c, Poisson_c, Conductivity_c, SpecificHeat_c, Expansion_c],
            [desity_b, Elastic_b, Poisson_b, Conductivity_b, SpecificHeat_b, Expansion_b],
            [desity_f, Elastic_f, Poisson_f, Conductivity_f, SpecificHeat_f, Expansion_f],
            [desity_h, Elastic_h, Poisson_h, Conductivity_h, SpecificHeat_h, Expansion_h]
        ]

    # 导入构件
    part_name = ['shell', 'bfc', 'fengtou', 'propeller']
    part_path = [filepath_c, filepath_b, filepath_f, filepath_h]
    part_size = [size_c, size_b, size_f, size_h]

    # 定义一个part类,完成模型导入等过程
    count = 0
    for name, path, size in zip(part_name, part_path, part_size):

        count += 1
        print('{}th, NAME={}, PATH={}, SIZE={}'.format(count+1, name, path, size))
        p = Part(name)
        p.input_part(path)
        p.instance()
        p.gene_mesh(size)

    # 定义一个Property类,完成材料参数导入等过程
    count = int(0)
    for name, mat in zip(part_name, part_property):

        count += 1
        # print('{}th, name={}, path={}, size={}'.format(count+1, name, path, size))
        p_property = Property(name)
        p_property.creat_property(mat)
        p_property.SetSectionAssignment()
        print('{}th, MODULE:PROPERTY {} IS DONE!'.format(count, name))
        # count += 1

    if var_export:
        exportTXT(part_property, 1)


def orthotropic_mat(name, desity, elastic, conductivity, expansion, specific):

    mat = Property_ORT(name)
    mat.ort_property(desity, elastic, conductivity, expansion, specific)

