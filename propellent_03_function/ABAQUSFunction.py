# coding:utf-8
from abaqus import *
from abaqusConstants import *
import os


class Part:
    a = mdb.models['Model-1'].rootAssembly

    def __init__(self, name):
        assert type(name) == str, 'the type of {} is not str!'.format(name)
        self.name = name

        print('Current part is {}'.format(self.name))

    def input_part(self, filepath):
        assert os.path.exists(filepath), '{} not exists'.format(filepath)

        acis = mdb.openAcis(filepath, scaleFromFile=OFF)
        mdb.models['Model-1'].PartFromGeometryFile(name=self.name, geometryFile=acis,
                                                   combine=False, dimensionality=THREE_D, type=DEFORMABLE_BODY)
        print('   - {} has been imported to CAE ...'.format(self.name))

    def instance(self):
        a = mdb.models['Model-1'].rootAssembly
        p = mdb.models['Model-1'].parts[self.name]
        a.Instance(name=self.name + '-1', part=p, dependent=ON)

        print('   - {} has been generated instance.'.format(self.name))

    def setStaticEletype(self, ele_region):
        elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD,
                                  kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF,
                                  hourglassControl=DEFAULT, distortionControl=DEFAULT)
        elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
        elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
        elemType = (elemType1, elemType2, elemType3)

        p = mdb.models['Model-1'].parts[self.name]
        p.setElementType(regions=ele_region, elemTypes=elemType)

        print('   - {} has been set Static Eletype.'.format(self.name))

    def setHeatTransferEletype(self, ele_region):
        elemType1 = mesh.ElemType(elemCode=DC3D8, elemLibrary=STANDARD)
        elemType2 = mesh.ElemType(elemCode=DC3D6, elemLibrary=STANDARD)
        elemType3 = mesh.ElemType(elemCode=DC3D4, elemLibrary=STANDARD)
        elemType = (elemType1, elemType2, elemType3)

        p = mdb.models['Model-1'].parts[self.name]
        p.setElementType(regions=ele_region, elemTypes=elemType)

        print('   - {} has been set HeatTransfer Eletype.'.format(self.name))

    def setCoupledTempDisplacementEletype(self, ele_region):
        elemType1 = mesh.ElemType(elemCode=C3D8T, elemLibrary=STANDARD,
                                  secondOrderAccuracy=OFF, distortionControl=DEFAULT)
        elemType2 = mesh.ElemType(elemCode=C3D6T, elemLibrary=STANDARD)
        elemType3 = mesh.ElemType(elemCode=C3D4T, elemLibrary=STANDARD)
        elemType = (elemType1, elemType2, elemType3)

        p = mdb.models['Model-1'].parts[self.name]
        p.setElementType(regions=ele_region, elemTypes=elemType)

        print('   - {} has been set CoupledTempDisplacement Eletype.'.format(self.name))

    def gene_mesh(self, size):
        assert type(size) == float, 'the type of {} is not float!'.format(size)
        assert size > 0, '{} msut been positive number!'.format(size)

        p_cells = mdb.models['Model-1'].parts[self.name].cells[:]
        p.setMeshControls(regions=p_cells, elemShape=HEX, technique=SWEEP,
                          algorithm=ADVANCING_FRONT)
        p.seedPart(size=size, deviationFactor=0.1, minSizeFactor=0.1)
        p.generateMesh()

        print('   - {} has been generated.'.format(self.name))

    def get_set_region(self, index):
        assert type(index) == list, 'the type of {} is not list!'.format(index)

    def get_name(self): return self.name

    def get_instance(self): return self.name + '-1'


class Property:

    def __init__(self, name):
        assert type(name) == str, 'the type of {} is not str!'.format(name)

        # 材料属性生成
        mat_name = mdb.models['Model-1'].Material(name=name)
        self.mat_name = mat_name

    # 开始生成材料属性
    def creat_property(self, property_list):
        assert type(property_list) == list
        assert len(property_list) != 0

        # 生成密度
        self.mat_name.Density(table=((property_list[0],),))

        # 根据材料是否各项异性输入弹性模量
        self.mat_name.Elastic(table=(property_list[1], property_list[2]))

        # 根据材料是否各项异性输入热传导
        self.mat_name.Conductivity(table=property_list[3])

        # 输入比热容
        self.mat_name.SpecificHeat(table=((property_list[4],),))

        # 输入热膨胀
        self.mat_name.Expansion(table=property_list[5])

        print('   - Finish generating {} propertes...'.format(self.mat_name))

    def SetSectionAssignment(self):
        pickedCells = mdb.models['Model-1'].parts[self.mat_name].cells[:]

        p.Set(cells=pickedCells, name='Set_' + self.mat_name)
        region = p.sets['Set_' + self.mat_name]
        p.SectionAssignment(region=region, sectionName=self.mat_name + '-1', offset=0.0,
                            offsetType=MIDDLE_SURFACE, offsetField='',
                            thicknessAssignment=FROM_SECTION)

        print('   - {} has been set Assignment Section.'.format(self.mat_name))


