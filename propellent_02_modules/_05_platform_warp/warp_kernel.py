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

from propellent_03_function.propellent_03_function import *
job_path = os.getcwd() + '\\'

def warp(F,thickness,width,Cpu_num, var_export=False, var_input=False, inputfile=None ):
    # print('warp is active!')
    if var_export:
        data_thermal = [F,thickness,width,Cpu_num]
        exportTXT(data_thermal, 5)
    if var_input:
        data_warp = readTXT(inputfile, 5)
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
    start_temp = 500
    end_temp = 300

    # 开始赋予单元属性，赋予初始温度场
    a = mdb.models['Model-1'].rootAssembly

    # 以下代码是提取当前模型的所有part的名称，并将tank的名称添加到现有part_list
    part_list = get_all_part_name()

    num_3 = 0
    # 依次调用4个构件,将提取的cell累加,定义初始温度场中
    for i in range(len(part_list)):

        # 给每个构件赋予热传递单元属性,初始温度场
        part_i = part_list[i]
        initThermal_mesh(part_i, start_temp)
        # del_mat_property(part_i)

    # 依次抽取每个instance，施加初始温度场
    a = mdb.models['Model-1'].rootAssembly
    instance_list = gain_name_of_composte_instance()#保存当前所有的instances，其中第一个是外壳
    for i in instance_list:
        c = a.instances[i].cells
        pickedCells = c[:]
        a.Set(cells=pickedCells, name='Set-init' + i)
        region_load = a.sets['Set-init' + i]

        # 建立构件的初始温度场
        mdb.models['Model-1'].Temperature(name='Predefined Field-' + i + '-load', createStepName='Initial',
                                          region=region_load, distributionType=UNIFORM,
                                          crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, magnitudes=(start_temp,))
        print('   The initial tempreture field has been generated in {}'.format(i))
    # 定义静态通用分析步
    mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial',
                                     timePeriod=1, maxNumInc=1000, initialInc=0.01,
                                     minInc=1e-5, maxInc=0.1)

    # 理想应力为120MPa
    true_S22 = F / width / thickness
    end_temp_new = end_temp
    avg_S22 = true_S22 / 10

    # 定义计数器,监控当前迭代轮数，不再容差范围内循环，在就跳出
    count = 0
    # instance_list = gain_name_of_composte_instance()#保存当前所有的instances，其中第一个是外壳
    while abs(1 - avg_S22 / true_S22) >= 0.05:

        print('This {}th iteration calculation'.format(count + 1))
        count += 1
        # 修改复合材料终止时刻的温度为end_temp
        mdb.models['Model-1'].predefinedFields['Predefined Field-' + instance_list[0] + '-load'].setValuesInStep(
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
        list = []
        for i in range(len(data_new.values)):
            if data_new.values[i].instance.name == instance_list[0].upper():
                composite_S22 = data_new.values[i].data[1]
                list.append(composite_S22)
        # 进行求均值计算
        avg_S22_1 = sum(list) / len(list)
        avg_S22 = avg_S22_1
        print('    The S22 of composite is {}'.format(avg_S22))

        # 计算完毕后根据S22求新一轮迭代所需要的终止温度
        end_temp_new = start_temp - (start_temp - end_temp_new) / avg_S22 * true_S22
    print('Finish calcute compostie, please check in {}'.format(odb_name))
