# coding:utf-8                                 
                 
from abaqus import *                
from abaqusConstants import *

# 将写好的函数调用起来
from propellent_03_function.propellent_03_function import *

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
    # 当用户勾选此选项，数据导出，
    if var_export:
        data_tie = [
            [Master_cb, Slave_cb, Position_cb, var_cb],
            [Master_bf, Slave_bf, Position_bf, var_bf],
            [Master_bh, Slave_bh, Position_bh, var_bh],
            [Master_hf, Slave_hf, Position_hf, var_hf]
        ]

        # 开始导出数据
        exportTXT(data_tie, 2)

    # 根据var_input的布尔值，绝对采用何种数据来源
    print('Beginning creat tie constraint!')
    if var_input:
        input_data = readTXT(inputfile, 2)
        instance_list = gain_name_of_composte_instance()
        print('instance_list is :{}'.format(instance_list))
        tie_data = construced_tie_data_matrix(instance_list, input_data)
        print('tie_data is :{}'.format(tie_data))
        generate_tie(tie_data)

    else:
        #根据用户输入的数据后台操作
        index2tie(pick_face2index_list(Master_cb), pick_face2index_list(Slave_cb), Position_cb, var_cb, 0, 1),
        index2tie(pick_face2index_list(Master_bf), pick_face2index_list(Slave_bf), Position_bf, var_bf, 1, 2),
        index2tie(pick_face2index_list(Master_bh), pick_face2index_list(Slave_bh), Position_bh, var_bh, 1, 3),
        index2tie(pick_face2index_list(Master_hf), pick_face2index_list(Slave_hf), Position_hf, var_hf, 3, 2)

    print('Finish creat tie constraint!')


