# coding:utf-8
from abaqus import *
from abaqusConstants import *
import copy
from caeModules import *
from driverUtils import executeOnCaeStartup
import time

def result2PNG(odb_path, png_name,
               result_type='E',png_folder=r'D:/05_result/',
               ):

    '''
    将结果文件打印到指定路径
    :param odb_path: odb路径
    :param structure: 何种结构类型
    :param loadcase: 工况类型
    :param instance: 何种构件
    :param result_type: 结果类型,S, E
    :param png_folder: 图片路径
    :return: 无
    '''
    session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=192.38020324707,
                     height=71.1782455444336)
    session.viewports['Viewport: 1'].makeCurrent()
    session.viewports['Viewport: 1'].maximize()
    executeOnCaeStartup()
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    o1 = session.openOdb(name='d:/Temp/thermal-2019-05-08-15-36-00.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o1)
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF,))
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT,
                                                                         'Max. Principal'), )
    #######################################
    # 后处理图像进行处理,删去杂物,仅保留图形和数值
    #######################################
    session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
        visibleEdges=FREE)
    session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(triad=OFF,
                                                                         title=OFF, state=OFF, annotations=OFF,
                                                                         compass=OFF)
    session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
        legendBox=OFF)
    session.viewports['Viewport: 1'].maximize()
    session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
        legendFont='-*-verdana-medium-r-normal-*-*-160-*-*-p-*-*-*')
    del_instance = [('BFC-1', 'FENGTOU-1', 'PROPELLANT-1'),
                     ('SHELL-1', 'FENGTOU-1', 'PROPELLANT-1'),
                     ('SHELL-1', 'BFC-1', 'PROPELLANT-1'),
                     ('SHELL-1', 'BFC-1', 'FENGTOU-1')]
    instance_name = ['S', 'B', 'F', 'H']
    leaf = dgo.LeafFromPartInstance(partInstanceName=('BFC-1', 'FENGTOU-1', 'PROPELLANT-1',))

    session.viewports['Viewport: 1'].odbDisplay.displayGroup.remove(leaf=leaf)
    #######################################
    # 输出当前图片
    #######################################
    png_path = png_folder + png_name + 'S'
    session.printToFile(fileName=png_path,
        format=PNG, canvasObjects=(session.viewports['Viewport: 1'],))
    leaf_1 = dgo.Leaf(leafType=DEFAULT_MODEL)
    session.viewports['Viewport: 1'].odbDisplay.displayGroup.replace(leaf=leaf_1)
    instance_name = ['S', 'B', 'F', 'H']
    leaf = dgo.LeafFromPartInstance(partInstanceName=('SHELL-1', 'FENGTOU-1', 'PROPELLANT-1',))
    session.viewports['Viewport: 1'].odbDisplay.displayGroup.remove(leaf=leaf)
    #######################################
    # 输出当前图片
    #######################################
    png_path = png_folder + png_name + 'B'
    session.printToFile(fileName=png_path,
        format=PNG, canvasObjects=(session.viewports['Viewport: 1'],))
    time.sleep(5)
    leaf_1 = dgo.Leaf(leafType=DEFAULT_MODEL)
    session.viewports['Viewport: 1'].odbDisplay.displayGroup.replace(leaf=leaf_1)
    time.sleep(5)
    instance_name = ['S', 'B', 'F', 'H']
    leaf = dgo.LeafFromPartInstance(partInstanceName=('SHELL-1', 'BFC-1', 'PROPELLANT-1',))
    session.viewports['Viewport: 1'].odbDisplay.displayGroup.remove(leaf=leaf)
    #######################################
    # 输出当前图片
    #######################################
    png_path = png_folder + png_name + 'F'
    session.printToFile(fileName=png_path,
        format=PNG, canvasObjects=(session.viewports['Viewport: 1'],))
    leaf_1 = dgo.Leaf(leafType=DEFAULT_MODEL)
    session.viewports['Viewport: 1'].odbDisplay.displayGroup.replace(leaf=leaf_1)
    instance_name = ['S', 'B', 'F', 'H']
    leaf = dgo.LeafFromPartInstance(partInstanceName=('SHELL-1', 'BFC-1', 'FENGTOU-1',))
    session.viewports['Viewport: 1'].odbDisplay.displayGroup.remove(leaf=leaf)
    #######################################
    # 输出当前图片
    #######################################
    png_path = png_folder + png_name + 'H'
    session.printToFile(fileName=png_path,
        format=PNG, canvasObjects=(session.viewports['Viewport: 1'],))
    leaf_1 = dgo.Leaf(leafType=DEFAULT_MODEL)
    session.viewports['Viewport: 1'].odbDisplay.displayGroup.replace(leaf=leaf_1)


result2PNG('d:/Temp/thermal-2019-05-08-15-36-00.odb', png_name='S_3_T_')
