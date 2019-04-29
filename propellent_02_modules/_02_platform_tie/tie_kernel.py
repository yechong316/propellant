# coding:utf-8                                 
                 
from abaqus import *
from abaqusConstants import *

# 将写好的函数调用起来
from propellent_03_function.propellent_03_function import *
from propellent_03_function.ABAQUSFunction import *

'''
本插件用于当构件导入之后，定义4个构件之间的tie绑定关系
以下4个函数分别为获取4个构件上面的函数
'''
def tie_input(
        # 定义4个tie绑定对，分别为主面，从面，容差
        Master_cb=None,Slave_cb=None,Position_cb=None,var_cb=None,
        Master_bf=None,Slave_bf=None,Position_bf=None,var_bf=None,
        Master_bh=None,Slave_bh=None,Position_bh=None,var_bh=None,
        Master_hf=None,Slave_hf=None,Position_hf=None,var_hf=None,
        var_export=False, var_input=False, inputfile=None
                   ):
    '''
    数据有两种来源方式,1. 界面参数,即上面函数中的参数, 2.文件导入,
    下面的if语句就干这么个事情
    '''
    if var_input:

        input_tie_data = Read()
        data_tie = input_tie_data.plug_2(inputfile)

    else:
        data_tie = [
            # 将鼠标点击到的主从面转换列表
            [pick_face2index_list(Master_cb), pick_face2index_list(Slave_cb), Position_cb, var_cb],
            [pick_face2index_list(Master_bf), pick_face2index_list(Slave_bf), Position_bf, var_bf],
            [pick_face2index_list(Master_bh), pick_face2index_list(Slave_bh), Position_bh, var_bh],
            [pick_face2index_list(Master_hf), pick_face2index_list(Slave_hf), Position_hf, var_hf]
        ]

    # 数据检查，必须要求主从面的索引为int， 容差必须大于等于0， 是否切换主从面为布尔类型
    for data in data_tie:

        for i in data[0]:
            assert type(i) == int, 'INDEX MUST BEEN INT!'
        for i in data[1]:
            assert type(i) == int, 'INDEX MUST BEEN INT!'

        assert data[2] >= 0
        assert type(data[3]) == bool

    '''
    ABAQUS在建立tie关系的时候遵循这样的流程:
    找到主面实体 --> 根据这实体上的索引号读取到Face --> 根据Face生成region_master --> 
    次面实体(循环上述流程)得到region_slave --> 然后根据绑定对的名称+两个主从面的region+容差+是否
    切换主从面,完成定义.
    ================================这是傲娇的分割线===============================
    为实现上述过程,
    1. 首先罗列出4组绑定对的主从面实体,为方便阅读及代码维护,统一用字典索引的方式, 并储存到列表中
    2. 遍历该列表与上文得到的具体参数, 分别建立主面.从面的region,然后建立tie关系
    '''
    tie_1 = {'master_instance':'shell', 'slave_instance':'bfc'}
    tie_2 = {'master_instance':'bfc', 'slave_instance':'fengtou'}
    tie_3 = {'master_instance':'bfc', 'slave_instance':'propeller'}
    tie_4 = {'master_instance':'propeller', 'slave_instance':'fengtou'}
    tie_pair = [tie_1, tie_2, tie_3, tie_4]


    # 依次建立绑定关系
    for data, part_name in zip(data_tie, tie_pair):

        tie = Tie()
        region_master = tie.creat_surface(part_name['master_instance'], data[0], 'M')
        region_slave = tie.creat_surface(part_name['slave_instance'], data[1], 'S')
        tie.creat_tie('Tie_' + part_name['master_instance'] + '_' + part_name['slave_instance'],
                      region_master, region_slave, data[2], data[3])

    if var_export: exportTXT(data_tie, 2)


