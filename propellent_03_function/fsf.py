#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : fsf.py
# @Author: YC
# @Date  : 2019/1/27
indexlist = [2, 3, 15, 18]

a = mdb.models['Model-1'].rootAssembly
side1Faces = []
for i in range(len(indexlist)):

    print('current indexlist:')
    print(indexlist[i])
    print(type(indexlist[i]))
    # 依次索引当前面的对象
    # print(indexlist[i].index)
    print(a.instances['composite-1'].faces[indexlist[i]:indexlist[i]+1])
    list.append(a.instances['composite-1'].faces[indexlist[i]:indexlist[i]+1])


side1Faces = []
for i in range(len(indexlist)):
    print('current indexlist:')
    print(indexlist[i])
    print(type(indexlist[i]))
    # 依次索引当前面的对象
    # print(indexlist[i].index)
    # print(a.instances['composite-1'].faces[indexlist[i]:indexlist[i]+1])
    side1Faces.append(a.instances['composite-1'].faces[indexlist[i]:indexlist[i] + 1])