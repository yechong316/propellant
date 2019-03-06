# -*- coding: utf-8 -*-
#!/usr/bin/python3
# propellant 
# Authorn:Jaime Lannister
# Time:2019/3/6-12:29 

# 读取材料参数
def readTXT(txtname, plug_type):
    '''
    要求用户导入一个文件，然后根据不同的文件类型进行读取
    plug_type = 1 表示插件1，等于2表示写入插件2，依次类推,返回没有任何换行符号的字符串
    '''
    # 将删去汉字等无用符号的文本存入到一个临时文件中
    file = 'data_temp.txt'

    # 导入构件
    if plug_type == 1:
        # print('READTXT IS SUCCESSFUL STARTING!!!')
        # 打开该txt文件
        with open(txtname, 'r') as f:
            data_origin = f.read()
        #     删除无用汉字文本
        data_origin = data_origin.replace('复合材料壳体:', '')
        data_origin = data_origin.replace('使用说明：每一行的数据分别为该构件的密度、弹性模量、泊松比、热传导系数、比热容系数、热膨胀系数和网格尺寸', '')
        data_origin = data_origin.replace('包覆层:', '')
        data_origin = data_origin.replace('封头:', '')
        data_origin = data_origin.replace('推进剂:', '')
        with open(file, 'w') as fpw:
            fpw.write(data_origin)
        # data_total = data_origin
        F1 = open(file, "r")
        data_total = F1.readlines()
        mat_size = []
        for i in range(1, len(data_total)):
            data_None_str = data_total[i].strip().split("、")  # 每一行split后是一个列表
            data_str = filter(None, data_None_str)
            data = map(float, data_str)
            mat_size.append(data)
            # for j in data_str:
            #     data_str
            # mat_size.append(map(float, data_str))
            # for j in range(len(data_total[i])):

            # print('before:', type(data_str[i]))
            # map(float, filter(None, data_str[i]))

            # print('after:', type(data_str[i]))
        #  jiang

        # for i in range(1, len(list_source)):
        #     mat_size.append(map(float, filter(None, list_source[i])))
        F1.close()
        # print('The data from {} has been imported to CAE!'.format(txtname))
        return mat_size

    # 绑定关系
    elif plug_type == 2:
        # print('READTXT TIE IS SUCCESSFUL STARTING')
        # 打开该txt文件
        with open(txtname, 'r') as f:
            data_origin = f.read()

        #     删除无用汉字文本
        data_origin = data_origin.replace('推进剂VS封头:', '')
        data_origin = data_origin.replace('使用说明：每一行的数据分别为该构件的主面坐标、从面坐标、位置容差、是否切换主从面', '')
        data_origin = data_origin.replace('复合材料VS包覆层:', '')
        data_origin = data_origin.replace('包覆层VS封头:', '')
        data_origin = data_origin.replace('包覆层VS推进剂:', '')

        # 将处理后的数据写入到临时文本，然后将存到list_source中
        with open(file, 'w') as fpw:
            fpw.write(data_origin)
        # data_total = data_origin
        F1 = open(file, "r")
        data_total = F1.readlines()
        data_tie = []
        for i in range(1, len(data_total)):
            data_None_str = data_total[i].strip().split("、")  # 每一行split后是一个列表
            data_str = filter(None, data_None_str)
            data_tie.append(data_str)

        data = [
            [str_indes2Face(data_tie[0][0]), str_indes2Face(data_tie[0][1]), float(data_tie[0][2]),
             str2bool(data_tie[0][3])],
            [str_indes2Face(data_tie[1][0]), str_indes2Face(data_tie[1][1]), float(data_tie[1][2]),
             str2bool(data_tie[1][3])],
            [str_indes2Face(data_tie[2][0]), str_indes2Face(data_tie[2][1]), float(data_tie[2][2]),
             str2bool(data_tie[2][3])],
            [str_indes2Face(data_tie[3][0]), str_indes2Face(data_tie[3][1]), float(data_tie[3][2]),
             str2bool(data_tie[3][3])],
        ]
        # print('The data[3][3]  of tie is :',data[3][3])
        return data

    # 温度冲击
    elif plug_type == 3:
        # print('readTXT-functiong is successful starting')

        # 打开该txt文件
        with open(txtname, 'r') as f:
            data_origin = f.read()
        #     删除无用汉字文本
        data_origin = data_origin.replace('温度冲击试验时间:', '')
        data_origin = data_origin.replace('使用说明：每一行的数据分别对应温度冲击试验时间，构件初始温度，升降温曲线，复合材料外表面坐标，CPU核数', '')
        data_origin = data_origin.replace('构件初始温度:', '')
        data_origin = data_origin.replace('升降温曲线:', '')
        data_origin = data_origin.replace('复合材料外表面索引:', '')
        data_origin = data_origin.replace('CPU核数:', '')
        # print('After delete:data_origin:')
        # print(data_origin)
        with open(file, 'w') as fpw:
            fpw.write(data_origin)
        data_total = data_origin
        F1 = open(file, "r")
        data_total = F1.readlines()
        list_source = []
        for i in range(len(data_total)):
            data_str = data_total[i]  # 每一行split后是一个列表
            list_source.append(data_str)
        for line in F1.readlines():
            line = line.strip('\n')
        # print('End of data_thermal reading!')
        # 开始删除空格符号
        list = []
        for i in list_source:
            if i != '\n':
                list.append(i)
        for i in list:
            i.replace('\n', '')
        print('Finish gain the thermal data from txt!')
        return list

    # 固化工艺
    elif plug_type == 4:
        # print('readTXT is successful starting')
        # 打开该txt文件
        with open(txtname, 'r') as f:
            data_origin = f.read()
        #     删除无用汉字文本
        data_origin = data_origin.replace('固化工艺时间:', '')
        data_origin = data_origin.replace('使用说明：每一行的数据分别对应固化工艺时间，构件初始温度，升降温曲线，复合材料外表面坐标，CPU核数', '')
        data_origin = data_origin.replace('构件初始温度:', '')
        data_origin = data_origin.replace('升降温曲线:', '')
        data_origin = data_origin.replace('复合材料外表面索引:', '')
        data_origin = data_origin.replace('CPU核数:', '')
        # print('After delete:data_origin:')
        with open(file, 'w') as fpw:
            fpw.write(data_origin)
        data_total = data_origin
        F1 = open(file, "r")
        data_total = F1.readlines()

        list_source = []
        for i in range(len(data_total)):
            data_str = data_total[i]  # 每一行split后是一个列表
            list_source.append(data_str)
        for line in F1.readlines():
            line = line.strip('\n')

        # 开始删除空格符号
        list = []
        for i in list_source:
            if i != '\n':
                list.append(i)
        for i in list:
            i.replace('\n', '')
        print('The data of curing has been import to CAE!')

        return list

    # 缠绕工艺
    elif plug_type == 5:
        # 打开该txt文件
        with open(txtname, 'r') as f:
            data_origin = f.read()
        #     删除无用汉字文本
        data_origin = data_origin.replace('预紧力:', '')
        data_origin = data_origin.replace('使用说明：每一行的数据分别对应预紧力,纤维铺层厚度，纤维宽度，CPU核数', '')
        data_origin = data_origin.replace('纤维铺层厚度:', '')
        data_origin = data_origin.replace('纤维宽度:', '')
        data_origin = data_origin.replace('CPU核数:', '')
        # print(data_origin)
        with open(file, 'w') as fpw:
            fpw.write(data_origin)
        # data_total = data_origin
        F1 = open(file, "r")
        data_total = F1.readlines()
        list_source = []
        for i in range(len(data_total)):
            # print(data_total[i])
            data_str = data_total[i].strip().split(",")  # 每一行split后是一个列表
            list_source.append(data_str)
        # 开始删除空格符号
        list = []
        for i in list_source:
            if i != '\n':
                # print(i)
                list.append(i)
        F1.close()
        return list
    # F1.close()

    print('The data from {} has been imported to CAE!'.format(txtname))
    # os.remove(file)

# 将字符串索引转变为数字序列
def str_indes2Face(str):
    '''
    一、提取用户选取的面 的索引
    二。组成序列后转换为字符串序列
    eg：'2 3 15 18'
    返回的是：[2, 3, 15, 18]
    '''
    numbers = map(int, str.split(' '))
    # print('str_index has been transfer index')
    return numbers
    '''
    一、提取用户选取的面 的索引
    二。组成序列后转换为字符串序列
    eg：'2 3 15 18'
    返回的是：[2, 3, 15, 18]
    '''
    # print(sys._getframe().f_lineno)
    list = []
    list = str.split(' ')
    numbers = map(int, list)
    for i in numbers:
        list.append(i)
    str2 = ' '.join([str(x) for x in list])
    # print('Face has been transfer str_index')
    # print(list)
    # print(str2)
    return str2

# 将字符串布尔值 ---》 布尔值
def str2bool(str):
    if str == 'True':
        return True
    else:
        return False

inputfile = r"D:\temp\abaqus_plugins\propellant\propellent_04_data\Tie_v2019-01-27_23-27-40.txt"
input_data = readTXT(inputfile, 2)

instance_list = ['unknown', 'bfc-1', 'fengtou-1', 'propeller-1']
tie_instance = [
    [instance_list[0], instance_list[1]],
    [instance_list[1], instance_list[2]],
    [instance_list[1], instance_list[3]],
    [instance_list[3], instance_list[2]]
]

tie_data = [
    [zip(tie_instance[0], [input_data[0][0], input_data[0][1]] ),input_data[0][2],input_data[0][3]],
    [zip(tie_instance[1], [input_data[1][0], input_data[1][1]] ),input_data[1][2],input_data[1][3]],
    [zip(tie_instance[2], [input_data[2][0], input_data[2][1]] ),input_data[2][2],input_data[2][3]],
    [zip(tie_instance[3], [input_data[3][0], input_data[3][1]] ),input_data[3][2],input_data[3][3]]
]
# print(dict(zip(tie_instance[0], tie_index[0])))
print(tie_data[0])
print(tie_data)

# def xx(*w):
#     print(w)
#
# xx(instance_list[0])