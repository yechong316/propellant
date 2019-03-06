# -- encoding:utf-8 --             
from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
from odbAccess import *
import mesh

import datetime
import os

from propellent_03_function.propellent_03_function import *


userfile_path = os.getcwd() + '\\abaqus_plugins\\propellant\\propellent_05_Subfile\\'
job_path = os.getcwd() + '\\'

#os.chdir(job_path)
sys.path.append('E:\\propellant_v0125-1100\\propellent_07_job')

# 开始主函数
def curing_input(timePeriod1=None,intialtemp=None,table_list=None,Composite_outface=None,Cpu_num=None
                , var_export=False, var_input=False, inputfile=None):
    a = mdb.models['Model-1'].rootAssembly
    # print('curing_load is active!')
    if var_export:
        # print('Export data!')
        data_thermal = [timePeriod1,intialtemp,table_list,Composite_outface,Cpu_num]
        # print('current total data is %s'%data_thermal)
        exportTXT(data_thermal, 4)

    if var_input:
        curing_Data = readTXT(inputfile,4)

        # 开始调用副程序
        curing_kernel_input(
            float(curing_Data[0]),
            float(curing_Data[1]),
            tuple(eval(curing_Data[2])),
            str_indes2Face(curing_Data[3]),
            int(curing_Data[4])
        )
    else:
        curing_kernel_input(timePeriod1,intialtemp,table_list,pick_face2index_list(Composite_outface),Cpu_num)


# 开始读取用户输入的参数
def curing_kernel_input(timePeriod1,intialtemp,table_list,Composite_outface_index,Cpu_num
                , var_export=False, var_input=False, inputfile=None):
    # **************************************************
    # 注：Composite_outface_index是索引号，2019年3月5日09:41:37
    # **************************************************
    # 根据升降温曲线生成子程序语句
    file_path = creat_thermal_user_data(table_list)

    # 初始文本位置 # 获取FILM的位置 # 写入FILM的数据，0---代表FILM的位置
    user_init = userfile_path + 'Propellant.for'
    CFILMstart_num = access_taget('CFILMstart', user_init)
    user_file_path = write_data(user_init, CFILMstart_num, file_path[0])

    # 第一次修改后的文本位置，获取DISP的位置# 写入DISP的数据，1---代表DISP的位置
    cDISPstart_num = access_taget('cDISPstart', user_file_path)
    user_file_path = write_data(user_file_path, cDISPstart_num, file_path[1])
    # print('DISP and FILM successfule write .for!')
    print('The data of DISP and FILM have been successfully writed to *.for!')

    # 给4个构件增加初始温度场
    generate_init_temprature(intialtemp)

    # # 给每个构件赋予热传递单元属性
    for i in part_list:
        assign_DC3D8_element(i)

    # 给复合材料添加子程序属性
    mats = mdb.models['Model-1'].materials
    mats_model = [key for key in mats.keys()]
    mats_init = ['bfc', 'fengtou', 'propeller']

    # 将3个构件的材料属性除去，仅仅保留其他属性
    mats_list = []
    for mat in mats_model:
        if mat not in mats_init:
            mats_list.append(mat)

    for m in mats_list:
        creat_user_composite(m)

    # 首先定义分析步信息生成一个热传递耦合分析步固化工艺总时长
    mdb.models['Model-1'].HeatTransferStep(name='Step-1', previous='Initial',
                                           timePeriod=timePeriod1, maxNumInc=10000, initialInc=10.0, minInc=1e-05,
                                           maxInc=timePeriod1, deltmx=1000.0)
    mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=('NT', 'HFL', 'RFL', 'SDV',))

    # *******************复合材料壳体施加外表面载荷
    # 外表面temprature工况
    mdb.models['Model-1'].TemperatureBC(name='BC-thermal', createStepName='Step-1',
                                        region=index2tie(master=Composite_outface_index, num_M=0,var_set_face='S'),
                                        fixed=OFF, distributionType=UNIFORM,
                                        fieldName='', magnitude=1.0, amplitude='thermal_Amp')
    # 
    # 热对流工况
    mdb.models['Model-1'].FilmCondition(name='Int-1', createStepName='Step-1',
         surface=index2tie(master=Composite_outface_index, num_M=0,var_set_face= 'F'),
         definition=USER_SUB, filmCoeff=1.0, sinkTemperature=1.0,
         sinkDistributionType=UNIFORM, sinkFieldName='')

    # 提交计算，注意要选择子程序
    time_heat = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    Job_name = 'curing_' + time_heat + '_heat'
    creat_job(Job_name, Cpu_num)
    # 在信息栏输出  ---  开始求解温度场，写出inp文件
    print('Beginning heat thensfer analysis!')
    mdb.jobs[Job_name].writeInput(consistencyChecking=OFF)

    # 开始修改inp文件
    inp_name = job_path + Job_name + '.inp'
    # modefiled_inp的序列里面的依次为job名称,和新的inp文件路径
    # print(inp_name)
    f = open(inp_name, "r")
    for num, value in enumerate(f):
        if value == '*Initial Conditions, type=TEMPERATURE\n':
            target_num = num
    lines = []
    f.close()

    f = open(inp_name, 'r')  # your path!
    for line in f:
        lines.append(line)
    f.close()
    lines.insert(target_num, "*INITIAL CONDITIONS, TYPE=FIELD, VARIABLE=1\n")

    # 把字符串沾起来
    s = ''.join(lines)
    new_inp_filepath = job_path + 'curing_' + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.inp'
    f = open(new_inp_filepath, 'w+')  # 重新写入文件
    f.write(s)
    f.close()
    # 在信息栏中输出  ---  插入关键词成功
    print('%s.inp is inserted successful!' % inp_name)

    # 直接提交刚刚修改完毕的inp文件，调用子程序文件
    Job_new_name = 'curing_' + datetime.datetime.now().strftime('%H-%M-%S')
    mdb.JobFromInputFile(name=Job_new_name, inputFileName=new_inp_filepath,
                         type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None,
                         memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
                         explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE,
                         userSubroutine=user_file_path, scratch='', resultsFormat=ODB,
                         parallelizationMethodExplicit=DOMAIN,
                         numDomains=1, activateLoadBalancing=False, multiprocessingMode=DEFAULT, numCpus=Cpu_num)
    # 在信息栏中输出  ---  新的inp文件为：new_inp_filepath
    print('new_inp :%s' % new_inp_filepath)
    mdb.jobs[Job_new_name].submit(consistencyChecking=OFF)
    mdb.jobs[Job_new_name].waitForCompletion()

    # 计算完毕后，读取当前odb的最后增量步的数字
    # print(Job_new_name)
    odb_name = job_path + Job_new_name + '.odb'
    myodb = openOdb(odb_name)
    end_increment = len(myodb.steps['Step-1'].frames) - 1
    myodb.close()
    # 在信息栏输出  ---  增量步数量已成功获取
    print('FINAL INCREMENT HAS BEEN ACCESS!')

    # 复制上述模型，建立静态通用分析步
    mdb.Model(name='Model-static', objectToCopy=mdb.models['Model-1'])
    print('Model-static has been copy from Model-1!')
    mdb.models['Model-static'].StaticStep(name='Step-1', previous='Initial',
                                          timePeriod=1, maxNumInc=1000, initialInc=0.01,
                                          minInc=1e-5, maxInc=1)
    mdb.models['Model-static'].fieldOutputRequests['F-Output-1'].setValues(variables=('S', 'E', 'U', 'NT'))

    # 给每个构件赋予静态通用单元属性
    for i in part_list:
        creat_C3D8R_element(i)

    mdb.models['Model-static'].Temperature(name='Predefined Field-total',
                                           createStepName='Initial', distributionType=FROM_FILE,
                                           fileName=odb_name, beginStep=1, beginIncrement=1,
                                           endStep=None, endIncrement=None, interpolate=OFF,
                                           absoluteExteriorTolerance=0.0, exteriorTolerance=0.05)

    mdb.models['Model-static'].predefinedFields['Predefined Field-total'].setValuesInStep(
        stepName='Step-1', endStep=1, endIncrement=end_increment)

    # 在信息栏输出  ---  开始静力分析
    print('Beginning General Static analysis!')
    Job_name_static = 'curing_' + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '_static'
    mdb.Job(name=Job_name_static, model='Model-static', description='', type=ANALYSIS,
            atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
            memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
            explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
            modelPrint=OFF, contactPrint=OFF, historyPrint=OFF,
            userSubroutine='', scratch='',
            resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=Cpu_num, numGPUs=0)
    mdb.jobs[Job_name_static].submit(consistencyChecking=OFF)

    # 在信息栏中输出  ---  请查看计算结果文件
    print('Please look at:%s.odb' % Job_name_static)