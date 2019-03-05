#!/usr/bin/env python                 
# -*- coding: utf-8 -*-     
# @File  : test_fun.py
# @Author: YC
# @Date  : 2019/1/26
from abaqus import *
from abaqusConstants import *

def tag(str):
    for i in str:
        print(i.index)
    #print(str)

def fun_sub(num):
    n1 = num +12
    #print(n1)

def fun_main(num,var = False):
    # print(num)
    # print(var)
    if var == True:
        print(num)
    else:
        fun_sub(num)


def Face2coord(str):
    list = []
    for i in str:
        list.append(i.pointOn)
    list_tup = tuple(list)
    print(list_tup)
    return list_tup


# t = (((158.2, 3.924884, -21.724326),), ((158.2, 1.219623, 10.574432),), ((158.2, -3.924882, 21.724325),), ((158.2, -1.735526, -11.006278),))
# f = open('d.txt', 'w')
# f.write(str(t))
# f.close()
# def str2tup(str):
#     tup = tuple(eval(str))
#     return tup

# def readTXT(txtname, plug_type):
#     '''
#     要求用户导入一个文件，然后根据不同的文件类型进行读取
#     plug_type = 1 表示插件1，等于2表示写入插件2，依次类推
#     :param data:
#     :return:
#     '''
#     file = 'test1.txt'
#     if plug_type == 1:
#         print('readTXT is successful starting')
#         # 打开该txt文件
#         with open(txtname, 'r',encoding='UTF-8') as fpr:
#             content = fpr.read()
#         #     删除无用汉字文本
#         content = content.replace('复合材料壳体:', '')
#         content = content.replace('使用说明：每一行的数据分别为该构件的密度、弹性模量、泊松比、热传导系数、比热容系数、热膨胀系数和网格尺寸', '')
#         content = content.replace('包覆层:', '')
#         content = content.replace('封头:', '')
#         content = content.replace('推进剂:', '')
#         with open(file, 'w') as fpw:
#             fpw.write(content)
#         List_row = content
#         F1 = open(file, "r")
#         List_row = F1.readlines()
#         list_source = []
#         for i in range(len(List_row)):
#             column_list = List_row[i].strip().split(",")  # 每一行split后是一个列表
#             list_source.append(column_list)
#         print(
#             b'\xd2\xd1\xb3\xc9\xb9\xa6\xb6\xc1\xc8\xa1\xb2\xce\xca\xfd:'
#         )
#         print(list_source)
#         return list_source
#     elif plug_type == 2:
#         print('readTXT is successful starting')
#         # 打开该txt文件
#         with open(txtname, 'r',encoding='UTF-8') as fpr:
#             content = fpr.read()
#         #     删除无用汉字文本
#         content = content.replace('推进剂VS封头:', '')
#         content = content.replace('使用说明：每一行的数据分别为该构件的主面坐标、从面坐标、位置容差、是否切换主从面','')
#         content = content.replace('复合材料VS包覆层:', '')
#         content = content.replace('包覆层VS封头:', '')
#         content = content.replace('包覆层VS推进剂:', '')
#         with open(file, 'w') as fpw:
#             fpw.write(content)
#         List_row = content
#         F1 = open(file, "r")
#         List_row = F1.readlines()
#         list_source = []
#         for i in range(len(List_row)):
#             column_list = List_row[i].strip().split("、")  # 每一行split后是一个列表
#             list_source.append(column_list)
#         lsit_final = []
#         for i in range(len(list_source)):
#             # for j in range(len(list_source[i])):
#             if list_source[i] != ['']:
#                 lsit_final.append(list_source[i])
#         tie_list1 = [
#             [[], [], [], []],
#             [[], [], [], []],
#             [[], [], [], []],
#             [[], [], [], []]
#         ]
#         for i in range(len(lsit_final)):
#             for j in range(len(lsit_final[i])):
#                 if lsit_final[i][j] != '':
#                     tie_list1[i][j] = lsit_final[i][j]
#         print('Tie_data has been read!')
#         return tie_list1
#     elif plug_type == 3:
#         print('readTXT is successful starting')
#         # 打开该txt文件
#         with open(txtname, 'r') as fpr:
#             content = fpr.read()
#         #     删除无用汉字文本
#         content = content.replace('温度冲击试验时间:', '')
#         content = content.replace('使用说明：每一行的数据分别对应温度冲击试验时间，构件初始温度，升降温曲线，复合材料外表面坐标，CPU核数', '')
#         content = content.replace('构件初始温度:', '')
#         content = content.replace('升降温曲线:', '')
#         content = content.replace('复合材料外表面坐标:', '')
#         content = content.replace('CPU核数:', '')
#         with open(file, 'w') as fpw:
#             fpw.write(content)
#         List_row = content
#         F1 = open(file, "r")
#         List_row = F1.readlines()
#         list_source = []
#         for i in range(len(List_row)):
#             column_list = List_row[i].strip().split(",")  # 每一行split后是一个列表
#             list_source.append(column_list)
#         print(
#             b'\xd2\xd1\xb3\xc9\xb9\xa6\xb6\xc1\xc8\xa1\xb2\xce\xca\xfd:'
#         )
#         print(list_source)
#         return list_source
#     elif plug_type == 4:
#         print('readTXT is successful starting')
#         # 打开该txt文件
#         with open(txtname, 'r') as fpr:
#             content = fpr.read()
#         #     删除无用汉字文本
#         content = content.replace('固化工艺时间:', '')
#         content = content.replace('使用说明：每一行的数据分别对应固化工艺时间，构件初始温度，升降温曲线，复合材料外表面坐标，CPU核数', '')
#         content = content.replace('构件初始温度:', '')
#         content = content.replace('升降温曲线:', '')
#         content = content.replace('复合材料外表面坐标:', '')
#         content = content.replace('CPU核数:', '')
#         with open(file, 'w') as fpw:
#             fpw.write(content)
#         List_row = content
#         F1 = open(file, "r")
#         List_row = F1.readlines()
#         list_source = []
#         for i in range(len(List_row)):
#             column_list = List_row[i].strip().split(",")  # 每一行split后是一个列表
#             list_source.append(column_list)
#         print(
#             b'\xd2\xd1\xb3\xc9\xb9\xa6\xb6\xc1\xc8\xa1\xb2\xce\xca\xfd:'
#         )
#         print(list_source)
#         return list_source
#     elif plug_type == 5:
#         print('readTXT is successful starting')
#         # 打开该txt文件
#         with open(txtname, 'r') as fpr:
#             content = fpr.read()
#         #     删除无用汉字文本
#         content = content.replace('预紧力:', '')
#         content = content.replace('使用说明：每一行的数据分别对应预紧力,纤维铺层厚度，纤维宽度，CPU核数', '')
#         content = content.replace('纤维铺层厚度:', '')
#         content = content.replace('纤维宽度:', '')
#         content = content.replace('CPU核数:', '')
#         with open(file, 'w') as fpw:
#             fpw.write(content)
#         List_row = content
#         F1 = open(file, "r")
#         List_row = F1.readlines()
#         list_source = []
#         for i in range(len(List_row)):
#             column_list = List_row[i].strip().split(",")  # 每一行split后是一个列表
#             list_source.append(column_list)
#         print(
#             b'\xd2\xd1\xb3\xc9\xb9\xa6\xb6\xc1\xc8\xa1\xb2\xce\xca\xfd:'
#         )
#         print(list_source)
#         return list_source
#     # os.remove(file)
#
# input_data = readTXT("E:\propellant_v2019年1月26日155418\propellent_04_data\Tie_v2019-01-26_21-46-18.txt", 2)
# print(str2tup(input_data[0][0]))