#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 生成DISP之间的内容.py
# @Author: YC
# @Date  : 2019/1/25
import sys
table_list = ((0, 297), (20, 232), (740, 232), (741, 322), (1460, 322), (1461, 297), (1470, 297))
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


creat_DISPdata(table_list)