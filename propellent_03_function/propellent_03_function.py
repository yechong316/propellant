#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : propellant_function_total.py
# @Author: YC
# @Date  : 2019/1/25
'''
所有文件默认在启动py脚本中搜索

'''
import datetime
import sys
import os

from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
from odbAccess import *
import mesh

# from propellant_output_pick import *
from propellent_03_function import *

# 定义参数文本、子程序文本的默认地址
userfile_path = os.path.abspath(os.path.join(os.getcwd(), "")) + '\\abaqus_plugins\\propellant\\propellent_05_Subfile\\'
data_path = os.path.abspath(os.path.join(os.getcwd(), "")) + '\\abaqus_plugins\\propellant\\propellent_04_data\\'

# 以下代码是提取当前模型的所有part的名称，并将tank的名称添加到现有part_list
part_list = ['unknown', 'bfc', 'fengtou', 'propeller']
p_total = mdb.models['Model-1'].parts
part_model = [key for key in p_total.keys()]
for part, num in zip(part_model, range(len(part_list))):
    if part != 'bfc' and part != 'fengtou' and part != 'propeller':
        part_list[0] = part_model[num]

# 以下代码是提取当前模型的所有instance的名称，并将tank的名称添加到现有instance_list
instance_list = ['unknown', 'bfc-1', 'fengtou-1', 'propeller-1']
instance_total = mdb.models['Model-1'].rootAssembly.instances
instance_model = [key for key in instance_total.keys()]
for instance in instance_model:
    if instance not in instance_list:
        instance_list[0] = instance

class Part(object):
    '''
    本类中储存所有ABAQUS关于PART模块中的所有操作
    '''
    def __init__(self, part, part_path):
        self.part = part
        self.part_path = part_path

    def import_part(self, part, part_path):
        # 导入构件,默认为sat文件
        acis = mdb.openAcis(part_path, scaleFromFile=OFF)
        mdb.models['Model-1'].PartFromGeometryFile(name=part, geometryFile=acis,
        combine=False, dimensionality=THREE_D, type=DEFORMABLE_BODY)
        print('{} has been imported to CAE!'.format(part))

def FaceIndex2region(indexlist, num):
    '''
    根据面的索引号序列，返回一个sideface，供上级程序建立一个region面，生成绑定关系或者
    面上的载荷的等
    :param indexlist:
    :param num:
    :return:
    '''
    a = mdb.models['Model-1'].rootAssembly
    side1Faces = []
    for i in range(len(indexlist)):
        side1Faces.append(a.instances[instance_list[num]].faces[indexlist[i]:indexlist[i] + 1])
    return side1Faces




def creat_thermal_user_data(table_list):
    '''
    2019年1月28日09:48:07  ---本函数没有问题，别看了~~~~
    根据用户输入的升降温曲线，自动生成子程序中需要的语句
    eg：if***
    elseif****
    :param table_list: 用户输入的升降温曲线
    :return: 两个文件的绝对路径,并且组成列表
    '''
    #开始生成 DISP_temp.txt
    DISPdata_file = userfile_path + 'DISP_temp.txt'
    with open(DISPdata_file, 'w+') as f:
        num = len(table_list)
        count = 0
        s_if = '      IF(TIME(2).LE.' + str(table_list[1][0]) + ')THEN'
        f.write(s_if)
        f.write('\n')
        s_U1 = '          U(1)=' + str(table_list[0][1]) + '+TIME(2)*' + str(
            (table_list[1][1] - table_list[0][1]) / (table_list[1][0] - table_list[0][0]))
        f.write(s_U1)
        f.write('\n')
        for i in range(1, len(table_list) - 1):
            s_elif = '      ELSEIF(TIME(2).LE.' + str(table_list[i + 1][0]) + ')THEN'
            f.write(s_elif)
            f.write('\n')
            s_U1 = '          U(1)=' + str(table_list[i][1]) + '+TIME(2)*' + str(
                (table_list[i + 1][1] - table_list[i][1]) / (table_list[i + 1][0] - table_list[i][0]))
            f.write(s_U1)
            f.write('\n')
    # print('%s Is Done!'%DISPdata_file)

    # 开始生成 FILM。txt
    FILMdata_file = userfile_path + 'FILM_temp.txt'
    with open(FILMdata_file, 'w') as f:
        s_if = '      IF(TIME(2).LE.' + str(table_list[1][0]) + ')THEN'
        f.write(s_if)
        f.write('\n')
        s_U1 = '          SINK=' + str(table_list[0][1]) + '+TIME(2)*' + str(
            (table_list[1][1] - table_list[0][1]) / (table_list[1][0] - table_list[0][0]))
        f.write(s_U1)
        f.write('\n')
        for i in range(1, len(table_list) - 1):
            s_elif = '      ELSEIF(TIME(2).LE.' + str(table_list[i + 1][0]) + ')THEN'
            f.write(s_elif)
            f.write('\n')
            s_U1 = '          SINK=' + str(table_list[i][1]) + '+TIME(2)*' + str(
                (table_list[i + 1][1] - table_list[i][1]) / (table_list[i + 1][0] - table_list[i][0]))
            f.write(s_U1)
            f.write('\n')
    # print('%s Is Done!'%FILMdata_file)

    # 两个文本的路径转为 列表 并且输出
    DISP_FILM_file = []
    DISP_FILM_file.append(FILMdata_file)
    DISP_FILM_file.append(DISPdata_file)

    return DISP_FILM_file

# 获取文件中标记所在的位置
def access_taget(label,file):

    '''
    2019年1月28日09:48:21 应该也没有问题，别看了
    读取初始子程序文件，根据预先写的标识符号获取当前行号
    :param label: 位置标号， cDISP,cFILM
    :return: 返回数字，int
    '''
    f = open(file, 'r')
    lines = []
    for line in f:
        lines.append(line)
    f.close()
    for i in range(len(lines)):
        if lines[i] == label + '\n':
            return i

def write_data(insert_user_name,num,insert_data_file):
    '''
    本函数的功能在于：可以insert_data_file将插入到insert_user_name的行号num前面，然后返回新的文本路径
    :param num: 用户必须两个两个的传入参数，第一个是行号，第二个是插入的文本绝对路径
    :param insert_data_file: 用户需要写入的子程序文本
    :return: 本函数注意是输出.for文件的路径
    '''
    f = open(insert_user_name, 'r')  # your path!
    lines_old = []
    for line in f:
        lines_old.append(line)
    f.close()

    # 开始读取当前insert文件,将所有的子程序文本存入lines_user_FILM
    lines_user_FILM = []
    f2 = open(insert_data_file, 'r')  # your path!
    for line in f2:
        lines_user_FILM.append(line)
    f2.close()

    # 再把读到的lines__user写入到lines_old
    for i in range(len(lines_user_FILM)):
        lines_old.insert(num + i, lines_user_FILM[i] + '\n')  # 第四行插入666并回车

    s = ''.join(lines_old)
    # 新建一个文本，开始写入上述文本，并返回将来子程序。for文件
    user_current = userfile_path + 'Propellant_' + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') +'.for'
    f = open(user_current, 'w+')  # 重新写入文件
    f.write(s)
    f.close()
    del lines_old[:]  # 清空列表
    # print('%s has been write %s'%(insert_data_file,user_current))
    return user_current



# 定义热传递单元
def assign_DC3D8_element(part):
    '''
    输入：构件名称
    输出：无
    功能：赋予热传递单元属性
    '''
    a = mdb.models['Model-1'].rootAssembly
    '''
    对当前单元赋予热传递单元属性
    '''
    elemType1 = mesh.ElemType(elemCode=DC3D8, elemLibrary=STANDARD)
    elemType2 = mesh.ElemType(elemCode=DC3D6, elemLibrary=STANDARD)
    elemType3 = mesh.ElemType(elemCode=DC3D4, elemLibrary=STANDARD)
    a = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts[part]

    # 获取p实体的所有cells
    c = p.cells
    pickedCells_h = c[:]
    p.Set(cells=pickedCells_h, name='Set-' + part)

    # region为获取名为Set-composite的集合
    region_h = p.sets['Set-' + part]
    p.setMeshControls(regions=pickedCells_h, elemShape=HEX, technique=SWEEP,
                      algorithm=ADVANCING_FRONT)
    p.setElementType(regions=region_h,
                     elemTypes=(elemType1, elemType2,elemType3))
    p.generateMesh()
    print('    {} has been assigned heat transfer element property!'.format(part))

# 定义静态通用单元
def creat_static_element(part):
    '''
    对当前单元赋予静态分析类型
    :param part:
    :return:
    '''
    elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD,
                              kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF,
                              hourglassControl=DEFAULT, distortionControl=DEFAULT)
    elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
    elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
    a = mdb.models['Model-static'].rootAssembly
    p = mdb.models['Model-static'].parts[part]
    # 获取p实体的所有cells
    c = p.cells
    # pickedCells为所有cells
    pickedCells_h = c[:]
    # region为获取名为Set-composite的集合
    region_h = (pickedCells_h,)
    p.setElementType(regions=region_h, elemTypes=(elemType1, elemType2,
                                                       elemType3))
    #p.seedPart(size=size, deviationFactor=0.1, minSizeFactor=0.1)
    #p.generateMesh()
    print('    {} has been assigned '.format(part))

# 定义初始温度场
def generate_pickCells(part) :
    '''
    :param part:
    :return:
    '''
    a = mdb.models['Model-1'].rootAssembly
    c1 = a.instances[instance_list[0]].cells
    pickedCells1 = c1[:]

    return pickedCells1

# 定义复合材料的子程序属性
def creat_user_composite(mat):
    '''
    # 复合材料属性中新增子程序属性
    :param part:
    :return:
    '''
    mdb.models['Model-1'].materials[mat].Depvar(n=1)
    mdb.models['Model-1'].materials[mat].UserDefinedField()
    mdb.models['Model-1'].materials[mat].HeatGeneration()
    # 在信息栏中输出  ---  复合材料子程序材料属性定义成功!
    print('    {} has been add property of user subroutines!'.format(mat))

# 定义生成job
def creat_job(job_name_1,cpu_num_1, user = ''):
    mdb.Job(name=job_name_1, model='Model-1', description='', type=ANALYSIS,
            atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
            memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
            explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
            modelPrint=OFF, contactPrint=OFF, historyPrint=OFF,
            userSubroutine=user, scratch='',
            resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=cpu_num_1, numGPUs=0)
    # 在信息栏中输出  ---  job_name_1已成功生成
    print(b'    %s has been generated!'%job_name_1)

# 修改inp文件,加入USDFLD关键词
def modefiled_inp(inp_name_1, X1=None):
    f = open(inp_name_1, "r")
    for num, value in enumerate(f):
        if value == '*Initial Conditions, type=TEMPERATURE\n':
            target_num = num
    lines = []
    f.close()
    f = open(inp_name_1, 'r')  # your path!
    for line in f:
        lines.append(line)
    f.close()
    lines.insert(target_num, "*INITIAL CONDITIONS, TYPE=FIELD, VARIABLE=1\n")
    s = ''.join(lines)
    Job_name1 = 'curing-'
    new_inp_filepath = X1 + r':\\temp\\' + Job_name1 + '-modefied' + '.inp'
    f = open(new_inp_filepath, 'w+')  # 重新写入文件
    f.write(s)
    f.close()
    time_modefied = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    Job_new_name = Job_name1 + time_modefied + '-modefied'
    # 在信息栏中输出  ---  插入关键词成功
    # print('%s.inp\xb2\xe5\xc8\xeb\xb9\xd8\xbc\xfc\xb4\xca\xb3\xc9\xb9\xa6!'%inp_name_1)
    #在信息栏中输出  ---  新的inp文件为：new_inp_filepath
    print('    new_inp_filepath is :%s.'%new_inp_filepath)
    list = []
    list.append(Job_new_name)
    list.append(new_inp_filepath)
    return list

# 该函数是根据用户输入的升降温曲线添加至子程序文本中
def del_mat_property(mat_name):
    # 删去无用热学参数，其中保留复合材料的热膨胀系数
    del mdb.models['Model-1'].materials[mat_name].conductivity
    del mdb.models['Model-1'].materials[mat_name].specificHeat
    if mat_name != 'composite':
        del mdb.models['Model-1'].materials[mat_name].expansion


# 固化工艺和温度冲击工艺可以共用此喊
def generate_init_temprature(intialtemp):
    a = mdb.models['Model-1'].rootAssembly
    #part_list = ['Tank', 'bfc', 'fengtou', 'propeller']
    num_3 = 0
    # 依次调用4个构件,将提取的cell累加,定义初始温度场中
    for i in part_list:
        # 4个构件的cell累加
        if num_3 == 0:
            num_3 = 1
            pickedCells = generate_pickCells(i)
        else:
            pickedCells += generate_pickCells(i)
    a.Set(cells=pickedCells, name='Set-total')
    region_total = a.sets['Set-total']
    mdb.models['Model-1'].Temperature(name='Predefined Field-total', createStepName='Initial',
                                      region=region_total, distributionType=UNIFORM,
                                      crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, magnitudes=(intialtemp,))
    print('Generating initial temprature field in the all parts!')

def initThermal_mesh(part,start_temp):
    mdb.models['Model-1'].materials['bfc'].elastic.setValues(table=((7.8, 0.3),))
    #
    # #####################
    # 开始赋予力学单元属性
    elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD,
                              kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF,
                              hourglassControl=DEFAULT, distortionControl=DEFAULT)
    elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
    elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
    p = mdb.models['Model-1'].parts[part]
    # 获取p实体的所有cells
    c= p.cells
    # pickedCells为所有cells
    pickedCells = c[:]
    # 为该cells创建一个名为Set-composite的集合
    p.Set(cells=pickedCells, name='Set-' + part + 'load')
    # region为获取名为Set-composite的集合
    region = p.sets['Set-' + part + 'load']
    p.setElementType(regions=region, elemTypes=(elemType1, elemType2,
                                                       elemType3))
    # 导出每个构件的cell


    print('   {} has been assigned C3D8R element property'.format(part))


# 将字符串索引转变为数字序列
def str_indes2Face(str):
    '''
    一、提取用户选取的面 的索引
    二。组成序列后转换为字符串序列
    eg：'2 3 15 18'
    返回的是：[2, 3, 15, 18]
    '''
    numbers = map(int, str.split(' '))
    # print('str_index has been transfer index')
    return numbers
    '''
    一、提取用户选取的面 的索引
    二。组成序列后转换为字符串序列
    eg：'2 3 15 18'
    返回的是：[2, 3, 15, 18]
    '''
    # print(sys._getframe().f_lineno)
    list = []
    list = str.split(' ')
    numbers = map(int, list)
    for i in numbers:
        list.append(i)
    str2 = ' '.join([str(x) for x in list])
    # print('Face has been transfer str_index')
    # print(list)
    # print(str2)
    return str2

# 将字符串布尔值 ---》 布尔值
def str2bool(str):
    if str == 'True':
        return True
    else:
        return False

def Face2str_indes(face):
    '''
    一、提取用户选取的面 的索引
    二。组成序列后转换为字符串序列
    eg：[2, 3, 15, 18]
    返回的是：'2 3 15 18'
    '''
    current = 0
    # print('    Face2str_indes is active,This is %d'%current)
    print('    The face which user picks in GUI is %s', face)

    list = []

    for i in face:
        # print(i.index)
        list.append(i.index)
    str2 = ' '.join([str(x) for x in list])
    # print('Face has been transfer str_index')
    # print(list)
    # print(str2)
    current += 1
    return str2


def bool2str(str):
    if str == True:
        return 'True'
    else:
        return 'False'
#



def creat_thermal_force_element(part):
    '''
    功能:对传入的part赋予C3D8R,无返回值
    输入：构件名称，eg："bfc"
    输出：无返回值，仅为赋予属性
    '''

    # 定义单元类型
    elemType1 = mesh.ElemType(elemCode=C3D8T, elemLibrary=STANDARD,
                              secondOrderAccuracy=OFF, distortionControl=DEFAULT)
    elemType2 = mesh.ElemType(elemCode=C3D6T, elemLibrary=STANDARD)
    elemType3 = mesh.ElemType(elemCode=C3D4T, elemLibrary=STANDARD)

    # 获取part
    # m1 = [key for key in m.keys()]  这是第二种提取model方法，
    # 暂存后续有要求可更改
    # >> > m1
    # ['Model-1', 'Model-1-Copy']
    p_func = mdb.models['Model-1'].parts[part]
    # 获取p实体的所有cells
    c_func = p_func.cells
    # pickedCells为所有cells
    pickedCells_h = c_func[:]
    # region为获取名为Set-composite的集合
    region_func = (pickedCells_h,)
    p_func.setElementType(regions=region_func, elemTypes=(elemType1, elemType2,elemType3))
    print('  Finish assigned {} to C3D8R!'.format(part))

def creat_initThermal(part) :
    '''
    生成初始温度场
    输入：构件名称，eg："bfc"
    输出：无返回值
    '''
    a = mdb.models['Model-1'].rootAssembly
    c1 = a.instances[instance_list[0]].cells
    pickedCells1 = c1[:]

    print('  Finish creating initial thermal field in the {}!'.format(part))
    return pickedCells1

def exportTXT(data_total,plug_type, WCM_state=False):

    '''
    要求用户输入一个列表，该列表中包含你想到导出的数据，然后根据不同的插件定制成不同的形式
    plug_type = 1 表示插件1，等于2表示写入插件2，依次类推
    输入：每个插件的函数参数和num
    输出：导出该参数到预先定义好的文本中
    :param data:
    :return:
    '''
    time_property = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    # 导入构件
    if plug_type == 1:
        if WCM_state:
            partlist = ['包覆层:', '封头:', '推进剂:']
            file_name = 'Property_WCM_v'
        else:
            partlist = ['复合材料壳体:', '包覆层:', '封头:', '推进剂:']
            file_name = 'Property_v'
        data_txt_name = file_name + time_property + '.txt'
        data_file = data_path + data_txt_name

        fileObject = open(data_file, 'w')
        fileObject.write('使用说明：每一行的数据分别为该构件的'
                         '密度、弹性模量、泊松比、热传导系数、比热容系数、热膨胀系数和网格尺寸')
        fileObject.write('\n')
        for i in range(len(partlist)):
            fileObject.write(partlist[i])
            for j in range(len(data_total[i])):
                fileObject.write(str(data_total[i][j]))
                fileObject.write('、')
            fileObject.write('\n')
        fileObject.close()

        # 打印已成功导出参数
        print('PROPERTY DATA HAS BEEN EXPORTED SUCCESSFULLY!')

    # 绑定关系
    elif plug_type == 2:
        if WCM_state:
            partlist = ['包覆层:', '封头:', '推进剂:']
            file_name = 'Tie_WCM_v'
        else:
            partlist = ['复合材料壳体:', '包覆层:', '封头:', '推进剂:']
            file_name = 'Tie_v'
        # print('Tie_data is exporting...')
        for i in range(len(data_total)):
            for j in range(len(data_total[i])):
                pass

        # 首先用户输入的参数进行格式转换，将所有的浮点，布尔，Face，统统变成字符串形式
        data_total = [
            [Face2str_indes(data_total[0][0]), Face2str_indes(data_total[0][1]), str(data_total[0][2]), bool2str(data_total[0][3])],
            [Face2str_indes(data_total[1][0]), Face2str_indes(data_total[1][1]), str(data_total[1][2]), bool2str(data_total[1][3])],
            [Face2str_indes(data_total[2][0]), Face2str_indes(data_total[2][1]), str(data_total[2][2]), bool2str(data_total[2][3])],
            [Face2str_indes(data_total[3][0]), Face2str_indes(data_total[3][1]), str(data_total[3][2]), bool2str(data_total[3][3])]
        ]

        # 定义一个数据文本
        fi
        data_txt_name = file_name + time_property + '.txt'
        data_file = data_path + data_txt_name

        # 逐步写入的文本的抬头，每行的起始信息：利于用户读懂该文件
        fileObject = open(data_file, 'w')
        # print(sys._getframe().f_lineno)
        fileObject.write('使用说明：每一行的数据分别为该构件的'
                         '主面坐标、从面坐标、位置容差、是否切换主从面')
        fileObject.write('\n')
        for i in range(4):
            # print(sys._getframe().f_lineno)
            if i == 0 :
                # print(sys._getframe().f_lineno)
                fileObject.write('复合材料VS包覆层:')
                for j in range(4):
                    # print(data_total[i][j])
                    # print(sys._getframe().f_lineno)
                    fileObject.write((data_total[i][j]))
                    fileObject.write('、')
                fileObject.write('\n')
                # print('FHCL-BFC SUCCESSFUL!')

            elif i == 1:
                # print(sys._getframe().f_lineno)
                fileObject.write('包覆层VS封头:')
                for j in range(4):
                    fileObject.write((data_total[i][j]))
                    fileObject.write('、')
                fileObject.write('\n')
                # print('BFC-FENGTOU SUCCESSFUL!')

            elif i == 2:
                #print(sys._getframe().f_lineno)
                fileObject.write('包覆层VS推进剂:')
                for j in range(4):
                    # print(sys._getframe().f_lineno)
                    fileObject.write((data_total[i][j]))
                    fileObject.write('、')
                fileObject.write('\n')
                # print('BH SUCCESSFUL!')

            elif i == 3:
                # print(sys._getframe().f_lineno)
                fileObject.write('推进剂VS封头:')
                for j in range(4):
                    # print(sys._getframe().f_lineno)
                    fileObject.write((data_total[i][j]))
                    fileObject.write('、')
                fileObject.write('\n')
                # print('HF SUCCESSFUL!')
        fileObject.close()

        # 告诉用户已成功导出参数
        print('TIE DATA_TOTAL HAS BEEN PRINT!')

    # 温度冲击
    elif plug_type == 3:
        # print('export data_total to thermal_*.txt')
        data_file = data_path + 'Thermal_v' + time_property + '.txt'

        # 新建该文本，开始写入数据，刚开始写入文本标题
        fileObject = open(data_file, 'w')
        fileObject.write('使用说明：每一行的数据分别对应温度冲击试验时间，'
                         '构件初始温度，升降温曲线，复合材料外表面坐标，CPU核数\n')

        # 开始写入数据
        fileObject.write('温度冲击试验时间:')
        fileObject.write(str(data_total[0]))
        fileObject.write('\n')
        fileObject.write('构件初始温度:')
        fileObject.write(str(data_total[1]))
        fileObject.write('\n')
        fileObject.write('升降温曲线:')
        fileObject.write(data_total[2].__str__())
        fileObject.write('\n')
        fileObject.write('复合材料外表面索引:')
        fileObject.write(Face2str_indes(data_total[3]))
        fileObject.write('\n')
        fileObject.write('CPU核数:')
        fileObject.write(str(data_total[4]))

        fileObject.close()
        # 打印已成功导出参数
        print('The temprature shock parameters have been sucessfully exported!')

    # 固化工艺
    elif plug_type == 4:
        data_txt_name = 'Curing_v' + time_property + '.txt'
        data_file = data_path + data_txt_name
        fileObject = open(data_file, 'w')
        fileObject.write('使用说明：每一行的数据分别对应固化工艺时间，'
                         '构件初始温度，升降温曲线，复合材料外表面坐标，CPU核数')
        fileObject.write('\n')
        fileObject.write('固化工艺时间:')
        fileObject.write(str(data_total[0]))
        fileObject.write('\n')
        fileObject.write('构件初始温度:')
        fileObject.write(str(data_total[1]))
        fileObject.write('\n')
        fileObject.write('升降温曲线:')
        fileObject.write(data_total[2].__str__())
        fileObject.write('\n')
        fileObject.write('复合材料外表面索引:')
        fileObject.write(Face2str_indes(data_total[3]))
        fileObject.write('\n')
        fileObject.write('CPU核数:')
        fileObject.write(str(data_total[4]))
        fileObject.close()
        # 打印已成功导出参数
        print('The data of curing is successfully exported to {}!'.format(data_txt_name))

    # 缠绕工艺
    elif plug_type == 5:
        data_txt_name = data_path + 'Warp_v' + time_property + '.txt'
        fileObject = open(data_txt_name, 'w')
        fileObject.write('使用说明：每一行的数据分别对应预紧力，'
                         '纤维铺层厚度，纤维宽度，CPU核数')
        fileObject.write('\n')
        fileObject.write(str(data_total[0]))
        fileObject.write('\n')
        fileObject.write(str(data_total[1]))
        fileObject.write('\n')
        fileObject.write(str(data_total[2]))
        fileObject.write('\n')
        fileObject.write(str(data_total[3]))
        fileObject.close()
        # 打印已成功导出参数
        print('The data of warp has been exported to {}!!!'.format(data_txt_name))


# 读取材料参数
def readTXT(txtname, plug_type):
    '''
    要求用户导入一个文件，然后根据不同的文件类型进行读取
    plug_type = 1 表示插件1，等于2表示写入插件2，依次类推,返回没有任何换行符号的字符串
    '''
    # 将删去汉字等无用符号的文本存入到一个临时文件中
    file = 'data_temp.txt'

    # 导入构件
    if plug_type == 1:
        # print('READTXT IS SUCCESSFUL STARTING!!!')
        # 打开该txt文件
        with open(txtname, 'r') as f:
            data_origin = f.read()
        #     删除无用汉字文本
        data_origin = data_origin.replace('复合材料壳体:', '')
        data_origin = data_origin.replace('使用说明：每一行的数据分别为该构件的密度、弹性模量、泊松比、热传导系数、比热容系数、热膨胀系数和网格尺寸', '')
        data_origin = data_origin.replace('包覆层:', '')
        data_origin = data_origin.replace('封头:', '')
        data_origin = data_origin.replace('推进剂:', '')
        with open(file, 'w') as fpw:
            fpw.write(data_origin)
        # data_total = data_origin
        F1 = open(file, "r")
        data_total = F1.readlines()
        mat_size = []
        for i in range(1, len(data_total)):
            data_None_str = data_total[i].strip().split("、")  # 每一行split后是一个列表
            data_str = filter(None, data_None_str)
            data = map(float, data_str)
            mat_size.append(data)
            # for j in data_str:
            #     data_str
            # mat_size.append(map(float, data_str))
            # for j in range(len(data_total[i])):

            # print('before:', type(data_str[i]))
            # map(float, filter(None, data_str[i]))

            # print('after:', type(data_str[i]))
        #  jiang

        # for i in range(1, len(list_source)):
        #     mat_size.append(map(float, filter(None, list_source[i])))
        F1.close()
        # print('The data from {} has been imported to CAE!'.format(txtname))
        return mat_size

    # 绑定关系
    elif plug_type == 2:
        # print('READTXT TIE IS SUCCESSFUL STARTING')
        # 打开该txt文件
        with open(txtname, 'r') as f:
            data_origin = f.read()

        #     删除无用汉字文本
        data_origin = data_origin.replace('推进剂VS封头:', '')
        data_origin = data_origin.replace('使用说明：每一行的数据分别为该构件的主面坐标、从面坐标、位置容差、是否切换主从面', '')
        data_origin = data_origin.replace('复合材料VS包覆层:', '')
        data_origin = data_origin.replace('包覆层VS封头:', '')
        data_origin = data_origin.replace('包覆层VS推进剂:', '')

        # 将处理后的数据写入到临时文本，然后将存到list_source中
        with open(file, 'w') as fpw:
            fpw.write(data_origin)
        # data_total = data_origin
        F1 = open(file, "r")
        data_total = F1.readlines()
        data_tie = []
        for i in range(1, len(data_total)):
            data_None_str = data_total[i].strip().split("、")  # 每一行split后是一个列表
            data_str = filter(None, data_None_str)
            data_tie.append(data_str)

        data = [
            [str_indes2Face(data_tie[0][0]), str_indes2Face(data_tie[0][1]), float(data_tie[0][2]),
             str2bool(data_tie[0][3])],
            [str_indes2Face(data_tie[1][0]), str_indes2Face(data_tie[1][1]), float(data_tie[1][2]),
             str2bool(data_tie[1][3])],
            [str_indes2Face(data_tie[2][0]), str_indes2Face(data_tie[2][1]), float(data_tie[2][2]),
             str2bool(data_tie[2][3])],
            [str_indes2Face(data_tie[3][0]), str_indes2Face(data_tie[3][1]), float(data_tie[3][2]),
             str2bool(data_tie[3][3])],
        ]
        # print('The data[3][3]  of tie is :',data[3][3])
        return data

    # 温度冲击
    elif plug_type == 3:
        # print('readTXT-functiong is successful starting')

        # 打开该txt文件
        with open(txtname, 'r') as f:
            data_origin = f.read()
        #     删除无用汉字文本
        data_origin = data_origin.replace('温度冲击试验时间:', '')
        data_origin = data_origin.replace('使用说明：每一行的数据分别对应温度冲击试验时间，构件初始温度，升降温曲线，复合材料外表面坐标，CPU核数', '')
        data_origin = data_origin.replace('构件初始温度:', '')
        data_origin = data_origin.replace('升降温曲线:', '')
        data_origin = data_origin.replace('复合材料外表面索引:', '')
        data_origin = data_origin.replace('CPU核数:', '')
        # print('After delete:data_origin:')
        # print(data_origin)
        with open(file, 'w') as fpw:
            fpw.write(data_origin)
        data_total = data_origin
        F1 = open(file, "r")
        data_total = F1.readlines()
        list_source = []
        for i in range(len(data_total)):
            data_str = data_total[i]  # 每一行split后是一个列表
            list_source.append(data_str)
        for line in F1.readlines():
            line = line.strip('\n')
        # print('End of data_thermal reading!')
        # 开始删除空格符号
        list = []
        for i in list_source:
            if i != '\n':
                list.append(i)
        for i in list:
            i.replace('\n', '')
        print('Finish gain the thermal data from txt!')
        # print('Thermal Data is :')
        # print(list)
        return list

    # 固化工艺
    elif plug_type == 4:
        # print('readTXT is successful starting')
        # 打开该txt文件
        with open(txtname, 'r') as f:
            data_origin = f.read()
        #     删除无用汉字文本
        data_origin = data_origin.replace('固化工艺时间:', '')
        data_origin = data_origin.replace('使用说明：每一行的数据分别对应固化工艺时间，构件初始温度，升降温曲线，复合材料外表面坐标，CPU核数', '')
        data_origin = data_origin.replace('构件初始温度:', '')
        data_origin = data_origin.replace('升降温曲线:', '')
        data_origin = data_origin.replace('复合材料外表面索引:', '')
        data_origin = data_origin.replace('CPU核数:', '')
        # print('After delete:data_origin:')
        with open(file, 'w') as fpw:
            fpw.write(data_origin)
        data_total = data_origin
        F1 = open(file, "r")
        data_total = F1.readlines()

        list_source = []
        for i in range(len(data_total)):
            data_str = data_total[i]  # 每一行split后是一个列表
            list_source.append(data_str)
        for line in F1.readlines():
            line = line.strip('\n')

        # 开始删除空格符号
        list = []
        for i in list_source:
            if i != '\n':
                list.append(i)
        for i in list:
            i.replace('\n', '')
        print('The data of curing has been import to CAE!')

        return list

    # 缠绕工艺
    elif plug_type == 5:
        # 打开该txt文件
        with open(txtname, 'r') as f:
            data_origin = f.read()
        #     删除无用汉字文本
        data_origin = data_origin.replace('预紧力:', '')
        data_origin = data_origin.replace('使用说明：每一行的数据分别对应预紧力,纤维铺层厚度，纤维宽度，CPU核数', '')
        data_origin = data_origin.replace('纤维铺层厚度:', '')
        data_origin = data_origin.replace('纤维宽度:', '')
        data_origin = data_origin.replace('CPU核数:', '')
        # print(data_origin)
        with open(file, 'w') as fpw:
            fpw.write(data_origin)
        # data_total = data_origin
        F1 = open(file, "r")
        data_total = F1.readlines()
        list_source = []
        for i in range(len(data_total)):
            # print(data_total[i])
            data_str = data_total[i].strip().split(",")  # 每一行split后是一个列表
            list_source.append(data_str)
        # 开始删除空格符号
        list = []
        for i in list_source:
            if i != '\n':
                # print(i)
                list.append(i)
        F1.close()
        return list
    # F1.close()

    print('The data from {} has been imported to CAE!'.format(txtname))
    # os.remove(file)


def pick_face2index_list(pick):
    '''
    pick:输入用户鼠标点击面后台获取的数据，返回给你一个序列_index_list
    序列里面一串int数字，分别是你选的面的索引号
    :param pick: mdb.[model_name].part[].face[]
    :return:
    '''
    #print('pick is %s', pick)
    _index_list = []
    for i in pick:
        _index_list.append(i.index)
    return _index_list

def index2tie(master,slave=None,pos=None,var=None,
              num_M=None,num_S=None, var_set_face=None):
    '''
    :param master: 主面的索引号，必须是int，必须是整型序列
    :param slave: 从面的索引号，必须是int，必须是整型序列
    :param pos: 主从面的位置容差，float
    :param var: 是否切换主从面，bool
    :param num_M: 主面的编号，在partlist中调取，进行不同的绑定对，面名称的命名
    :param num_S: 从面的编号，在partlist中调取，进行不同的绑定对，面名称的命名
    :var_set_face: S---建立一个set，F，代表建立一个surface,若用户输入两个面，则不需要输入该参数
    若用户输入一个main，则必须输入该参数，指定是在建立 在set还是surface上
    :return:
    1.若用户输入一个面，则返回该面的region，根据自己的需求定义不同的边界条件
    2.若用户输入两个main，则建立tie关系。不返回任何值
    '''
    # print('Index2tie Is Active!!')
    a = mdb.models['Model-1'].rootAssembly
    if slave == None:
        # print('')
        name = part_list[num_M] + '_outface'
        if var_set_face == 'S':
            region_outface = a.Set(faces=FaceIndex2region(master, num_M), name=name)
            # print('CreatRegion_Outface Is Successful!')

            #输出此时建立的region
            return region_outface
        elif var_set_face == 'F':

            region_outface = a.Surface(side1Faces=FaceIndex2region(master, num_M), name=name)
            # print('Region_Outface Is Successful!')
            # print(region_outface)
            return region_outface
    else:
        #print('user input two faces!')
        # 定义绑定对的名称
        name_mid = 'CP_' + part_list[num_M] + '_' + part_list[num_S]

        # 开始提取主从面的sideface
        a = mdb.models['Model-1'].rootAssembly
        side1Faces_M = []  #主面
        for i in range(len(master)):
            side1Faces_M.append(a.instances[instance_list[num_M]].faces[indexlist[i]:indexlist[i] + 1])
        side1Faces_S = []  #从面
        for i in range(len(master)):
            side1Faces_S.append(a.instances[instance_list[num_S]].faces[indexlist[i]:indexlist[i] + 1])
        
        # 分别定义绑定对的两个面
        region_Master_cb = a.Surface(side1Faces=side1Faces_M, name=name_mid + '_M')
        region_Slave_cb = a.Surface(side1Faces=side1Faces_S, name=name_mid + '_S')

        # 定义绑定对的名称
        tie_name_mid = 'Constraint_' + part_list[num_M] + '_' + part_list[num_S]
        mdb.models['Model-1'].Tie(name=tie_name_mid, master=region_Master_cb,
                                  slave=region_Slave_cb, positionToleranceMethod=SPECIFIED,
                                  positionTolerance=pos,
                                  adjust=ON, tieRotations=ON, thickness=ON)

        # 交互绑定对的主从面
        if var == True:
            mdb.models['Model-1'].constraints[tie_name_mid].swapSurfaces()
        print('    %s is successful!!' % tie_name_mid)


def Face2str_indes(face):
    '''
    一、提取用户选取的面 的索引
    二。组成序列后转换为字符串序列
    eg：[2, 3, 15, 18]
    返回的是：'2 3 15 18'
    '''
    current = 0
    # print('Face2str_indes is active,This is %d'%current)
    # print('The face which user picks in GUI is %s', face)

    list = []

    for i in face:
        # print(i.index)
        list.append(i.index)
    str2 = ' '.join([str(x) for x in list])
    # print('Face has been transfer str_index')
    # print(list)
    # print(str2)
    current += 1
    return str2


def bool2str(str):
    if str == True:
        return 'True'
    else:
        return 'False'
#




# 本函数是根据输入的文件内数据，生成可供注册文件调用的自定义常量脚本
def creat_parameter(var_file, property_data_file=None, WCM_state=False):
    '''
    本函数的功能是，输入用户文本的数据，生成一个文本，文本内容为一系列常量，
    供注册.py文件调用，在插件上实时显示当前使用的参数
    :param var_file: 数据开关，当为true时，书写文件数据，反之此时调用GUI类内部的数据
    :param property_data_file: 7个材料的参数，分别为密度、弹性模量，还有网格尺寸，是一个4×7的矩阵
    :return: 生成一个文件，供注册文件使用
    '''
    # *************************************************************************
    #  撰写脚本的文件的抬头标识等
    f = open('parameter_GUI_file.py', 'w')
    f.write('# -* - coding:UTF-8 -*-\n')
    f.write('\n')

    f.write('#Start defining data for interfaces and text\n')
    f.write('class var_data:\n')
    f.write('\n')
    f.write('    def __init__(self):\n')
    if var_file == False:
        print('CURRENT DATA IS GUI!!!')
        f.write("        self.var_data = 'GUI'\n")

    elif var_file == True:
        print('CURRENT DATA IS file!!!')
        f.write("        self.var_data = 'file'\n")

    property_name = ['d', 'e', 'p', 'c', 's', 'ep', 'mesh_size']
    # 根据WCM状态的不同，使用不一样的构件名称和材料名称
    if WCM_state:
        part_name = ['b', 'f', 'h']
        # 默认参数值
        property_data = [
            ['1.23E-006', '0.384', '0.3', '1', '1219', '0.000326', '5'],
            ['0.00785', ' 2e5', '0.3', '1.6578', '512', '1.22E-005', '3'],
            ['1.65E-006', '4000', '0.3', '0.001', '1500', '0.0001263', '5'],
        ]
    else:
        part_name = ['c', 'b', 'f', 'h']
        # 默认参数值
        property_data = [
            ['1e-6', '23500', '0.33', '0.00043', '826', '0.00143', '5'],
            ['1.23E-006', '0.384', '0.3', '1', '1219', '0.000326', '5'],
            ['0.00785', ' 2e5', '0.3', '1.6578', '512', '1.22E-005', '3'],
            ['1.65E-006', '4000', '0.3', '0.001', '1500', '0.0001263', '5'],
        ]

    # 开始书写GUI参数的默认值
    for i in range(len(part_name )):
        for j in range(len(property_name)):
            s = ''.join(['        self.GUI_', part_name[i], '_', property_name[j],
                         ' = ', property_data[i][j] + '\n'])
            f.write(s)
    f.write('\n')

    # 开始书写file参数的默认值
    if var_file:
        # 插入断言函数，提前预判，导入的数据类型是否与本地一致
        assert len(property_name) == len(property_data_file[0]), 'the columns of property_data_file is not  != 7'
        assert len(part_name) == len(property_data_file), 'the rows of property_data_file is not equal 3'
        for i in range(len(part_name)):
            for j in range(len(property_name)):
                s = ''.join(['        self.file_', part_name[i], '_', property_name[j],
                             ' = ', property_data_file[i][j] + '\n'
                             ])
                f.write(s)
        f.write('\n')

    # ~~~~~~~~~~~~~~~~~~~~~
    s = '    @property\n' \
        '    def extract_var(self):\n' \
        '        return self.var_data\n'
    f.write(s)

    # 初始化参数值设定完毕，空一行便于阅读代码,开始写提取GUI参数的方法
    f.write('\n')
    f.write('#Start defining methods for extracting GUI data\n')
    f.write('class Data_GUI(var_data):\n')

    for i in range(len(part_name)):
        for j in range(len(property_name)):
            f.write('    @property\n')

            # 遇到for循环，注意检查维度是否一致
            s = ''.join(['    def ', part_name[i], '_', property_name[j],
                         '(self):\n', '        return self.GUI_',
                         part_name[i], '_', property_name[j] + '\n'
                         ])
            f.write(s)

    # 初始化参数值设定完毕，空一行便于阅读代码,开始抽取写file参数值
    if var_file:
        f.write('\n')
        f.write('#Start defining methods for extracting file data\n')
        f.write('class Data_file(var_data):\n')

        for i in range(len(part_name)):
            for j in range(len(property_name)):
                f.write('    @property\n')
                s = ''.join(['    def ', part_name[i], '_', property_name[j],
                             '(self):\n', '        return self.file_',
                             part_name[i], '_', property_name[j] + '\n'
                             ])
                f.write(s)
    print('CURRENT DATA HAS BEEN CREATED SUCCSFULLY!!')
    # 文件已生成，此时关闭文件
    f.close()

