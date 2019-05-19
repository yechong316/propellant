from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
from odbAccess import *
executeOnCaeStartup()


def Print_png(job_name, png_name):
    # session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    #     referenceRepresentation=ON)
    session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=208.729156494141,
                     height=116.98380279541)
    session.viewports['Viewport: 1'].makeCurrent()
    session.viewports['Viewport: 1'].maximize()
    # -*- coding: mbcs -*-
    #
    # Abaqus/CAE Release 6.14-4 replay file
    # Internal Version: 2015_06_12-04.41.13 135079
    # Run by yanguowei on Sat May 11 20:51:08 2019
    #
    # from driverUtils import executeOnCaeGraphicsStartup
    # executeOnCaeGraphicsStartup()
    #: Executing "onCaeGraphicsStartup()" in the site directory ...
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    o1 = session.openOdb(name='d:/Temp/' + job_name + '.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o1)
    #: Model: d:/Temp/Struct01-Curing-30.odb
    #: Number of Assemblies:         1
    #: Number of Assembly instances: 0
    #: Number of Part instances:     4
    #: Number of Meshes:             4
    #: Number of Element Sets:       16
    #: Number of Node Sets:          17
    #: Number of Steps:              1
    session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
        visibleEdges=NONE)
    leaf = dgo.LeafFromPartInstance(partInstanceName=('BFC-1', 'FENGTOU-1',
                                                      'SHELL-2D-1',))
    session.viewports['Viewport: 1'].odbDisplay.displayGroup.remove(leaf=leaf)
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT,
                                                                         'Max. In-Plane Principal'), )
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(
        plotState=CONTOURS_ON_DEF)
    #: Warning: The selected Primary Variable is not available in the current frame for any elements in the current display group.
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT,
                                                                         'Max. Principal'), )
    session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
        legendFont='-*-verdana-medium-r-normal-*-*-120-*-*-p-*-*-*')
    session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
        legendFont='-*-verdana-medium-r-normal-*-*-120-*-*-p-*-*-*')
    session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(triad=OFF,
                                                                         legendBox=OFF, title=OFF, state=OFF,
                                                                         annotations=OFF, compass=OFF)
    session.viewports['Viewport: 1'].restore()
    session.viewports['Viewport: 1'].setValues(origin=(0.0, 0.898147583007813),
                                               width=281.739562988281, height=116.085655212402)
    session.viewports['Viewport: 1'].setValues(origin=(0.0, 20.4328765869141),
                                               width=193.72395324707, height=96.5509262084961)
    session.viewports['Viewport: 1'].setValues(origin=(0.0, 19.7592620849609),
                                               width=105.932289123535, height=97.4490737915039)
    session.viewports['Viewport: 1'].setValues(origin=(73.234375,
                                                       13.9212951660156))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=299.091,
                                                    farPlane=612.523, width=209.158, height=182.524,
                                                    viewOffsetX=-10.7205,
                                                    viewOffsetY=-0.961218)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=307.965,
                                                    farPlane=598.584, width=215.364, height=187.94,
                                                    cameraPosition=(243.817,
                                                                    396.378, 166.829),
                                                    cameraUpVector=(-0.98538, 0.0560728, -0.160878),
                                                    cameraTarget=(93.5112, -2.9037, -3.62765), viewOffsetX=-11.0386,
                                                    viewOffsetY=-0.98974)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=309.153,
                                                    farPlane=612.941, width=216.195, height=188.665,
                                                    cameraPosition=(-55.2795,
                                                                    338.133, 272.059),
                                                    cameraUpVector=(-0.782444, -0.505787, -0.363264),
                                                    cameraTarget=(94.102, 1.70998, -2.85566), viewOffsetX=-11.0812,
                                                    viewOffsetY=-0.993557)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=307.983,
                                                    farPlane=614.111, width=215.377, height=187.951,
                                                    viewOffsetX=-41.7409,
                                                    viewOffsetY=0.875723)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=295.564,
                                                    farPlane=638.142, width=206.693, height=180.372,
                                                    cameraPosition=(-201.718,
                                                                    255.12, 248.811),
                                                    cameraUpVector=(-0.50312, -0.783397, -0.364909),
                                                    cameraTarget=(80.7768, -3.68454, -4.7433), viewOffsetX=-40.0578,
                                                    viewOffsetY=0.840411)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=286.781,
                                                    farPlane=610.929, width=200.551, height=175.013,
                                                    cameraPosition=(-134.983,
                                                                    351.99, 149.026),
                                                    cameraUpVector=(-0.576106, -0.586135, -0.569691),
                                                    cameraTarget=(112.884, -2.56031, -5.66374), viewOffsetX=-38.8675,
                                                    viewOffsetY=0.815438)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=296.304,
                                                    farPlane=610.425, width=207.211, height=180.825,
                                                    cameraPosition=(-101.348,
                                                                    352.642, 201.553),
                                                    cameraUpVector=(-0.625583, -0.453811, -0.634587),
                                                    cameraTarget=(114.803, 2.17935, -2.23046), viewOffsetX=-40.1582,
                                                    viewOffsetY=0.842516)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=295.072,
                                                    farPlane=611.657, width=206.35, height=180.073,
                                                    viewOffsetX=-52.0246,
                                                    viewOffsetY=16.4781)
    session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
        legendNumberFormat=FIXED)
    session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
        maxValue=0.00948534, minValue=0.00123981, showMaxLocation=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=280.431,
                                                    farPlane=599.647, width=196.111, height=171.138,
                                                    cameraPosition=(-185.224,
                                                                    334.881, -7.31748),
                                                    cameraUpVector=(-0.423753, -0.797228, -0.429956),
                                                    cameraTarget=(114.759, -13.024, -14.0651), viewOffsetX=-49.4432,
                                                    viewOffsetY=15.6605)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=283.206,
                                                    farPlane=596.872, width=198.051, height=172.831,
                                                    viewOffsetX=-30.2556,
                                                    viewOffsetY=17.102)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=284.21,
                                                    farPlane=583.856, width=198.753, height=173.444,
                                                    cameraPosition=(-91.4508,
                                                                    378.992, 89.4086),
                                                    cameraUpVector=(-0.591956, -0.548107, -0.590903),
                                                    cameraTarget=(117.585, -17.5186, -11.373), viewOffsetX=-30.3629,
                                                    viewOffsetY=17.1627)
    session.printOptions.setValues(vpDecorations=OFF)
    session.printToFile(
        fileName='d:/旧电脑/[2019年5月7日]固体发动机报告/06_计算文件/s1/Curing/' + png_name + '.png',
        format=PNG, canvasObjects=(session.viewports['Viewport: 1'],))
    # session.printToFile(
    #     fileName='d:/旧电脑/[2019年5月7日]固体发动机报告/06_计算文件/s1/Curing/Struct01-Curing-Propellant-30.png',
    #     format=PNG, canvasObjects=(session.viewports['Viewport: 1'],))


def report(odb_name, prt_path):
    myodb = openOdb(odb_path)
    data = myodb.steps['Step-1'].frames
    fram = len(data)
    odb = session.odbs[odb_path]
    session.viewports['Viewport: 1'].setValues(displayedObject=odb)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=308.512,
        farPlane=591.945, width=298.268, height=111.486, cameraPosition=(-186.397,
        234.575, 262.601), cameraUpVector=(-0.238164, 0.132867, -0.962094))
    leaf = dgo.LeafFromPartInstance(partInstanceName=('BFC-1', 'FENGTOU-1',
        'SHELL-2D-1', ))
    session.viewports['Viewport: 1'].odbDisplay.displayGroup.remove(leaf=leaf)
    odb = session.odbs[odb_path]
    session.writeFieldReport(fileName=prt_path, append=ON,
        sortItem='Element Label', odb=odb, step=0, frame=8,
        outputPosition=INTEGRATION_POINT, variable=(('E', INTEGRATION_POINT, ((
        INVARIANT, 'Max. Principal'), (INVARIANT, 'Mid. Principal'), (INVARIANT,
        'Min. Principal'), )), ))

curing_temp = [20, 30, 40, 50, 60]
prt_path = 'Struct02-Curing.rpt'
for i in curing_temp:
    # job_name = 'Struct01-Curing-' + str(i)
    # png_name = 'Struct01-Curing-Propellant-' + str(i)
    odb_path = 'd:/Temp/Struct01-Curing-' + str(i) + '.odb'
    # Print_png(job_name, png_name)
    report(odb_path)






curing_temp = [20, 30, 40, 50, 60]

