# coding:utf-8
from abaqus import * 
from abaqusConstants import *
import mesh

import os
import sys
import datetime

from propellent_03_function.propellent_03_function import *
# from propellent_03_function.propellant_output_pick import *
# from propellent_03_function.propellant_input_tie import *



'''
本插件应用于温度冲击试验，当完成构件导入，tie绑定关系建立后，使用此插件进行温度冲击
相关仿真流程的定义，程序实现方法：首先判断是否导出数据，之后是否导入数据
'''
# old_job_path = os.path.abspath(os.path.join(os.getcwd(), "")) + '\\abaqus_plugins\\propellant\\propellent_07_job\\'
# os.chdir(old_job_path)

sys.path.append('E:\\propellant_v0125-1100\\propellent_07_job')
# print('i am in thermal_kernel.py,job path : %s'%new_job_path)
#
##############
# 以下代码是提取当前模型的所有instance的名称，并将tank的名称添加到现有instance_list
instance_list = ['unknown', 'bfc-1', 'fengtou-1', 'propeller-1']
instance_total = mdb.models['Model-1'].rootAssembly.instances
instance_model = [key for key in instance_total.keys()]
for instance, num in zip(instance_model, range(len(part_list))):
    if instance != 'bfc-1' and instance != 'fengtou-1' and instance != 'propeller-1':
        instance_list[0] = instance_model[num]


#开始主函数
def temprature_shock_input(timePeriod1=None,intialtemp=None, hermal_zaihe_list=None,Composite_outface=None,Cpu_num=None, var_export=False, var_input=False, inputfile=None
           ):

    # print('THERMAL CONTACK CODES IS STARTING!')
    if var_export:
        # print('Export data!')
        # print(sys._getframe().f_lineno)
        data_thermal = [timePeriod1,intialtemp, hermal_zaihe_list,Composite_outface,Cpu_num]
        #print('CURRENT TOTAL DATA IS: %s'%data_thermal)
        exportTXT(data_thermal, 3)

    # g根据数据类型进行调用
    if var_input:
        input_data_thermal = readTXT(inputfile, 3)
        # print('INPUT_DATA_THERMAL :')
        # print(input_data_thermal)
        Thermal_kernel_input(
            float(input_data_thermal[0]),
            float(input_data_thermal[1]),
            tuple(eval(input_data_thermal[2])),
            str_indes2Face(input_data_thermal[3]),
            int(input_data_thermal[4]),
        )
    else:
        Thermal_kernel_input(
            timePeriod1, intialtemp, hermal_zaihe_list, pick_face2index_list(Composite_outface), Cpu_num
        )


def Thermal_kernel_input(timePeriod1, intialtemp, hermal_zaihe_list, Composite_outface, Cpu_num,
                         var_export=False):
    '''
    ABAQUS后台执行的命令核心脚本，本质上，上面的函数只是一个判断函数，这个才是核心
    '''
    # 检查升降温曲线合法性，如果有负数，则退出程序
    # print('thermal list is %s', hermal_zaihe_list)
    for i in range(len(hermal_zaihe_list[0])):
        # print(sys._getframe().f_lineno)
        for j in [0, 1]:
            # print(hermal_zaihe_list[i][j])
            if hermal_zaihe_list[i][j] < 0:
                print(
                    b'\xc9\xfd\xbd\xb5\xce\xc2\xc7\xfa\xcf\xdf\xc0\xeb\xc9\xa2\xca\xfd\xbe\xdd\xb5\xe3\xd6\xd0\xb2\xbb\xbf\xc9\xd2\xd4\xb4\xe6\xd4\xda\xb8\xba\xca\xfd!'
                )
                exit()

    print('Beginning analysis FEA of temprature shock of propellant!')
    # 定义分析步参数和场变量值
    mdb.models['Model-1'].CoupledTempDisplacementStep(name='Step-1',
                                                      previous='Initial', timePeriod=timePeriod1, maxNumInc=1000,
                                                      initialInc=1,
                                                      minInc=1e-5, maxInc=timePeriod1 / 10, deltmx=100)
    mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=('S', 'E', 'LE', 'U', 'NT'))

    # 定义最外表面温度冲击载荷幅值曲线，和边界条件
    mdb.models['Model-1'].TabularAmplitude(name='thermal_Amp', timeSpan=STEP,
                                           smooth=SOLVER_DEFAULT, data=hermal_zaihe_list)

    mdb.models['Model-1'].TemperatureBC(name='BC-thermal', createStepName='Step-1',
                                        region=index2tie(master=Composite_outface, num_M=0,var_set_face='S'),
                                        fixed=OFF, distributionType=UNIFORM,
                                        fieldName='', magnitude=1.0, amplitude='thermal_Amp')

    # 搜索当前模型的所有实体，建立初始温度场
    generate_init_temprature(intialtemp)
    
    for i in part_list:
        # 给每个构件赋予热传递单元属性
        creat_thermal_force_element(i)

    # 05-提交计算查看结果
    Job_name = 'thermal-' + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    mdb.Job(name=Job_name, model='Model-1', description='', type=ANALYSIS,
            atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
            memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
            explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
            modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
            scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=Cpu_num,
            numDomains=4, numGPUs=0)
    mdb.jobs[Job_name].submit(consistencyChecking=OFF)