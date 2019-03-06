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

        # ############################################################
        # 本部分功能总结：
        # 1. 读取文件数据（已转化abaqus可以识别的格式）
        # 2.获取当前模型复合材料的实体名称
        # 3.分别寻找主从面的sideface
        # 4.建立绑定关系
        # 5.开始重复4组tie对
        # ############################################################

        # 复合材料 -包覆层
        # 1. 读取文件数据（已转化abaqus可以识别的格式）----
        input_data = readTXT(inputfile, 2)
        index_M,  index_S= input_data[0][0], input_data[0][1]

        # 2.获取当前模型复合材料的实体名称
        instance_list = gain_name_of_composte_instance()
        ins_M, ins_S = instance_list[0], instance_list[1]
        tie_name = 'CP_ ' + ins_M + '_' + ins_S

        # 3.分别寻找主从面的sideface
        sideface_M = generate_instance_sideface(ins_M, index_M)
        sideface_S = generate_instance_sideface(ins_S, index_S)

        #4.建立绑定关系
        generate_tie(tie_name, sideface_M, sideface_S)

        # 包覆层 - 封头
        # 1. 读取文件数据（已转化abaqus可以识别的格式）----
        index_M, index_S = input_data[1][0], input_data[1][1]

        # 2.获取当前模型复合材料的实体名称
        ins_M, ins_S = instance_list[1], instance_list[2]
        tie_name = 'CP_ ' + ins_M + '_' + ins_S

        # 3.分别寻找主从面的sideface
        sideface_M = generate_instance_sideface(ins_M, index_M)
        sideface_S = generate_instance_sideface(ins_S, index_S)

        # 4.建立绑定关系
        generate_tie(tie_name, sideface_M, sideface_S)

        # 封头 - 推进剂
        # 1. 读取文件数据（已转化abaqus可以识别的格式）----
        index_M, index_S = input_data[2][0], input_data[2][1]

        # 2.获取当前模型复合材料的实体名称
        ins_M, ins_S = instance_list[2], instance_list[3]
        tie_name = 'CP_ ' + ins_M + '_' + ins_S

        # 3.分别寻找主从面的sideface
        sideface_M = generate_instance_sideface(ins_M, index_M)
        sideface_S = generate_instance_sideface(ins_S, index_S)

        # 4.建立绑定关系
        generate_tie(tie_name, sideface_M, sideface_S)

        # 推进剂 - 封头
        # 1. 读取文件数据（已转化abaqus可以识别的格式）----
        index_M, index_S = input_data[3][0], input_data[3][1]

        # 2.获取当前模型复合材料的实体名称
        ins_M, ins_S = instance_list[3], instance_list[2]
        tie_name = 'CP_ ' + ins_M + '_' + ins_S

        # 3.分别寻找主从面的sideface
        sideface_M = generate_instance_sideface(ins_M, index_M)
        sideface_S = generate_instance_sideface(ins_S, index_S)

        # 4.建立绑定关系
        generate_tie(tie_name, sideface_M, sideface_S)


    else:
        #根据用户输入的数据后台操作
        index2tie(pick_face2index_list(Master_cb), pick_face2index_list(Slave_cb), Position_cb, var_cb, 0, 1),
        index2tie(pick_face2index_list(Master_bf), pick_face2index_list(Slave_bf), Position_bf, var_bf, 1, 2),
        index2tie(pick_face2index_list(Master_bh), pick_face2index_list(Slave_bh), Position_bh, var_bh, 1, 3),
        index2tie(pick_face2index_list(Master_hf), pick_face2index_list(Slave_hf), Position_hf, var_hf, 3, 2)

    print('Finish creat tie constraint!')


