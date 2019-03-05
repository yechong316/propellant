#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : define_user_sub_total.py
# @Author: YC
# @Date  : 2019/1/25
import os
import datetime
current_path = os
def creat_DISPdata(table_list):
    with open('DISP_temp.txt', 'w') as f:
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

def creat_FILMdata(table_list):
    with open('DISP_temp.txt', 'w') as f:
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
    with open('FILM_temp.txt', 'w') as f:
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

def access_taget(label):
    f = open('main-composite_curing.for', 'r')
    lines = []
    for line in f:
        lines.append(line)
    f.close()
    for i in range(len(lines)):
        if lines[i] == label + '\n':
            return i


def write_data(FILM_num, DISP_num):
    lines_old = []
    f = open('main-composite_curing.for', 'r')  # your path!
    for line in f:
        lines_old.append(line)
    f.close()
    lines_DISP = []
    f2 = open('DISP_temp.txt', 'r')  # your path!
    for line in f2:
        lines_DISP.append(line)
    f2.close()

    lines_FILM = []
    f2 = open('FILM_temp.txt', 'r')  # your path!
    for line in f2:
        lines_FILM.append(line)
    f2.close()


    for i in range(len(lines_DISP)):
        lines_old.insert(i + DISP_num, lines_DISP[i] + '\n')  # 第四行插入666并回车
    for i in range(len(lines_FILM)):
        lines_old.insert(i + FILM_num, lines_FILM[i] + '\n')  # 第四行插入666并回车
    s = ''.join(lines_old)
    date_user = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    f = open('main-composite_curing_' + date_user + '.for', 'w+')  # 重新写入文件
    f.write(s)
    f.close()
    del lines_old[:]  # 清空列表



    table_list = ((0, 297), (20, 232), (740, 232), (741, 322), (1460, 322), (1461, 297), (1470, 297))

    creat_DISPdata(table_list)
    creat_FILMdata(table_list)

    CFILMstart_num = access_taget('CFILMstart')
    cDISPstart_num = access_taget('cDISPstart')

    user_file_path = write_data(CFILMstart_num, cDISPstart_num)