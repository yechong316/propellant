# -*- coding: utf-8 -*-
#!/usr/bin/python3
# propellant 
# Authorn:Jaime Lannister
# Time:2019/3/7-16:39 
'''
本脚本储存Part模块的所有操作
'''
class Part:
    '''
    本类中储存所有ABAQUS关于PART模块中的所有操作
    '''

    def import_part(self, part_name, part_path):
        '''
        输入：文件名，文件路径
        输出：导入该构件
        :param part_name:
        :param part_path:
        :return:
        '''
        assert isinstance(part_path, str), 'Type error! The data of {}_path is {},expected str!'.format(part_name, part_path)

        # 导入构件,默认为sat文件
        acis = mdb.openAcis(part_path, scaleFromFile=OFF)
        mdb.models['Model-1'].PartFromGeometryFile(name=part_name, geometryFile=acis,
        combine=False, dimensionality=THREE_D, type=DEFORMABLE_BODY)

        # 生成实例 + 截面属性赋予
        a = mdb.models['Model-1'].rootAssembly
        p = mdb.models['Model-1'].parts[part_name]

        # 生成实例
        a.Instance(name=part + '-1', part=p, dependent=ON)
        print('{} has been imported to CAE!'.format(part))

    def test(self, name):
        print('hellon, I am {}'.format(name))

class Property:
    '''
    构建材料属性
    '''

    # #######################################
    # 生成材料属性
    # #######################################

    # 各项同行，金属，输入材料名称，材料属性
    def ISOTROPIC(self, mat_name, *mat):
        # 材料属性生成
        
        mat_name1 = mdb.models['Model-1'].Material(name=mat_name)
        
        mat_name1.Density(table=((mat[0],),))
        mat_name1.Elastic(table=((mat[1], mat[2]),))
        mat_name1.Conductivity(table=((mat[3],),))
        mat_name1.SpecificHeat(table=((mat[4],),))
        mat_name1.Expansion(table=((mat[5],),))

        print('    The property of {} has been generated!'.format(part))
    
    # 各项异性，输入材料名称，材料属性---工程常数
    def ENGINEERING_CONSTANTS(self, mat_name,  *args):
        '''
        导入材料参数，组装成tuple，
        :param args: 
        :return: 
        '''
        # 材料属性生成
        mat_name1 = mdb.models['Model-1'].Material(name=mat_name)

        mat_name1.Density(table=((args[0],),))
        mat_name1.Elastic(type=ENGINEERING_CONSTANTS, table=args[1])
        mat_name1.Conductivity(type=ORTHOTROPIC, table=args[2])
        mat_name1.SpecificHeat(table=((args[3],),))
        mat_name1.Expansion(type=ORTHOTROPIC, table=args[4])
        
        print('The property of {} which user inputs has been import to CAE'.format(name))
        
    # 输入材料名称，添加子程序属性
    def USER(self, mat_name):
        mat_name1 = mdb.models['Model-1'].materials[mat_name1]

        mat_name1.Depvar(n=1)
        mat_name1.UserDefinedField()
        mat_name1.HeatGeneration()
    # 在信息栏中输出  ---  复合材料子程序材料属性定义成功!
    print('    {} has been add property of user subroutines!'.format(name))

    # #######################################
    # 给构件赋予材料属性
    # #######################################
    def assign_part(self, mat_name, part_name):
        
        # 生成实例 + 截面属性赋予
        a = mdb.models['Model-1'].rootAssembly
        p = mdb.models['Model-1'].parts[part]

        # 生成截面属性
        mdb.models['Model-1'].HomogeneousSolidSection(name=mat_name + '_section',
                                                      material=mat_name, thickness=None)

        # 获取p实体的所有cells
        c = p.cells
        # pickedCells为所有cells
        pickedCells = c[:]
        # 为该cells创建一个名为Set-composite的集合

        # region为获取名为Set-composite的集合
        region = p.sets['Set-' + part]
        
        # 生成实例 + 截面属性赋予
        a = mdb.models['Model-1'].rootAssembly
        p = mdb.models['Model-1'].parts[part]

        pickedCells = Pick.pick_cell(part_name)
        p.Set(cells=pickedCells, name='Set-' + part)
        p.SectionAssignment(region=region, sectionName=part + '_section', offset=0.0,
                            offsetType=MIDDLE_SURFACE, offsetField='',
                            thicknessAssignment=FROM_SECTION)
        pass
    

class Pick:
    '''
    所有相关set， surface的拾取的功能全部在这里实现
    '''
    def pick_cell(self, cell_name):

        # 生成实例 + 截面属性赋予
        a = mdb.models['Model-1'].rootAssembly
        p = mdb.models['Model-1'].parts[cell_name]

        c = p.cells

        # pickedCells为所有cells
        pickedCells = c[:]

        return pickedCells

    def pick_face(self, pick, instance_model, num):
        '''
        选取面上的集合
        :param instance_name:
        :return:
        '''
        pick_index_list = []
        for i in pick:
            pick_index_list.append(i.index)

        a = mdb.models['Model-1'].rootAssembly
        # 以下代码是提取当前模型的所有instance的名称，并将tank的名称添加到现有instance_list
        instance_total = mdb.models['Model-1'].rootAssembly.instances
        instance_model = [key for key in instance_total.keys()]


        side1Faces = []  #
        for i in pick_index_list:  # pick_index_list = [8, 9, 14, 16]
            side1Faces.append(a.instances[instance_model[num]].faces[i :i + 1])
        return side1Faces  #返回该面的sideface


class Region:

    def region_set(self, side1Faces, instance_name):
        region = a.Set(faces=side1Faces, name='Sur_' + instance_name)

        return region

    def region_surface(self, side1Faces, instance_name):
        region = a.Surface(side1Faces=side1Faces, name='Sur_' + instance_name)

        return region

class Interaction:

    def tie(self, master_region, part_M, slave_region, part_S, positontolerance, var_swap):
        # 分别定义绑定对的两个面
        tie_name_mid = 'Tie_' + part_M + '_' + part_M
        mdb.models['Model-1'].Tie(name=tie_name_mid, master=master_region,
                                  slave=slave_region, positionToleranceMethod=SPECIFIED,
                                  positionTolerance=positontolerance,
                                  adjust=ON, tieRotations=ON, thickness=ON)
        # 交互绑定对的主从面
        if var_swap == True:
            mdb.models['Model-1'].constraints[tie_name_mid].swapSurfaces()
        print('    %s is successfully created!!' % tie_name_mid)




