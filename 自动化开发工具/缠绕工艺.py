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
import numpy as np
import datetime
F = [20,
     # 40,
     # 60,
     # 80,
     # 100
     ]
struct_name = [
    'Struct01'
    # , 'Struct02'
    # , 'Struct03'
    # , 'Struct04'
               ]
width = 4
thickness = 0.25
for k in range(len(struct_name)):
    for i in range(len(F)):
        true_S22 = F[i] / width / thickness
        start_temp = 0
        end_temp_new = -200
        avg_S22 = true_S22 / 10
        # 定义计数器,监控当前迭代轮数，不再容差范围内循环，在就跳出
        count = 1
        now_time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        file_name = struct_name[k] + '-' + F[i] + '-' + now_time + '.warp_log'
        with open(file_name, 'a') as f:
            f.write('*'*50)
            f.write('{}受到{}N时，计算结果如下：'.format(struct_name[k], F[i]))
            f.write('\n')
        while abs(1 - avg_S22 / true_S22) >= 0.05:
            # print('This {}th iteration calculation'.format(count + 1))
    
            # 修改复合材料终止时刻的温度为end_temp
            mdb.models['Model-1'].predefinedFields['Predefined Field-2'].setValuesInStep(
                stepName='Step-1', magnitudes=(end_temp_new,))
            print('    The current temprature is {}K'.format(end_temp_new))
            # 提交job计算
            time_warp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            Job_new_name = '{}-Warp-{}-{}'.format(struct_name[k], F[i], time_warp)
            #     提交计算，并获取结果值
            mdb.Job(name=Job_new_name, model='Model-1', description='', type=ANALYSIS,
                    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
                    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
                    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
                    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
                    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=4,
                    numDomains=4, numGPUs=1)
            # print(' %d:job submit = %s successful' % (count, Job_new_name))
            mdb.jobs[Job_new_name].submit(consistencyChecking=OFF)
            # 等待计算完成后执行后续过程
            mdb.jobs[Job_new_name].waitForCompletion()
            # print('    {} has been calculated successfully!'.format(Job_new_name))
            # 打开odb文件
            odb_name = 'd:/Temp/' + Job_new_name + '.odb'
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
            for _ in range(len(data_new.values)):
                if data_new.values[_].instance.name == 'SHELL-2D-1':
                    node_S11 = data_new.values[_].data[0]
                    node_S22 = data_new.values[_].data[1]
                    node_S33 = data_new.values[_].data[2]
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
            with open(file_name, 'a') as f:
                f.write('Iteration   Temperature_difference   Target_S_mise\n')
                f.write('{}   {}   {}\n'.format(count, start_temp - end_temp_new, avg_S22))
                f.write('\n')
            end_temp_new = start_temp - (start_temp - end_temp_new) / avg_S22 * true_S22
            count += 1
            if count > 3:
                print('F:{}, 迭代次数过多，请检查参数'.format(F[i]))
                break
        odb_name = 'd:/Temp/' + Job_new_name + '.odb'
        # 打开odb文件
        myodb = openOdb(odb_name)
        data = myodb.steps['Step-1'].frames[-1].fieldOutputs['E']
        E_max, E_mid, E_min = [], [], []
        for j in range(len(data.values)):
            if data.values[j].instance.name == 'PROPELLER-1':
                E_max.append(data.values[j].maxPrincipal)
                E_mid.append(data.values[j].midPrincipal)
                E_min.append(data.values[j].minPrincipal)
        ep_max, ep_mid, ep_min = max(E_max), max(E_mid), max(E_min)
        ep_safe = 0.05
        ep_law = 0.707 * np.power(np.sum(np.square(ep_max), np.square(ep_mid), np.square(ep_min)), 0.5)
        report_name = '{}-Warp.result'.format(struct_name[k])
        with open(report_name, 'a') as f:
            f.write(str(ep_max) + ',')
            f.write(str(ep_mid) + ',')
            f.write(str(ep_min) + ',')
            f.write(str(ep_law) + '\n')
            # print('{}结果已输出!'.format(amp[i]))
        # print('Finish calcute compostie, please check in {}'.format(odb_name))