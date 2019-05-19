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
jobs = mdb.jobs.keys()
for i in jobs:
    odb_path = 'd:/Temp/' + i + '.odb'
    myodb = openOdb(odb_path)
    data = myodb.steps['Step-1'].frames[-1].fieldOutputs['E']
    E_max, E_mid, E_min = [], [], []
    for i in range(len(data.values)):
        if data.values[i].instance.name == 'PROPELLER-1':
            E_max.append(data.values[i].maxPrincipal)
            E_mid.append(data.values[i].midPrincipal)
            E_min.append(data.values[i].minPrincipal)
    ep_max, ep_mid, ep_min = max(E_max), max(E_mid), max(E_min)
    ep_safe = 0.05
    ep_law = 0.707 * np.power(np.sum(np.square(ep_max), np.square(ep_mid), np.square(ep_min)), 0.5)
    with open('Struct03-Curing.dat', 'a') as f:
        f.write(str(ep_max) + ',')
        f.write(str(ep_mid) + ',')
        f.write(str(ep_min) + ',')
        f.write(str(ep_law) + '\n')
    # odb = session.odbs[odb_path]
    # session.viewports['Viewport: 1'].setValues(displayedObject=odb)
    # session.viewports['Viewport: 1'].view.setValues(nearPlane=308.512,
    #     farPlane=591.945, width=298.268, height=111.486, cameraPosition=(-186.397,
    #     234.575, 262.601), cameraUpVector=(-0.238164, 0.132867, -0.962094))
    # leaf = dgo.LeafFromPartInstance(partInstanceName=('BFC-1', 'FENGTOU-1',
    #     'SHELL-2D-1', ))
    # session.viewports['Viewport: 1'].odbDisplay.displayGroup.remove(leaf=leaf)
    # odb = session.odbs[odb_path]
    # session.writeFieldReport(fileName='Struct03-Curing-{}.txt'.format(curing_temp[i]), append=ON,
    #     sortItem='Element Label', odb=odb, step=0, frame=fram,
    #     outputPosition=INTEGRATION_POINT, variable=(('E', INTEGRATION_POINT, ((
    #     INVARIANT, 'Max. Principal'), (INVARIANT, 'Mid. Principal'), (INVARIANT,
    #     'Min. Principal'), )), ))

