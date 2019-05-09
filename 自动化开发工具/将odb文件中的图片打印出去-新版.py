# coding:utf-8
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=192.38020324707, 
    height=71.1782455444336)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
o1 = session.openOdb(name='d:/Temp/thermal-2019-05-08-15-36-00.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Max. Principal'), )
leaf = dgo.LeafFromPartInstance(partInstanceName=('FENGTOU-1', 'PROPELLER-1', 
    'SHELL-1', ))
session.viewports['Viewport: 1'].odbDisplay.displayGroup.remove(leaf=leaf)
