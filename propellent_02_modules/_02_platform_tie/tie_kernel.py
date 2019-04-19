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

    tie_pair = [
        ['shell', 'bfc'],
        ['bfc', 'fengtou'],
        ['bfc', 'propeller'],
        ['propeller', 'fengtou']
    ]
    if var_input:

        input_tie_data = Read()
        data_tie = input_tie_data.plug_2(inputfile)

    else:
        data_tie = [
            [pick_face2index_list(Master_cb), pick_face2index_list(Slave_cb), Position_cb, var_cb],
            [pick_face2index_list(Master_bf), pick_face2index_list(Slave_bf), Position_bf, var_bf],
            [pick_face2index_list(Master_bh), pick_face2index_list(Slave_bh), Position_bh, var_bh],
            [pick_face2index_list(Master_hf), pick_face2index_list(Slave_hf), Position_hf, var_hf]
        ]

    # 依次建立绑定关系
    for data, part_name in zip(data_tie, tie_pair):

        tie = Tie()
        region_master = tie.creat_surface(part_name[0], data[0], 'M')
        region_slave = tie.creat_surface(part_name[1], data[1], 'S')
        tie.creat_tie(region_master, region_slave, data[2], data[3])

    if var_export: exportTXT(data_tie, 2)


