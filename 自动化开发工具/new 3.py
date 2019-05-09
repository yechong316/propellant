from caeModules import *
from driverUtils import executeOnCaeStartup
from abaqus import *
from abaqusConstants import *
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
