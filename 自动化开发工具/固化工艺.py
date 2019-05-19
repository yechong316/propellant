# coding:utf-8
from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
from odbAccess import *
executeOnCaeStartup()
import datetime
import numpy as np
curing_temp = [20, 30, 40, 50, 60]
amp = ['Curing-20', 'Curing-30', 'Curing-40', 'Curing-50', 'Curing-60']
job_name = 'Struct04-Curing'
# report_name =
for i in range(1, len(amp)):
    step_time = mdb.models['Model-1'].amplitudes[amp[i]].data[-1][0]
    # print('i:{}, step_time:{},amp[i]:{}'.format(i, step_time, amp[i]))
    mdb.models['Model-1'].steps['Step-1'].setValues(timePeriod=step_time,
        maxInc=step_time)
    mdb.models['Model-1'].boundaryConditions['BC-1'].setValues(
        amplitude=amp[i])
    time_warp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    Job_new_name = job_name + '-{}-'.format(curing_temp[i]) + time_warp
    mdb.Job(name=Job_new_name, model='Model-1', description='', type=ANALYSIS,
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
        scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=4,
        numDomains=4, numGPUs=0)
    mdb.jobs[Job_new_name].submit(consistencyChecking=OFF)
    # 等待计算完成后执行后续过程
    mdb.jobs[Job_new_name].waitForCompletion()
    odb_path = 'd:/Temp/' + Job_new_name + '.odb'
    myodb = openOdb(odb_path)
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
    with open(job_name+ '.result', 'a') as f:
        f.write(str(ep_max) + ',')
        f.write(str(ep_mid) + ',')
        f.write(str(ep_min) + ',')
        f.write(str(ep_law) + '\n')
    print('{}结果已输出!'.format(amp[i]))

