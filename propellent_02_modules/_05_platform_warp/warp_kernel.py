# -- encoding:utf-8 --                                               
'''                 
本脚本旨在对建立好� ��绕工艺模型后进行处理计算S22，并与理想应力对比
�  �复迭代，使得到较好的值
''' 
from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
from odbAccess import *
import mesh

import os
import datetime
import numpy as np

from propellent_03_function.propellent_03_function import *
from propellent_03_function.ABAQUSFunction import *

job_path = os.getcwd() + '\\'


def warp(F,thickness,width,Cpu_num, var_export=False, var_input=False, inputfile=None ):

    assert F > 0, 'The F must been greater than 0'
    assert thickness > 0, 'The thickness must been greater than 0'
    assert width > 0, 'The width must been greater than 0'
    assert type(Cpu_num) == int, 'The type of number of CPUs must been int.'

    if var_export:

        data_thermal = [F,thickness,width,Cpu_num]
        exportTXT(data_thermal, 5)

    if var_input:

        input_warp_data = Read()
        data_warp = input_warp_data.plug_5(inputfile)

        warp_kernel_input(
            map(float, data_warp[1])[0],
            map(float, data_warp[2])[0],
            map(float, data_warp[3])[0],
            map(int, data_warp[4])[0]
        )
    else:

        warp_kernel_input(F,thickness,width,Cpu_num)



def warp_kernel_input(F,thickness,width,Cpu_num, var_export=False, var_input=False, inputfile=None):

    # 假定初始温度差为200K


    # 理想应力为120MPa
    true_S22 = F / width / thickness
    start_temp = 0

    end_temp_new = -200
    avg_S22 = true_S22 / 10

    # 定义计数器,监控当前迭代轮数，不再容差范围内循环，在就跳出
    count = 0
    while abs(1 - avg_S22 / true_S22) >= 0.05:

        print('This {}th iteration calculation'.format(count + 1))
        count += 1
        # 修改复合材料终止时刻的温度为end_temp

        mdb.models['Model-1'].predefinedFields['Predefined Field-shell'].setValuesInStep(
            stepName='Step-1', magnitudes=(end_temp_new,))
        print('    The current temprature is {}K'.format(end_temp_new))

        # 提交job计算
        time_warp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        Job_name = 'warp-' + time_warp
        Job_new_name = Job_name + '-' + str(count)
        # print(' %d:job name = %s successful' % (count, Job_new_name))
        #     提交计算，并获取结果值
        mdb.Job(name=Job_new_name, model='Model-1', description='', type=ANALYSIS,
                atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
                memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
                explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
                modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
                scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=Cpu_num,
                numGPUs=0)
        # print(' %d:job submit = %s successful' % (count, Job_new_name))
        mdb.jobs[Job_new_name].submit(consistencyChecking=OFF)
        # 等待计算完成后执行后续过程
        mdb.jobs[Job_new_name].waitForCompletion()
        # print('    {} has been calculated successfully!'.format(Job_new_name))

        # 打开odb文件
        odb_name = job_path + Job_new_name + '.odb'
        # print('this is %d times:%s' % (count, odb_name))

        # 打开odb文件
        myodb = openOdb(odb_name)
        # print(' %d:open odb %s successful' % (count, odb_name))
        # 定位到分析步1的最后一帧的数据
        data = myodb.steps['Step-1'].frames[-1].fieldOutputs['S']
        odb = session.odbs[odb_name]
        # 不明,可能是抓取当前odb
        scratchOdb = session.ScratchOdb(odb)

        # 给当前odb建立一个柱坐标系,要求X轴为固体发动机的轴向方向，将当前odb的数据全部按照柱坐标系进行转换
        scratchOdb.rootAssembly.DatumCsysByThreePoints(name='CSYS-1',
                                                       coordSysType=CYLINDRICAL, origin=(0.0, 0.0, 0.0),
                                                       point1=(0.0, 1.0, 0.0),
                                                       point2=(0.0, 0.0, 1.0))
        dtm = session.scratchOdbs[odb_name].rootAssembly.datumCsyses['CSYS-1']
        data_new = data.getTransformedField(datumCsys=dtm)

        # 遍历所有所有单元数据,如果当前数据属于复合材料实体的,那么返回该数据的S22值
        # 并填入列表list中,对其进行求均值计算
        total_node_S11, total_node_S22, total_node_S33 = [], [], []
        for i in range(len(data_new.values)):
            if data_new.values[i].instance.name == 'SHELL-2D-1':

                node_S11 = data_new.values[i].data[0]
                node_S22 = data_new.values[i].data[1]
                node_S33 = data_new.values[i].data[2]
                total_node_S11.append(node_S11)
                total_node_S22.append(node_S22)
                total_node_S33.append(node_S33)
        # 进行求均值计算
        mean_S11 = np.mean(total_node_S11)
        mean_S22 = np.mean(total_node_S22)
        mean_S33 = np.mean(total_node_S33)
        print('ITERATION={}, S11_MEAN={}, S22_MEAN={}, S33_MEAN={}'.format(
            count, mean_S11, mean_S22, mean_S33))
        avg_S = np.max([mean_S11, mean_S22, mean_S33])
        avg_S22 = avg_S
        print('    The S22 of composite is {}'.format(avg_S22))

        # 计算完毕后根据S22求新一轮迭代所需要的终止温度
        end_temp_new = start_temp - (start_temp - end_temp_new) / avg_S22 * true_S22
    print('Finish calcute compostie, please check in {}'.format(odb_name))
