#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 生成他不来序列.py
# @Author: YC
# @Date  : 2019/1/27

# for i in range(4):
#     for j in range(4):
#         print('data_total[%d][%d]'%(i,j))
#     print('\n')

#
# n = [
#     1472,
#      (mdb.models['Model-1'].rootAssembly.instances['composite-1'].faces[2], mdb.models['Model-1'].rootAssembly.instances['composite-1'].faces[3], mdb.models['Model-1'].rootAssembly.instances['composite-1'].faces[15], mdb.models['Model-1'].rootAssembly.instances['composite-1'].faces[18]),
#      ((0, 297), (20, 232), (740, 232), (741, 322), (1460, 322), (1461, 297)),
#      297,
#      4
# ]

def readTXT(txtname, plug_type):
    '''
    要求用户导入一个文件，然后根据不同的文件类型进行读取
    plug_type = 1 表示插件1，等于2表示写入插件2，依次类推
    '''
    file = 'data_temp.txt'
    if plug_type == 1:
        print('readTXT is successful starting')
        # 打开该txt文件
        with open(txtname, 'r',encoding='UTF-8') as fpr:
            content = fpr.read()
        #     删除无用汉字文本
        content = content.replace('复合材料壳体:', '')
        content = content.replace('使用说明：每一行的数据分别为该构件的密度、弹性模量、泊松比、热传导系数、比热容系数、热膨胀系数和网格尺寸', '')
        content = content.replace('包覆层:', '')
        content = content.replace('封头:', '')
        content = content.replace('推进剂:', '')
        with open(file, 'w') as fpw:
            fpw.write(content)
        List_row = content
        F1 = open(file, "r")
        List_row = F1.readlines()
        list_source = []
        for i in range(len(List_row)):
            column_list = List_row[i].strip().split(",")  # 每一行split后是一个列表
            list_source.append(column_list)
        print(
            b'\xd2\xd1\xb3\xc9\xb9\xa6\xb6\xc1\xc8\xa1\xb2\xce\xca\xfd:'
        )
        print(list_source)
        return list_source
    elif plug_type == 2:
        print('readTXT is successful starting')
        # 打开该txt文件
        with open(txtname, 'r') as fpr:
            content = fpr.read()
        #     删除无用汉字文本
        content = content.replace('推进剂VS封头:', '')
        content = content.replace('使用说明：每一行的数据分别为该构件的主面坐标、从面坐标、位置容差、是否切换主从面','')
        content = content.replace('复合材料VS包覆层:', '')
        content = content.replace('包覆层VS封头:', '')
        content = content.replace('包覆层VS推进剂:', '')
        with open(file, 'w') as fpw:
            fpw.write(content)
        List_row = content
        F1 = open(file, "r")
        List_row = F1.readlines()
        list_source = []
        for i in range(len(List_row)):
            column_list = List_row[i].strip().split("、")  # 每一行split后是一个列表
            list_source.append(column_list)
        lsit_final = []
        for i in range(len(list_source)):
            # for j in range(len(list_source[i])):
            if list_source[i] != ['']:
                lsit_final.append(list_source[i])
        tie_list1 = [
            [[], [], [], []],
            [[], [], [], []],
            [[], [], [], []],
            [[], [], [], []]
        ]
        for i in range(len(lsit_final)):
            for j in range(len(lsit_final[i])):
                if lsit_final[i][j] != '':
                    tie_list1[i][j] = lsit_final[i][j]
        print('Tie_data has been read!')
        return tie_list1
        print(tie_list1)
    elif plug_type == 3:
        print('readTXT-functiong is successful starting')
        # 打开该txt文件
        with open(txtname, 'r', encoding='UTf-8') as fpr:
            content = fpr.read()
        #     删除无用汉字文本
        content = content.replace('温度冲击试验时间:', '')
        content = content.replace('使用说明：每一行的数据分别对应温度冲击试验时间，构件初始温度，升降温曲线，复合材料外表面坐标，CPU核数', '')
        content = content.replace('构件初始温度:', '')
        content = content.replace('升降温曲线:', '')
        content = content.replace('复合材料外表面索引:', '')
        content = content.replace('CPU核数:', '')
        print('After delete:content:')
        # print(content)
        with open(file, 'w') as fpw:
            fpw.write(content)
        List_row = content
        F1 = open(file, "r")
        List_row = F1.readlines()
        list_source = []
        for i in range(len(List_row)):
            # print('Current txt_data :')
            # print(List_row[i])
            # print(type(List_row[i]))
            column_list = List_row[i]  # 每一行split后是一个列表
            list_source.append(column_list)
        for line in F1.readlines():
            line = line.strip('\n')
        # list_data = []
        # list_data.append()

        print('End of data_thermal reading!')
        # 开始删除空格符号
        list = []
        for i in list_source:
            if i != '\n':
                list.append(i)
        for i in list:
            i.replace('\n', '')

        return list
    elif plug_type == 4:
        print('readTXT is successful starting')
        # 打开该txt文件
        with open(txtname, 'r') as fpr:
            content = fpr.read()
        #     删除无用汉字文本
        content = content.replace('固化工艺时间:', '')
        content = content.replace('使用说明：每一行的数据分别对应固化工艺时间，构件初始温度，升降温曲线，复合材料外表面坐标，CPU核数', '')
        content = content.replace('构件初始温度:', '')
        content = content.replace('升降温曲线:', '')
        content = content.replace('复合材料外表面坐标:', '')
        content = content.replace('CPU核数:', '')
        with open(file, 'w') as fpw:
            fpw.write(content)
        List_row = content
        F1 = open(file, "r")
        List_row = F1.readlines()
        list_source = []
        for i in range(len(List_row)):
            column_list = List_row[i].strip().split(",")  # 每一行split后是一个列表
            list_source.append(column_list)
        print(
            b'\xd2\xd1\xb3\xc9\xb9\xa6\xb6\xc1\xc8\xa1\xb2\xce\xca\xfd:'
        )
        print(list_source)
        return list_source
    elif plug_type == 5:
        print('readTXT is successful starting')
        # 打开该txt文件
        with open(txtname, 'r') as fpr:
            content = fpr.read()
        #     删除无用汉字文本
        content = content.replace('预紧力:', '')
        content = content.replace('使用说明：每一行的数据分别对应预紧力,纤维铺层厚度，纤维宽度，CPU核数', '')
        content = content.replace('纤维铺层厚度:', '')
        content = content.replace('纤维宽度:', '')
        content = content.replace('CPU核数:', '')
        with open(file, 'w') as fpw:
            fpw.write(content)
        List_row = content
        F1 = open(file, "r")
        List_row = F1.readlines()
        list_source = []
        for i in range(len(List_row)):
            column_list = List_row[i].strip().split(",")  # 每一行split后是一个列表
            list_source.append(column_list)
        print(
            b'\xd2\xd1\xb3\xc9\xb9\xa6\xb6\xc1\xc8\xa1\xb2\xce\xca\xfd:'
        )
        print(list_source)
        return list_source
    os.remove(file)



inputfile = "E:\propellant_v2019年1月26日155418\propellent_04_data\Thermal_v2019-01-27_16-23-57.txt"
input_data_thermal = readTXT(inputfile, 3)
print('input_data_thermal :')
print(input_data_thermal)
print(input_data_thermal[2])
print(type(tuple(eval(input_data_thermal[2]))))
# print(float(input_data_thermal[1]) + 1)
# print(type(float(input_data_thermal[0])))

# f = open(inputfile,'r', encoding='UTF-8')
# for line in f.readlines():
#     line=line.strip('\n')
#     print(line)
