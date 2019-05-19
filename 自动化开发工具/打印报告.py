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
job_name = mdb.jobs.keys()
# report_name =
for i in range(1):
    odb_path = 'd:/Temp/' + job_name[i] + '.odb'
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
    with open(job_name[i]+ '.result', 'a') as f:
        f.write(str(ep_max) + ',')
        f.write(str(ep_mid) + ',')
        f.write(str(ep_min) + ',')
        f.write(str(ep_law) + '\n')
    print('{}结果已输出!'.format(job_name[i]))

