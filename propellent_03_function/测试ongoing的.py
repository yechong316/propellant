#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 测试ongoing的.py
# @Author: YC
# @Date  : 2019/1/28
import os
import datetime
# from propellent_03_function.propellent_03_function import *
# from propellent_03_function.propellant_input_tie import *
userfile_path = os.path.abspath(os.path.join(os.getcwd(), "..")) + '\\' + 'propellent_05_Subfile' + '\\'
def access_taget(label,file):

    '''
    2019年1月28日09:48:21 应该也没有问题，别看了
    读取初始子程序文件，根据预先写的标识符号获取当前行号
    :param label: 位置标号， cDISP,cFILM
    :return: 返回数字，int
    '''
    f = open(file, 'r')
    lines = []
    for line in f:
        lines.append(line)
    f.close()
    for i in range(len(lines)):
        if lines[i] == label + '\n':
            return i
# CFILMstart_num = access_taget('CFILMstart')
# cDISPstart_num = access_taget('cDISPstart')
# print(cDISPstart_num)
def creat_thermal_user_data(table_list):
    '''
    2019年1月28日09:48:07  ---本函数没有问题，别看了~~~~
    根据用户输入的升降温曲线，自动生成子程序中需要的语句
    eg：if***
    elseif****
    :param table_list: 用户输入的升降温曲线
    :return: 两个文件的绝对路径,并且组成列表
    '''
    # DISP_temp.txt
    DISPdata_file = userfile_path + 'DISP_temp.txt'
    with open(DISPdata_file, 'w+') as f:
        num = len(table_list)
        count = 0
        s_if = '      IF(TIME(2).LE.' + str(table_list[1][0]) + ')THEN'
        f.write(s_if)
        f.write('\n')
        s_U1 = '          U(1)=' + str(table_list[0][1]) + '+TIME(2)*' + str(
            (table_list[1][1] - table_list[0][1]) / (table_list[1][0] - table_list[0][0]))
        f.write(s_U1)
        f.write('\n')
        for i in range(1, len(table_list) - 1):
            s_elif = '      ELSEIF(TIME(2).LE.' + str(table_list[i + 1][0]) + ')THEN'
            f.write(s_elif)
            f.write('\n')
            s_U1 = '          U(1)=' + str(table_list[i][1]) + '+TIME(2)*' + str(
                (table_list[i + 1][1] - table_list[i][1]) / (table_list[i + 1][0] - table_list[i][0]))
            f.write(s_U1)
            f.write('\n')
    print('%s Is Done!'%DISPdata_file)

    # 开始生成FILM。txt
    FILMdata_file = userfile_path + 'FILM_temp.txt'
    with open(FILMdata_file, 'w') as f:
        s_if = '      IF(TIME(2).LE.' + str(table_list[1][0]) + ')THEN'
        f.write(s_if)
        f.write('\n')
        s_U1 = '          SINK=' + str(table_list[0][1]) + '+TIME(2)*' + str(
            (table_list[1][1] - table_list[0][1]) / (table_list[1][0] - table_list[0][0]))
        f.write(s_U1)
        f.write('\n')
        for i in range(1, len(table_list) - 1):
            s_elif = '      ELSEIF(TIME(2).LE.' + str(table_list[i + 1][0]) + ')THEN'
            f.write(s_elif)
            f.write('\n')
            s_U1 = '          SINK=' + str(table_list[i][1]) + '+TIME(2)*' + str(
                (table_list[i + 1][1] - table_list[i][1]) / (table_list[i + 1][0] - table_list[i][0]))
            f.write(s_U1)
            f.write('\n')
    print('%s Is Done!'%FILMdata_file)
    DISP_FILM_file = []
    DISP_FILM_file.append(FILMdata_file)
    DISP_FILM_file.append(DISPdata_file)
    return DISP_FILM_file



def write_data(insert_user_name,num,insert_data_file):
    '''
    本函数的功能在于：可以insert_data_file将插入到insert_user_name的行号num前面，然后返回新的文本路径
    :param num: 用户必须两个两个的传入参数，第一个是行号，第二个是插入的文本绝对路径
    :param insert_data_file: 用户需要写入的子程序文本
    :return: 本函数注意是输出.for文件的路径
    '''
    f = open(insert_user_name, 'r')  # your path!
    lines_old = []
    for line in f:
        lines_old.append(line)
    f.close()

    # 开始读取当前insert文件,将所有的子程序文本存入lines_user_FILM
    lines_user_FILM = []
    f2 = open(insert_data_file, 'r')  # your path!
    for line in f2:
        lines_user_FILM.append(line)
    f2.close()

    # 再把读到的lines__user写入到lines_old
    for i in range(len(lines_user_FILM)):
        lines_old.insert(num + i, lines_user_FILM[i] + '\n')  # 第四行插入666并回车

    s = ''.join(lines_old)
    # 新建一个文本，开始写入上述文本，并返回将来子程序钓鱼岛 。for文件
    user_current = userfile_path + 'Propellant_' + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') +'.for'
    f = open(user_current, 'w+')  # 重新写入文件
    f.write(s)
    f.close()
    del lines_old[:]  # 清空列表
    print('%s has been write %s'%(insert_data_file,user_current))
    return user_current



table_list = ((0, 297), (20, 232), (740, 232), (741, 322), (1460, 322), (1461, 297), (1470, 297))
file_path = creat_thermal_user_data(table_list)

# 基于初始文本，生成新的的.for文件，为保证两次写入的文件是一个，开始预先定义。for的路径

user_init = userfile_path + 'Propellant.for'
# 初始文本位置 # 获取FILM的位置 # 写入FILM的数据，0---代表FILM的位置
CFILMstart_num = access_taget('CFILMstart',user_init)
user_file_path = write_data(user_init,CFILMstart_num, file_path[0])

#第一次修改后的文本位置
# 获取DISP的位置# 写入DISP的数据，1---代表DISP的位置
cDISPstart_num = access_taget('cDISPstart',user_file_path)
user_file_path = write_data(user_file_path,cDISPstart_num,file_path[1])
# print('DISP and FILM successfule write .for!')