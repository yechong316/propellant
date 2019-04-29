# coding:utf-8
from abaqus import * 
from abaqusConstants import *
import mesh

import os
import sys
import datetime

from propellent_03_function.ABAQUSFunction import *
from propellent_03_function.propellent_03_function import *

'''
本插件应用于温度冲击试验，当完成构件导入，tie绑定关系建立后，使用此插件进行温度冲击
相关仿真流程的定义，程序实现方法：首先判断是否导出数据，之后是否导入数据
'''

#
##############
# 以下代码是提取当前模型的所有instance的名称，并将tank的名称添加到现有instance_list
instance_list = ['unknown', 'bfc-1', 'fengtou-1', 'propeller-1']

instance_total = mdb.models['Model-1'].rootAssembly.instances
instance_model = [key for key in instance_total.keys()]
for instance, num in zip(instance_model, range(len(instance_list))):
    if instance != 'bfc-1' and instance != 'fengtou-1' and instance != 'propeller-1':
        instance_list[0] = instance_model[num]


#开始主函数
def temprature_shock_input(timePeriod1=None,intialtemp=None, hermal_zaihe_list=None,
           Composite_outface=None,Cpu_num=None, var_export=False, var_input=False, inputfile=None):

    data_thermal = [timePeriod1, intialtemp, hermal_zaihe_list, Composite_outface, Cpu_num]

    assert timePeriod1 > 0, 'THE TIME MUST BEEN GREATER THAN 0'
    assert intialtemp > 0, 'THE INITIAL TEMPRRATURE MUST BEEN GREATER THAN 0'
    for i in hermal_zaihe_list:
        for j in i:
            assert j > 0, 'The Rise temperature curve do not exit nagetive or zero'
    assert type(Cpu_num) == int, 'The type of number of CPUs must been int.'

    if var_export:

        exportTXT(data_thermal, 3)

    # g根据数据类型进行调用
    if var_input:

        input_thermal_data = Read()
        input_data_thermal = input_thermal_data.plug_3(inputfile)
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


def Thermal_kernel_input(timePeriod1, intialtemp, hermal_zaihe_list, Composite_outface_index, Cpu_num,
                         var_export=False):
    '''
    ABAQUS后台执行的命令核心脚本，本质上，上面的函数只是一个判断函数，这个才是核心
    温度冲击工艺基本没什么可说的，4个实体给初始温度场，外壳的外表面给个温度冲击的曲线，热力耦合分析步提交
    计算就ok
    '''


    # 定义分析步参数和场变量值
    mdb.models['Model-1'].CoupledTempDisplacementStep(name='Step-1',
                                                      previous='Initial', timePeriod=timePeriod1, maxNumInc=1000,
                                                      initialInc=1,
                                                      minInc=1e-5, maxInc=timePeriod1 / 10, deltmx=100)
    # exit()
    mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=('S', 'E', 'LE', 'U', 'NT'))
    # exit()
    # 定义最外表面温度冲击载荷幅值曲线，和边界条件
    mdb.models['Model-1'].TabularAmplitude(name='Amp-1', timeSpan=STEP,
                                           smooth=SOLVER_DEFAULT, data=hermal_zaihe_list )
    # mdb.models['Model-1'].TabularAmplitude(name='thermal_Amp', timeSpan=STEP,
    #                                        smooth=SOLVER_DEFAULT, data=hermal_zaihe_list)

    instances = gain_name_of_composte_instance()#保存当前所有的instances，其中第一个是外壳
    shell_name = instances[0] #保存当前所有的instances，其中第一个是外壳
    region_outface = generate_set_region(shell_name, Composite_outface_index)
    # 以上代码全部正常运行
    mdb.models['Model-1'].TemperatureBC(name='BC-thermal', createStepName='Step-1',
                                        region=region_outface,fixed=OFF, distributionType=UNIFORM,
                                        fieldName='', magnitude=1.0, amplitude='Amp-1')
    print('TempratureBC is successfully generated!')

    # 搜索当前模型的所有实体，建立初始温度场
    generate_init_temprature(instances, intialtemp)
    # exit()
    part_list = get_all_part_name()
    for i in part_list:
        # 给每个构件赋予热传递单元属性
        creat_thermal_force_element(i)

    # 05-提交计算查看结果
    # exit()
    Job_name = 'thermal-' + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    mdb.Job(name=Job_name, model='Model-1', description='', type=ANALYSIS,
            atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
            memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
            explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
            modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
            scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=Cpu_num,
            numDomains=4, numGPUs=0)
    mdb.jobs[Job_name].submit(consistencyChecking=OFF)