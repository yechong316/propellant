from caeModules import *
from driverUtils import executeOnCaeStartup
from abaqus import *
from abaqusConstants import *
# 给推进剂添加粘弹性材料属性
mdb.models['Model-1'].materials['propeller'].elastic.setValues(
    temperatureDependency=ON, table=((5143.68, 0.271, 306.0), (4292.0, 0.28, 
    316.0), (3530.0, 0.271, 326.0)))

# 给推进剂添加各向异性方向
p = mdb.models['Model-1'].parts['propeller']
p.DatumCsysByThreePoints(name='Datum csys-1', coordSysType=CYLINDRICAL, 
    origin=(0.0, 0.0, 0.0), point1=(0.0, 1.0, 0.0), point2=(0.0, 0.0, 1.0))
p = mdb.models['Model-1'].parts['propeller']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#ff ]', ), )
region = regionToolset.Region(cells=cells)
orientation = mdb.models['Model-1'].parts['propeller'].datums[6]
mdb.models['Model-1'].parts['propeller'].MaterialOrientation(region=region, 
    orientationType=SYSTEM, axis=AXIS_3, localCsys=orientation, fieldName='', 
    additionalRotationType=ROTATION_NONE, angle=0.0, 
    additionalRotationField='', stackDirection=STACK_3)


# 给推进剂添加各向异性方向
p = mdb.models['Model-1'].parts['shell']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#f ]', ), )
region = regionToolset.Region(cells=cells)
orientation = mdb.models['Model-1'].parts['shell'].datums[6]
mdb.models['Model-1'].parts['shell'].MaterialOrientation(region=region, 
    orientationType=SYSTEM, axis=AXIS_3, localCsys=orientation, fieldName='', 
    additionalRotationType=ROTATION_NONE, angle=0.0, 
    additionalRotationField='', stackDirection=STACK_3)
#: Specified material orientation has been assigned to the selected regions.

#启动插件来完成一些工作
propellent_02_modules._03_platform_thermal.temprature_shock_kernel.temprature_shock_input(
    timePeriod1=1472, intialtemp=297, hermal_zaihe_list=(), Cpu_num=4, 
    var_export=False, var_input=True, 
    inputfile='d:\\Temp\\abaqus_plugins\\propellant\\propellent_04_data\\Thermal_v2019-01-28_13-00-45.txt')

# 打开odb文件,进行后处理
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
#: Job thermal-2019-05-08-15-36-00: Abaqus/Standard completed successfully.
#: Job thermal-2019-05-08-15-36-00 completed successfully.
o3 = session.openOdb(name='d:/Temp/thermal-2019-05-08-15-36-00.odb')

session.Viewport(name='Viewport: 6', origin=(26.875, -90.2638931274414),
                 width=267.40625, height=94.0810241699219)
session.viewports['Viewport: 6'].makeCurrent()

# 将视角切换至应变
session.viewports['Viewport: 2'].odbDisplay.setPrimaryVariable(
    variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT,
                                                                     'Max. Principal'), )
session.viewports['Viewport: 2'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)

# 仅保留bfc,查看其应变
session.viewports['Viewport: 2'].makeCurrent()
leaf = dgo.LeafFromPartInstance(partInstanceName=('FENGTOU-1', 'PROPELLER-1',
                                                  'SHELL-1',))
session.viewports['Viewport: 2'].odbDisplay.displayGroup.remove(leaf=leaf)

#######################################
# 后处理图像进行处理,删去杂物,仅保留图形和数值
#######################################

session.viewports['Viewport: 2'].odbDisplay.commonOptions.setValues(
    visibleEdges=FREE)
session.viewports['Viewport: 2'].viewportAnnotationOptions.setValues(triad=OFF,
                                                                     title=OFF, state=OFF, annotations=OFF, compass=OFF)
session.viewports['Viewport: 2'].viewportAnnotationOptions.setValues(
    legendBox=OFF)
session.viewports['Viewport: 2'].maximize()
session.viewports['Viewport: 2'].viewportAnnotationOptions.setValues(
    legendFont='-*-verdana-medium-r-normal-*-*-160-*-*-p-*-*-*')

#######################################
# 输出当前图片
#######################################

session.printToFile(
    fileName='D:/旧电脑/[2019年5月7日]固体发动机报告/05_result/struct_3_bfc_E',
    format=PNG, canvasObjects=(session.viewports['Viewport: 2'],
                               session.viewports['Viewport: 3'], session.viewports['Viewport: 4'],
                               session.viewports['Viewport: 1']))


def result2PNG(odb_path, png_name,
               result_type='E',png_path=r'D:/旧电脑/[2019年5月7日]固体发动机报告/05_result/',
               ):

    '''
    将结果文件打印到指定路径
    :param odb_path: odb路径
    :param structure: 何种结构类型
    :param loadcase: 工况类型
    :param instance: 何种构件
    :param result_type: 结果类型,S, E
    :param png_path: 图片路径
    :return: 无
    '''
    instance_name = ['SHELL-1', 'BFC-1', 'FENGTOU-1', 'PROPELLANT-1']

    # 打开odb文件,进行后处理
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    #: Job thermal-2019-05-08-15-36-00: Abaqus/Standard completed successfully.
    #: Job thermal-2019-05-08-15-36-00 completed successfully.
    o3 = session.openOdb(name=odb_path)
    
    viewport = 'Viewport: 2'
    session.Viewport(name=viewport, origin=(26.875, -90.2638931274414),
                     width=267.40625, height=94.0810241699219)

    session.viewports[viewport].makeCurrent()
    session.viewports[viewport].maximize()

    # 将视角切换至应变
    session.viewports[viewport].odbDisplay.setPrimaryVariable(
        variableLabel=result_type, outputPosition=INTEGRATION_POINT, refinement=(INVARIANT,
                                                                         'Max. Principal'), )
    session.viewports[viewport].odbDisplay.display.setValues(
        plotState=CONTOURS_ON_DEF)

    # 仅保留bfc,查看其应变
    session.viewports[viewport].makeCurrent()

    for i in instance_name:

        del instance_name[i]

        del_instance = tuple(instance_name)
        leaf = dgo.LeafFromPartInstance(partInstanceName=del_instance)
        session.viewports[viewport].odbDisplay.displayGroup.remove(leaf=leaf)

        #######################################
        # 后处理图像进行处理,删去杂物,仅保留图形和数值
        #######################################

        session.viewports[viewport].odbDisplay.commonOptions.setValues(
            visibleEdges=FREE)
        session.viewports[viewport].viewportAnnotationOptions.setValues(triad=OFF,
                                                                             title=OFF, state=OFF, annotations=OFF,
                                                                             compass=OFF)
        session.viewports[viewport].viewportAnnotationOptions.setValues(
            legendBox=OFF)
        session.viewports[viewport].maximize()
        session.viewports[viewport].viewportAnnotationOptions.setValues(
            legendFont='-*-verdana-medium-r-normal-*-*-160-*-*-p-*-*-*')

        #######################################
        # 输出当前图片
        #######################################

        session.printToFile(
            fileName= png_path + png_name + i,
            format=PNG, canvasObjects=(session.viewports[viewport],))


result2PNG('d:/Temp/thermal-2019-05-08-15-36-00.odb', png_name='structure_3-loadcase_temprature-')


#######################################
# 添加粘弹性材料属性
#######################################



p = mdb.models['Model-1'].parts['shell']
region1=p.sets['Set_shell']
p = mdb.models['Model-1'].parts['shell']
region2=p.sets['Set_shell']
p = mdb.models['Model-1'].parts['shell']
region3=p.sets['Set_shell']
p = mdb.models['Model-1'].parts['shell']
region4=p.sets['Set_shell']
p = mdb.models['Model-1'].parts['shell']
region5=p.sets['Set_shell']
p = mdb.models['Model-1'].parts['shell']
region6=p.sets['Set_shell']
p = mdb.models['Model-1'].parts['shell']
region7=p.sets['Set_shell']
p = mdb.models['Model-1'].parts['shell']
region8=p.sets['Set_shell']
p = mdb.models['Model-1'].parts['shell']
s = p.faces
side1Faces = s.getSequenceFromMask(mask=('[#8 ]', ), )
normalAxisRegion = p.Surface(side1Faces=side1Faces, name='Surf-1')
p = mdb.models['Model-1'].parts['shell']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#400 ]', ), )
primaryAxisRegion = p.Set(edges=edges, name='Set-3')

compositeLayup = mdb.models['Model-1'].parts['shell'].CompositeLayup(
    name='CompositeLayup-1', description='', elementType=CONTINUUM_SHELL,
    symmetric=False)
compositeLayup.Section(preIntegrate=OFF, integrationRule=SIMPSON,
    poissonDefinition=DEFAULT, thicknessModulus=None, temperature=GRADIENT,
    useDensity=OFF)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-1', region=region1,
    material='shell', thicknessType=SPECIFY_THICKNESS, thickness=0.25,
    orientationType=SPECIFY_ORIENT, orientationValue=30.0,
    additionalRotationType=ROTATION_NONE, additionalRotationField='',
    axis=AXIS_3, angle=0.0, numIntPoints=5)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-2', region=region2,
    material='shell', thicknessType=SPECIFY_THICKNESS, thickness=0.25,
    orientationType=SPECIFY_ORIENT, orientationValue=30.0,
    additionalRotationType=ROTATION_NONE, additionalRotationField='',
    axis=AXIS_3, angle=0.0, numIntPoints=5)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-3', region=region3,
    material='shell', thicknessType=SPECIFY_THICKNESS, thickness=0.25,
    orientationType=SPECIFY_ORIENT, orientationValue=30.0,
    additionalRotationType=ROTATION_NONE, additionalRotationField='',
    axis=AXIS_3, angle=0.0, numIntPoints=5)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-4', region=region4,
    material='shell', thicknessType=SPECIFY_THICKNESS, thickness=0.25,
    orientationType=SPECIFY_ORIENT, orientationValue=30.0,
    additionalRotationType=ROTATION_NONE, additionalRotationField='',
    axis=AXIS_3, angle=0.0, numIntPoints=5)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-5', region=region5,
    material='shell', thicknessType=SPECIFY_THICKNESS, thickness=0.25,
    orientationType=SPECIFY_ORIENT, orientationValue=90.0,
    additionalRotationType=ROTATION_NONE, additionalRotationField='',
    axis=AXIS_3, angle=0.0, numIntPoints=5)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-7', region=region6,
    material='shell', thicknessType=SPECIFY_THICKNESS, thickness=0.25,
    orientationType=SPECIFY_ORIENT, orientationValue=90.0,
    additionalRotationType=ROTATION_NONE, additionalRotationField='',
    axis=AXIS_3, angle=0.0, numIntPoints=5)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-8', region=region7,
    material='shell', thicknessType=SPECIFY_THICKNESS, thickness=0.25,
    orientationType=SPECIFY_ORIENT, orientationValue=90.0,
    additionalRotationType=ROTATION_NONE, additionalRotationField='',
    axis=AXIS_3, angle=0.0, numIntPoints=5)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-6', region=region8,
    material='shell', thicknessType=SPECIFY_THICKNESS, thickness=0.25,
    orientationType=SPECIFY_ORIENT, orientationValue=90.0,
    additionalRotationType=ROTATION_NONE, additionalRotationField='',
    axis=AXIS_3, angle=0.0, numIntPoints=5)
compositeLayup.ReferenceOrientation(orientationType=DISCRETE, localCsys=None,
    additionalRotationType=ROTATION_NONE, angle=0.0,
    additionalRotationField='', axis=AXIS_3, stackDirection=STACK_3,
    normalAxisDefinition=SURFACE, normalAxisRegion=normalAxisRegion,
    normalAxisDirection=AXIS_3, flipNormalDirection=False,
    primaryAxisDefinition=EDGE, primaryAxisRegion=primaryAxisRegion,
    primaryAxisDirection=AXIS_1, flipPrimaryDirection=False)

# 切割曲面
p.PartitionCellByDatumPlane(datumPlane=d2[3], cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(width=162.345, height=71.6661,
    viewOffsetX=-0.309295, viewOffsetY=-0.876532)
p = mdb.models['Model-1'].parts['结构1_bfc']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['结构1_bfc']
p.DatumPlaneByPrincipalPlane(principalPlane=XYPLANE, offset=0.0)
p = mdb.models['Model-1'].parts['结构1_bfc']
p.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=0.0)
p = mdb.models['Model-1'].parts['结构1_bfc']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
d1 = p.datums
p.PartitionCellByDatumPlane(datumPlane=d1[3], cells=pickedCells)
p = mdb.models['Model-1'].parts['结构1_bfc']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#3 ]', ), )
d2 = p.datums
p.PartitionCellByDatumPlane(datumPlane=d2[2], cells=pickedCells)