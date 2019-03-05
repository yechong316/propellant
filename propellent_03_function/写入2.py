#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 写入2.py
# @Author: YC
# @Date  : 2019/1/25
#coding=utf-8
import os
def write_data():
    lines_old = []
    f = open('main-composite_curing.for', 'r')  # your path!
    for line in f:
        lines_old.append(line)
    # print(lines)
    f.close()
    lines_DISP = []
    f2 = open('DISP_temp.txt', 'r')  # your path!
    for line in f2:
        lines_DISP.append(line)
    f2.close()
    for i in range(len(lines_DISP)):
        lines_old.insert(i + 61, lines_DISP[i] + '\n')  # 第四行插入666并回车
    # print(lines_old)
    s = ''.join(lines_old)
    # print(s)

    f = open('main-composite_curing.for', 'w+')  # 重新写入文件
    f.write(s)
    f.close()
    del lines_old[:]  # 清空列表3

def readTXT(txtname, plug_type=1):
    '''
    要求用户导入一个文件，然后根据不同的文件类型进行读取
    plug_type = 1 表示插件1，等于2表示写入插件2，依次类推
    :param data:
    :return:
    '''
    data_path = os.path.abspath(os.path.join(os.getcwd(), ".")) + '\\' + 'propellent_04_data' + '\\'
    partlist = ['复合材料壳体:', '包覆层:', '封头:', '推进剂:']
    print('readTXT is successful starting')
    # 打开该txt文件
    with open(txtname, 'r') as fpr:
        content = fpr.read()
    #     删除无用汉字文本
    content = content.replace('复合材料壳体:', '')
    content = content.replace('使用说明：每一行的数据分别为该构件的密度、弹性模量、泊松比、热传导系数、比热容系数、热膨胀系数和网格尺寸', '')
    content = content.replace('包覆层:', '')
    content = content.replace('封头:', '')
    content = content.replace('推进剂:', '')
    with open('test1.txt', 'w') as fpw:
        fpw.write(content)
    List_row = content
    F1 = open('test1.txt', "r")
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


readTXT("E:\propellant_v2019年1月26日155418\propellent_04_data\Property_v2019-01-26_18-16-27.txt")
