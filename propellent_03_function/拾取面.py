#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 拾取面.py
# @Author: YC
# @Date  : 2019/1/26
'''
当我ABAQUS 界面点击pick时，软件后台自动输出一个tuple，内容分别如下，有几个面，那么就有几个元素
'''
# face = (
#     mdb.models['Model-1'].rootAssembly.instances['composite-1'].faces[2],
#     mdb.models['Model-1'].rootAssembly.instances['composite-1'].faces[3],
#     mdb.models['Model-1'].rootAssembly.instances['composite-1'].faces[15],
#     mdb.models['Model-1'].rootAssembly.instances['composite-1'].faces[18]
#         )

# from propellent_03_function.propellent_03_function import *



list = [2, 3, 15, 18]
# str1 = ''.join([str(x) for x in list])
str2 = ' '.join([str(x) for x in list])



list = ['2', '3', '15', '18']
f= open('da1.txt','w')
list_index_None = []
for i in list:
    print(i)
    f.write(i)
    f.write(' ')
f.close()

list_index = []
with open('da1.txt','r') as f:
    for i in f:
        list_index1 = i.split()
    for i in list_index1:
        list_index.append(int(i))
        print(int(i))
    # list_index_None.append(i)
    # print(i.strip(','))
print(list_index)
print(type(list_index))
# print(type(list_index_None))
# print(list_index_None)
# list_index = []
# for i in range(len(list_index_None)):
#     if list_index_None[i] != '\n':
#         print(list_index_None[i])
#         list_index.append(list_index_None[i])

# list_index
list_index1 = []
# for i in range(len(list_index)):
#     if list_index[i] != '\n':
#         print(list_index[i])
#         list_index1.append(list_index[i])
# readTXT('da1.txt', 2)
# print(list_index1)
# print(list(eval(list_index1)))