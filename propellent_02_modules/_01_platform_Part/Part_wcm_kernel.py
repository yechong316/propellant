# coding:utf-8 
'''  
本脚本是要完成导入几何构件并且赋予材料属性，以及完成网格划分
撰写自定义的方法是，
     ~~~内核文件----撰写ABAQUS执行命令流
    --》注册文件plugin -------将内核文件的参数发送到注册文件，重新定义参数，举例如下，plugin文件指向DB文件
            self.inputfileKw = AFXStringKeyword(self.cmd, 'inputfile', True, '')
    --》窗口文件DB  ------ 定义该窗口的位置，标题名等等信息
    其中，因使用WCM插件生成复合材料，故本脚本删去与复合材料相关的所有程序
'''
# 导入ABAQUS必备的方法包
import sys
abaqus_path = ['D:\\SIMULIA\\Abaqus\\6.14-4\\code\\python2.7\\lib',
               'D:\\SIMULIA\\Abaqus\\6.14-4\\tools\\SMApy\\python2.7\\lib',
               'D:\\SIMULIA\\Abaqus\\6.14-4\\code\\bin',
               'D:\\SIMULIA\\Abaqus\\6.14-4\\tools\\SMApy\\python2.7\\lib\\lib-tk',
               'D:\\SIMULIA\\Abaqus\\6.14-4\\tools\\SMApy\\python2.7\\lib\\site-packages',
               'D:\\SIMULIA\\Abaqus\\6.14-4\\tools\\SMApy\\python2.7\\lib\\site-packages\\win32',
               'D:\\SIMULIA\\Abaqus\\6.14-4\\tools\\SMApy\\python2.7\\lib\\site-packages\\win32\\lib',
               'D:\\SIMULIA\\Abaqus\\6.14-4\\tools\\SMApy\\python2.7\\lib\\site-packages\\Pythonwin',
               'D:\\SIMULIA\\Abaqus\\6.14-4\\tools\\SMApy\\python2.7\\DLLs',
               'D:\\Temp',
               'D:\\SIMULIA\\Abaqus\\6.14-4\\code\\bin\\python27.zip',
               'D:\\SIMULIA\\Abaqus\\6.14-4\\tools\\SMApy\\python2.7',
               'D:\\SIMULIA\\Abaqus\\6.14-4\\tools\\SMApy\\python2.7\\lib\\site-packages\\win32',
               'D:\\SIMULIA\\Abaqus\\6.14-4\\tools\\SMApy\\python2.7\\lib\\site-packages\\win32\\lib',
               'D:\\SIMULIA\\Abaqus\\6.14-4\\tools\\SMApy\\python2.7\\lib\\site-packages\\Pythonwin',
               'D:\\SIMULIA\\Abaqus\\6.14-4\\code\\bin', '.',
               'd:\\SIMULIA\\Abaqus\\6.14-4\\code\\python2.7\\lib\\abaqus_plugins\\bin']
from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
import mesh
import os

# 导入自定义的方法包
# cae使用
# from propellent_03_function import *

# kernel命令
from propellent_03_function.propellent_03_function import *
#
this_path = os.path.abspath(os.path.join(os.getcwd(), "")) + '\\abaqus_plugins\\propellant'

os.chdir = (this_path)

'''
本脚本供使用6大函数
var（），判别函数，判断导入，导出，是否使用WCM插件，
Part_WCM_kernel： 外壳复合材料的函数
Part_iron_kernel： 外壳金属的函数
input


'''
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
    ,desity_h=None,                                 Conductivity_h = None,SpecificHeat_h = None, Expansion_h = None, size_h = None
    # 开关函数
     ,var_export=False, var_input=False, var_WCM=False, inputfile=None
        ,elastic_temp=None
):
    # elastic_temp
    Elastic_h = 2e5
    Poisson_h = 0.3
    if var_WCM:
        Part_WCM_kernel(
        # 3个构件文件路径
        filepath_b, filepath_f,filepath_h
        # 2-包覆层的材料参数
        ,desity_b,Elastic_b, Poisson_b,Conductivity_b,  SpecificHeat_b,Expansion_b,size_b
        # 3-封头的材料参数
        ,desity_f, Elastic_f, Poisson_f, Conductivity_f, SpecificHeat_f, Expansion_f, size_f
        # 4-火药的材料参数
        ,desity_h, Elastic_h, Poisson_h, Conductivity_h, SpecificHeat_h, Expansion_h, size_h
        #     数据导入导出
        , var_export=False, var_input=False ,inputfile =None,elastic_temp=None
        )
        if var_export:
            data = [
                # 2-包覆层的材料参数
                [desity_b, Elastic_b, Poisson_b, Conductivity_b, SpecificHeat_b, Expansion_b, size_b],
                # 3-封头的材料参数
                [desity_f, Elastic_f, Poisson_f, Conductivity_f, SpecificHeat_f, Expansion_f, size_f],
                # 4-火药的材料参数
                [desity_h, elastic_temp, 0.3, Conductivity_h, SpecificHeat_h, Expansion_h, size_h],
            ]
            exportTXT(data, 1, WCM_state=var_WCM)
    else:
        Part_iron_kernel(
        # 4个构件文件路径
        filepath_c, filepath_b, filepath_f,filepath_h
        # 1-复合材料的材料参数
        ,desity_c, Elastic_c, Poisson_c, Conductivity_c, SpecificHeat_c, Expansion_c, size_c
        # 2-包覆层的材料参数
        ,desity_b,Elastic_b, Poisson_b,Conductivity_b,  SpecificHeat_b,Expansion_b,size_b
        # 3-封头的材料参数
        ,desity_f, Elastic_f, Poisson_f, Conductivity_f, SpecificHeat_f, Expansion_f, size_f
        # 4-火药的材料参数
        ,desity_h, Elastic_h, Poisson_h, Conductivity_h, SpecificHeat_h, Expansion_h, size_h
        #     数据导入导出
        , var_export=False, var_input=False ,inputfile = None, elastic_temp=None
        )
        if var_export:
            data = [
                # 1-复合材料的材料参数
                [desity_c, Elastic_c, Poisson_c, Conductivity_c, SpecificHeat_c, Expansion_c, size_c],
                # 2-包覆层的材料参数
                [desity_b, Elastic_b, Poisson_b, Conductivity_b, SpecificHeat_b, Expansion_b, size_b],
                # 3-封头的材料参数
                [desity_f, Elastic_f, Poisson_f, Conductivity_f, SpecificHeat_f, Expansion_f, size_f],
                # 4-火药的材料参数
                [desity_h, elastic_temp, 0.3, Conductivity_h, SpecificHeat_h, Expansion_h, size_h],
            ]
            exportTXT(data, 1)




# 当采用复合材料做推进剂外壳时
def Part_WCM_kernel(
        # 3个构件文件路径
        filepath_b, filepath_f,filepath_h
        # 2-包覆层的材料参数
        ,desity_b,Elastic_b, Poisson_b,Conductivity_b,  SpecificHeat_b,Expansion_b,size_b
        # 3-封头的材料参数
        ,desity_f, Elastic_f, Poisson_f, Conductivity_f, SpecificHeat_f, Expansion_f, size_f
        # 4-火药的材料参数
        ,desity_h, Elastic_h, Poisson_h, Conductivity_h, SpecificHeat_h, Expansion_h, size_h
        # 读取文件和输出参数
        ,var_export=False, var_input=False, var_WCM=False, inputfile=None, elastic_temp=None
):
    # 定义3个构件公用的参数，根据inputfile是否为空，取决于后续程序调用哪些参数
    part_list = ['bfc', 'fengtou', 'propeller']
    CAD_list = [filepath_b, filepath_f, filepath_h]

    # 开始判断数据来源， 文件 OR 用户输入
    if var_input == False:
        # 开始生成界面GUI的数据
        # creat_parameter(False, WCM_state=True)

        # 将导入的28个参数拼装成多维矩阵预先定义好3个构件所需要的参数
        size_list = [size_b, size_f, size_h]
        mat_list = [
              [desity_b, Elastic_b, Poisson_b, Conductivity_b, SpecificHeat_b, Expansion_b]
            , [desity_f, Elastic_f, Poisson_f, Conductivity_f, SpecificHeat_f, Expansion_f]
            , [desity_h, Elastic_h, Poisson_h, Conductivity_h, SpecificHeat_h, Expansion_h]
        ]
        # 依次调用3个构件，完成导入构件巴拉巴拉的功能
        for i in range(len(part_list)):
            cad_i = CAD_list[i]
            part_i = part_list[i]
            mat_i = mat_list[i]
            size_i = size_list[i]
            imputCAD_property_instance_mesh(cad_i, part_i, mat_i, size_i)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    else:
        # 用户导入外部txt文本数据
        mat_size_total = readTXT(inputfile, 1)

        # 提取4个构件的网格尺寸
        size_list = [i[6] for i in mat_size_total]

        # 提取4个构件的材料参数
        mat_list = [mat_size_total[0],mat_size_total[1], mat_size_total[2],mat_size_total[3]]
        for i in range(len(mat_size)):
            cad_i = CAD_list[i]
            part_i = part_list[i]
            # 用户输入的材料和网格参数如下：
            mat_i = mat_list[i]
            size_i = size_list[i]
            imputCAD_property_instance_mesh(cad_i, part_i, mat_i, size_i)

    mdb.models['Model-1'].materials['propeller'].Elastic(temperatureDependency=ON,
    table=(
    	(5143.68, 0.271, 306.0), (4292.46, 0.271, 316.0), (3530.65, 0.271,
    326.0)
    ))
    if var_export:
        # print('xxx')
        data = [
              desity_b, Elastic_b, Poisson_b, Conductivity_b, SpecificHeat_b, Expansion_b, size_b
            # 3-封头的材料参数
            , desity_f, Elastic_f, Poisson_f, Conductivity_f, SpecificHeat_f, Expansion_f, size_f
            # 4-火药的材料参数
            , desity_h, elastic_temp, Conductivity_h, SpecificHeat_h, Expansion_h, size_h
        ]

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        exportTXT(data,1, WCM_state=True)



# ABAQUS主函数，也是核心函数
def Part_iron_kernel(
        # 3个构件文件路径
        filepath_c, filepath_b, filepath_f,filepath_h
        # 1-复合材料的材料参数
        , desity_c, Elastic_c, Poisson_c, Conductivity_c, SpecificHeat_c, Expansion_c, size_c
        # 2-包覆层的材料参数
        ,desity_b,Elastic_b, Poisson_b,Conductivity_b,  SpecificHeat_b,Expansion_b,size_b
        # 3-封头的材料参数
        ,desity_f, Elastic_f, Poisson_f, Conductivity_f, SpecificHeat_f, Expansion_f, size_f
        # 4-火药的材料参数
        ,desity_h, Elastic_h, Poisson_h, Conductivity_h, SpecificHeat_h, Expansion_h, size_h

        # 读取文件和输出参数
        ,var_export=False, var_input=False,inputfile=None, elastic_temp=None
):
    # 定义3个构件公用的参数，根据inputfile是否为空，取决于后续程序调用哪些参数
    part_list = ['composite', 'bfc', 'fengtou', 'propeller']
    CAD_list = [filepath_c, filepath_b, filepath_f, filepath_h]
    # 开始判断数据来源， 文件 OR 用户输入
    if var_input == False:
        # 开始生成界面GUI的数据
        # creat_parameter(False)
        # 将导入的28个参数拼装成多维矩阵预先定义好3个构件所需要的参数
        size_list = [size_c, size_b, size_f, size_h]
        mat_list = [
              [desity_c, Elastic_c, Poisson_c, Conductivity_c, SpecificHeat_c, Expansion_c]
            , [desity_b, Elastic_b, Poisson_b, Conductivity_b, SpecificHeat_b, Expansion_b]
            , [desity_f, Elastic_f, Poisson_f, Conductivity_f, SpecificHeat_f, Expansion_f]
            , [desity_h, Elastic_h, Poisson_h, Conductivity_h, SpecificHeat_h, Expansion_h]
        ]
        # 依次调用3个构件，完成导入构件巴拉巴拉的功能
        for i in range(len(part_list)):
            cad_i = CAD_list[i]
            part_i = part_list[i]
            mat_i = mat_list[i]
            size_i = size_list[i]
            imputCAD_property_instance_mesh(cad_i, part_i, mat_i, size_i)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    else:
        # 用户导入外部txt文本数据
        mat_size_total = readTXT(inputfile, 1)

        # 提取4个构件的网格尺寸
        size_list = [i[6] for i in mat_size_total]

        # 提取4个构件的材料参数
        mat_list = [mat_size_total[0],mat_size_total[1], mat_size_total[2],mat_size_total[3]]
        for i in range(len(mat_size)):
            cad_i = CAD_list[i]
            part_i = part_list[i]
            # 用户输入的材料和网格参数如下：
            mat_i = mat_list[i]
            size_i = size_list[i]
            imputCAD_property_instance_mesh(cad_i, part_i, mat_i, size_i)

    mdb.models['Model-1'].materials['propeller'].Elastic(temperatureDependency=ON,
    table=(
    	(5143.68, 0.271, 306.0), (4292.46, 0.271, 316.0), (3530.65, 0.271,
    326.0)
    ))

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # 当用户勾选后，执行操作
    if var_export:

        data = [
              desity_c, Elastic_c, Poisson_c, Conductivity_c, SpecificHeat_c, Expansion_c, size_c
            # 2-包覆层的材料参数
            , desity_b, Elastic_b, Poisson_b, Conductivity_b, SpecificHeat_b, Expansion_b, size_b
            # 3-封头的材料参数
            , desity_f, Elastic_f, Poisson_f, Conductivity_f, SpecificHeat_f, Expansion_f, size_f
            # 4-火药的材料参数
            , desity_h, Elastic_h, Poisson_h, Conductivity_h, SpecificHeat_h, Expansion_h, size_h
        ]

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        exportTXT(data,1, WCM_state=True)

# 开始副函数 --2019年2月27日16:59:29 以前的版本，准备进行代码分解
def imputCAD_property_instance_mesh(part_path, part, mat , size):
    '''
    传入参数，ABAQUS后台执行导入构件，材料属性，划分网格等操作，所有参数均为浮点、整型等
    :param filepath: 构件路径
    :param part: 构件名称，eg： composiste，propellent
    :param mat:  材料属性，是一个1 × 7 的矩阵，分别为密度、弹性模量等
    :param size: 1 × n的矩阵，分别为n个构件的网格尺寸
    :param :  ：复合材料 推进剂， 封头，包覆层
    :return: 执行命令
    '''

    acis = mdb.openAcis(part_path, scaleFromFile=OFF)
    mdb.models['Model-1'].PartFromGeometryFile(name=part, geometryFile=acis,
                                               combine=False, dimensionality=THREE_D, type=DEFORMABLE_BODY)
    print('    {} has been imported to CAE!'.format(part))

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # 材料属性生成
    mat_name = mdb.models['Model-1'].Material(name=part)
    mat_name.Density(table=((mat[0],),))
    mat_name.Elastic(table=((mat[1], mat[2]),))
    mat_name.Conductivity(table=((mat[3],),))
    mat_name.SpecificHeat(table=((mat[4],),))
    mat_name.Expansion(table=((mat[5],),))
    mdb.models['Model-1'].HomogeneousSolidSection(name=part + '_section',
                                                  material=part, thickness=None)
    print('    The property of {} has been generated!'.format(part))

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # 生成实例 + 截面属性赋予
    a = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts[part]
    a.Instance(name= part + '-1', part=p, dependent=ON)
    # 获取p实体的所有cells
    c= p.cells
    # pickedCells为所有cells
    pickedCells = c[:]
    # 为该cells创建一个名为Set-composite的集合
    p.Set(cells=pickedCells, name='Set-' + part)
    # region为获取名为Set-composite的集合
    region = p.sets['Set-' + part]
    p.SectionAssignment(region=region, sectionName=part + '_section', offset=0.0,
                          offsetType=MIDDLE_SURFACE, offsetField='',
                          thicknessAssignment=FROM_SECTION)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # 划分网格,注，仅支持划分solid单元
    elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD,
                              kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF,
                              hourglassControl=DEFAULT, distortionControl=DEFAULT)
    elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
    elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
    p.setMeshControls(regions=pickedCells, elemShape=HEX, technique=SWEEP,
                        algorithm=ADVANCING_FRONT)
    p.setElementType(regions=region, elemTypes=(elemType1, elemType2,
                                                    elemType3))
    p.seedPart(size=size, deviationFactor=0.1, minSizeFactor=0.1)
    p.generateMesh()
    # print('    Mesh {} successfully!'.format(part))

# 开始导入构件
def ImputCAD(filepath, name):
    '''
    传入参数，ABAQUS后台执行导入构件，材料属性，划分网格等操作，所有参数均为浮点、整型等
    :param filepath: 构件路径
    :param part: 构件名称，eg： composiste，propellent
    :param part_hanzi:  ：复合材料 推进剂， 封头，包覆层
    :return: 执行命令
    '''
    # 导入构件
    acis = mdb.openAcis(filepath, scaleFromFile=OFF)
    mdb.models['Model-1'].PartFromGeometryFile(name=name, geometryFile=acis,
                                               combine=False, dimensionality=THREE_D, type=DEFORMABLE_BODY)
    print('   - Finish {} import to model ...'.format(name))

# 开始生成材料属性
def Property(name, desity, elastic, conductivity, expansion, specific):

    # 材料属性生成
    mat_name = mdb.models['Model-1'].Material(name=name)

    # 生成密度
    mat_name.Density(table=((desity,),))

    # 根据材料是否各项异性输入弹性模量
    print('The elastic which user inputs is %s'.format(elastic))
    mat_name.Elastic(type=ENGINEERING_CONSTANTS,table=elastic)

    # 根据材料是否各项异性输入热传导
    mat_name.Conductivity(type=ORTHOTROPIC,table=conductivity)

    # 输入比热容
    mat_name.SpecificHeat(table=((specific,),))

    # 输入热膨胀
    mat_name.Expansion(type=ORTHOTROPIC,table=expansion)
    # orientation = mdb.models['Model-1'].parts['Tank-1'].datums[267]
    # mdb.models['Model-1'].parts['Tank-1'].MaterialOrientation(region=region,
    #                                                           orientationType=SYSTEM, axis=AXIS_3,
    #                                                           localCsys=orientation, fieldName='',
    #                                                           additionalRotationType=ROTATION_NONE, angle=0.0,
    #                                                           additionalRotationField='', stackDirection=STACK_3)

    print('   - Finish generating {} propertes...'.format(name))

# 开始划分网格
def Mesh(name,size):
    '''
    传入参数，ABAQUS后台执行导入构件，材料属性，划分网格等操作，所有参数均为浮点、整型等
    :param size: 1 × n的矩阵，分别为n个构件的网格尺寸
    :return: 执行命令
    '''


    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # 生成实例 + 截面属性赋予
    a = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts[name]
    a.Instance(name= name + '-1', part=p, dependent=ON)
    # 获取p实体的所有cells
    c= p.cells[:]
    # 为该cells创建一个名为Set-composite的集合
    p.Set(cells=pickedCells, name='Set-' + name)
    # region为获取名为Set-composite的集合
    region = p.sets['Set-' + name]
    p.SectionAssignment(region=region, sectionName=name + '_section', offset=0.0,
                          offsetType=MIDDLE_SURFACE, offsetField='',
                          thicknessAssignment=FROM_SECTION)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # 划分网格,注，仅支持划分solid单元
    elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD,
                              kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF,
                              hourglassControl=DEFAULT, distortionControl=DEFAULT)
    elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
    elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
    p.setMeshControls(regions= mdb.models['Model-1'].parts[name].cells[:], elemShape=HEX, technique=SWEEP,
                        algorithm=ADVANCING_FRONT)
    p.setElementType(regions=region, elemTypes=(elemType1, elemType2,
                                                    elemType3))
    p.seedPart(size=size, deviationFactor=0.1, minSizeFactor=0.1)
    p.generateMesh()
    print('   - Finish creat {} mesh ...')

