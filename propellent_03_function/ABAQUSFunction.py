# coding:utf-8
from abaqus import *
from abaqusConstants import *
import os
# 将字符串索引转变为数字序列
def str_indes2Face(str):
    '''
    一、提取用户选取的面 的索引
    二。组成序列后转换为字符串序列
    eg：'2 3 15 18'
    返回的是：[2, 3, 15, 18]
    '''
    numbers = map(int, str.split(' '))
    # print('str_index has been transfer index')
    return numbers
    '''
    一、提取用户选取的面 的索引
    二。组成序列后转换为字符串序列
    eg：'2 3 15 18'
    返回的是：[2, 3, 15, 18]
    '''
    # print(sys._getframe().f_lineno)
    list = []
    list = str.split(' ')
    numbers = map(int, list)
    for i in numbers:
        list.append(i)
    str2 = ' '.join([str(x) for x in list])
    # print('Face has been transfer str_index')
    # print(list)
    # print(str2)
    return str2

# 将字符串布尔值 ---》 布尔值
def str2bool(str):
    if str == 'True':
        return True
    else:
        return False

class Part:
    a = mdb.models['Model-1'].rootAssembly

    def __init__(self, name):
        assert type(name) == str, 'the type of {} is not str!'.format(name)
        self.name = name

        # print('Current part is {}'.format(self.name))

    def input_part(self, filepath):
        # assert os.path.exists(filepath), '{} not exists'.format(filepath)
        print('filepath IS :', filepath)
        acis = mdb.openAcis(filepath, scaleFromFile=OFF)
        mdb.models['Model-1'].PartFromGeometryFile(name=self.name, geometryFile=acis,
                                                   combine=False, dimensionality=THREE_D, type=DEFORMABLE_BODY)
        print('   - {} BEEN IMPORTED TO CAE ...'.format(self.name))

    def instance(self):
        a = mdb.models['Model-1'].rootAssembly
        p = mdb.models['Model-1'].parts[self.name]
        a.Instance(name=self.name + '-1', part=p, dependent=ON)

        # print('   - {} has been generated instance.'.format(self.name))

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

        assert type(size) == float or type(size) == int, 'the type of {} is not float!'.format(size)
        assert size > 0, '{} msut been positive number!'.format(size)

        p = mdb.models['Model-1'].parts[self.name]
        p_cells = mdb.models['Model-1'].parts[self.name].cells[:]
        p.setMeshControls(regions=p_cells, elemShape=HEX, technique=SWEEP,
                          algorithm=ADVANCING_FRONT)
        p.seedPart(size=size, deviationFactor=0.1, minSizeFactor=0.1)
        p.generateMesh()

        print('MODULE:MESH {} IS DONE!'.format(self.name))

    def get_set_region(self, index):
        assert type(index) == list, 'the type of {} is not list!'.format(index)
        pass

    def get_name(self): return self.name

    def get_instance(self): return self.name + '-1'



class Property:

    def __init__(self, name):
        assert type(name) == str, 'the type of {} is not str!'.format(name)

        # 材料属性生成
        mat_name = mdb.models['Model-1'].Material(name=name)
        self.mat_name = mat_name
        self.name = name

    # 开始生成材料属性
    def creat_property(self, property_list):
        assert type(property_list) == list
        assert len(property_list) != 0

        # 生成密度
        self.mat_name.Density(table=((property_list[0],),))

        # 根据材料是否各项异性输入弹性模量
        self.mat_name.Elastic(table=((property_list[1], property_list[2]), ))

        # 根据材料是否各项异性输入热传导
        self.mat_name.Conductivity(table=((property_list[3], ), ))

        # 输入比热容
        self.mat_name.SpecificHeat(table=((property_list[4],),))

        # 输入热膨胀
        self.mat_name.Expansion(table=((property_list[5], ), ))

        print('   - Finish generating {} propertes...'.format(self.name))

    def SetSectionAssignment(self):

        # 将构件作为一个集进行定义,
        pickedCells = mdb.models['Model-1'].parts[self.name].cells[:]
        p = mdb.models['Model-1'].parts[self.name]
        p.Set(cells=pickedCells, name='Set_' + self.name)
        region = p.sets['Set_' + self.name]

        # 生成截面
        mdb.models['Model-1'].HomogeneousSolidSection(name=self.name + '-1',
                                                      material=self.name, thickness=None)

        # 将截面属性赋予给前文定义的集(abaqus不可以直接给某一个构件赋予材料属性
        # 必须先将构件定义为一个set,然后赋予到set上面
        p.SectionAssignment(region=region, sectionName=self.name + '-1', offset=0.0,
                            offsetType=MIDDLE_SURFACE, offsetField='',
                            thicknessAssignment=FROM_SECTION)

        print('   - {} has been set Assignment Section.'.format(self.name))

class Property_ORT(Property):
    pass

class Read:
    '''
    要求用户导入一个文件，然后根据不同的文件类型进行读取
    plug_type = 1 表示插件1，等于2表示写入插件2，依次类推,返回没有任何换行符号的字符串
    '''

    # 将删去汉字等无用符号的文本存入到一个临时文件中
    def __init__(self):

        with open('data_temp.txt', 'w') as f:
            pass

    def plug_1(self, txtname):
        print(txtname)

        # assert os.path.exists(txtname), '{} not exists'.format(txtname)
        with open(txtname, 'r'
                # , encoding='utf-8'
                  ) as f:
            data_origin = f.read()

        # 导入构件
        # print('READTXT IS SUCCESSFUL STARTING!!!')
        # 打开该txt文件
        data_origin = data_origin.replace('复合材料壳体:', '')
        data_origin = data_origin.replace('使用说明：每一行的数据分别为该构件的密度、弹性模量、泊松比、热传导系数、比热容系数、热膨胀系数和网格尺寸', '')
        data_origin = data_origin.replace('包覆层:', '')
        data_origin = data_origin.replace('封头:', '')
        data_origin = data_origin.replace('推进剂:', '')

        # assert os._exists(file) == True
        with open(file, 'w') as fpw:
            fpw.write(data_origin)
        with open(file, "r") as F1:
            data_total = F1.readlines()
            data = []
            for i in range(1, len(data_total)):
                data_None_str = data_total[i].strip().split("、")  # 每一行split后是一个列表
                data_str = filter(None, data_None_str)
                data.append(list(map(float, data_str)))

            self.data = data
            # return self.data

    def mat(self):
        return [i[:5] for i in self.data]

    def mesh_size(self):
        return [i[6] for i in self.data]

    def plug_2(self, txtname):

        with open(txtname, 'r') as f:
            data_origin = f.read()

        #     删除无用汉字文本
        data_origin = data_origin.replace('推进剂VS封头:', '')
        data_origin = data_origin.replace('使用说明：每一行的数据分别为该构件的主面坐标、从面坐标、位置容差、是否切换主从面', '')
        data_origin = data_origin.replace('复合材料VS包覆层:', '')
        data_origin = data_origin.replace('包覆层VS封头:', '')
        data_origin = data_origin.replace('包覆层VS推进剂:', '')

        # 将处理后的数据写入到临时文本，然后将存到list_source中
        with open(file, 'w') as fpw:
            fpw.write(data_origin)

        with open(file, "r") as F1:
            data_total = F1.readlines()

        data_tie = []
        for i in range(1, len(data_total)):
            data_None_str = data_total[i].strip().split("、")  # 每一行split后是一个列表
            data_str = filter(None, data_None_str)
            data_tie.append(data_str)

        data = [
            [ str_indes2Face(data_tie[0][0]), str_indes2Face(data_tie[0][1]), float(data_tie[0][2]),
             str2bool(data_tie[0][3])],
            [str_indes2Face(data_tie[1][0]), str_indes2Face(data_tie[1][1]), float(data_tie[1][2]),
             str2bool(data_tie[1][3])],
            [str_indes2Face(data_tie[2][0]), str_indes2Face(data_tie[2][1]), float(data_tie[2][2]),
             str2bool(data_tie[2][3])],
            [str_indes2Face(data_tie[3][0]), str_indes2Face(data_tie[3][1]), float(data_tie[3][2]),
             str2bool(data_tie[3][3])],
        ]

        return data

        # 温度冲击

    def plug_3(self, txtname):
        # print('readTXT-functiong is successful starting')
        #     删除无用汉字文本
        data_origin = data_origin.replace('温度冲击试验时间:', '')
        data_origin = data_origin.replace('使用说明：每一行的数据分别对应温度冲击试验时间，构件初始温度，升降温曲线，复合材料外表面坐标，CPU核数', '')
        data_origin = data_origin.replace('构件初始温度:', '')
        data_origin = data_origin.replace('升降温曲线:', '')
        data_origin = data_origin.replace('复合材料外表面索引:', '')
        data_origin = data_origin.replace('CPU核数:', '')
        # print('After delete:data_origin:')
        # print(data_origin)
        with open(file, 'w') as fpw:
            fpw.write(data_origin)
        data_total = data_origin
        F1 = open(file, "r")
        data_total = F1.readlines()
        list_source = []
        for i in range(len(data_total)):
            data_str = data_total[i]  # 每一行split后是一个列表
            list_source.append(data_str)
        for line in F1.readlines():
            line = line.strip('\n')
        # print('End of data_thermal reading!')
        # 开始删除空格符号
        list = []
        for i in list_source:
            if i != '\n':
                list.append(i)
        for i in list:
            i.replace('\n', '')
        print('Finish gain the thermal data from txt!')
        return list

        # 固化工艺

    def plug_4(self, txtname):
        # print('readTXT is successful starting')
        #     删除无用汉字文本
        data_origin = data_origin.replace('固化工艺时间:', '')
        data_origin = data_origin.replace('使用说明：每一行的数据分别对应固化工艺时间，构件初始温度，升降温曲线，复合材料外表面坐标，CPU核数', '')
        data_origin = data_origin.replace('构件初始温度:', '')
        data_origin = data_origin.replace('升降温曲线:', '')
        data_origin = data_origin.replace('复合材料外表面索引:', '')
        data_origin = data_origin.replace('CPU核数:', '')
        # print('After delete:data_origin:')
        with open(file, 'w') as fpw:
            fpw.write(data_origin)
        data_total = data_origin
        F1 = open(file, "r")
        data_total = F1.readlines()
        list_source = []
        for i in range(len(data_total)):
            data_str = data_total[i]  # 每一行split后是一个列表
            list_source.append(data_str)
        for line in F1.readlines():
            line = line.strip('\n')
        # 开始删除空格符号
        list = []
        for i in list_source:
            if i != '\n':
                list.append(i)
        for i in list:
            i.replace('\n', '')
        print('The data of curing has been import to CAE!')
        return list

        # 缠绕工艺

    def plug_5(self, txtname):
        # 打开该txt文件
        #     删除无用汉字文本
        data_origin = data_origin.replace('预紧力:', '')
        data_origin = data_origin.replace('使用说明：每一行的数据分别对应预紧力,纤维铺层厚度，纤维宽度，CPU核数', '')
        data_origin = data_origin.replace('纤维铺层厚度:', '')
        data_origin = data_origin.replace('纤维宽度:', '')
        data_origin = data_origin.replace('CPU核数:', '')
        # print(data_origin)
        with open(file, 'w') as fpw:
            fpw.write(data_origin)
        # data_total = data_origin
        F1 = open(file, "r")
        data_total = F1.readlines()
        list_source = []
        for i in range(len(data_total)):
            # print(data_total[i])
            data_str = data_total[i].strip().split(",")  # 每一行split后是一个列表
            list_source.append(data_str)
        # 开始删除空格符号
        list = []
        for i in list_source:
            if i != '\n':
                # print(i)
                list.append(i)
        F1.close()
        return list
        # F1.close()

        print('The data from {} has been imported to CAE!'.format(txtname))
        os.remove(file)


class Tie:

    def creat_surface(self, name, index, surface_type):
        '''

        :param name: 主面的instance的索引号
        :param index: 主面的索引号，必须是int，必须是整型序列
        :return:
        '''
        side1Faces = [a.instances[name + '-1'].faces[index[i]:index[i] + 1] for i in range(len(index))]  # 主面
        region_Surface = a.Surface(side1Faces=side1Faces, name=name + '_' + surface_type)
        self.surface_name = name + '_' + surface_type

        return region_Surface

    def creat_tie(self, tie_name, region_Master_cb, region_Slave_cb, pos, var):
        # 定义绑定对的名称
        mdb.models['Model-1'].Tie(name=tie_name, master=region_Master_cb,
                                  slave=region_Slave_cb, positionToleranceMethod=SPECIFIED,
                                  positionTolerance=pos,
                                  adjust=ON, tieRotations=ON, thickness=ON)

        # 交互绑定对的主从面
        if var == True:
            mdb.models['Model-1'].constraints[tie_name].swapSurfaces()
        print('    %s is successful!!' % tie_name)
