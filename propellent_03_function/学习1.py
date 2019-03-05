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

# tup = readTXT("E:\propellant_v2019年1月26日155418\propellent_04_data\Tie_v2019-01-26_21-46-18.txt", 2)
# print(type(tup[0][0]))
# tup1 = tuple(eval(tup[0][0]))


def str2tup(str):
    tup = tuple(eval(str))
    return tup

def str2TrueFalse(str):
    if str == 'True':

        return True
    else:
        return False


# print(type('True'))
# print(type(str2TrueFalse('True')))
# print(type(str2tup(tup[0][0])))

# def str2tup(str):
#     tup = tuple(eval(str))
#     return tup

def readTXT(txtname, plug_type):
    '''
    要求用户导入一个文件，然后根据不同的文件类型进行读取
    plug_type = 1 表示插件1，等于2表示写入插件2，依次类推
    :param data:
    :return:
    '''
    file = 'test1.txt'
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
        with open(txtname, 'r',encoding='UTF-8') as fpr:
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
    elif plug_type == 3:
        print('readTXT is successful starting')
        # 打开该txt文件
        with open(txtname, 'r') as fpr:
            content = fpr.read()
        #     删除无用汉字文本
        content = content.replace('温度冲击试验时间:', '')
        content = content.replace('使用说明：每一行的数据分别对应温度冲击试验时间，构件初始温度，升降温曲线，复合材料外表面坐标，CPU核数', '')
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
    # os.remove(file)

input_data = readTXT("E:\propellant_v2019年1月26日155418\propellent_04_data\Tie_v2019-01-26_21-46-18.txt", 2)
# print(str2tup(input_data[0][0]))

print(type(input_data[0][0]))
for i in input_data[0][0]:
    print(type(float(i)))





def Tie_kernel(
        # 定义4个tie绑定对，分别为主面，从面，容差
        Master_cb=None,Slave_cb=None,Position_cb=None,var_cb=None,
        Master_bf=None,Slave_bf=None,Position_bf=None,var_bf=None,
        Master_bh=None,Slave_bh=None,Position_bh=None,var_bh=None,
        Master_hf=None,Slave_hf=None,Position_hf=None,var_hf=None,
        var_export=False, var_input=False, inputfile=None
                   ):
    # 当用户勾选此选项，数据导出，
    data_tie = [
        [Master_cb,Slave_cb,Position_cb,var_cb],
        [Master_bf,Slave_bf,Position_bf,var_bf],
        [Master_bh,Slave_bh,Position_bh,var_bh],
        [Master_hf,Slave_hf,Position_hf,var_hf]
    ]
    # if var_export == True:
    #     exportTXT(data_tie, 2)
    a = mdb.models['Model-1'].rootAssembly
    # **********01**********-开始生成接触对复合材料壳体-包覆层:复合材料壳体
    s1 = a.instances['composite-1'].faces
    side1FacesMaster_cb = s1.findAt(Master_cb)
    s1 = a.instances['bfc-1'].faces
    side1FacesSlave_cb = s1.findAt(Slave_cb)
    region_Master_cb = a.Surface(side1Faces=side1FacesMaster_cb, name='CP_cb_M')
    region_Slave_cb = a.Surface(side1Faces=side1FacesSlave_cb, name='CP_cb_S')
    mdb.models['Model-1'].Tie(name='Constraint_cb', master=region_Master_cb,
                              slave=region_Slave_cb, positionToleranceMethod=SPECIFIED,
                              positionTolerance=Position_cb,
                              adjust=ON, tieRotations=ON, thickness=ON)
    if var_cb == True:
        mdb.models['Model-1'].constraints['Constraint_cb'].swapSurfaces()
    # **********02**********-开始生成接触对包覆层-封头:主面
    s1 = a.instances['bfc-1'].faces
    side1FacesMaster_bf = s1.findAt(Master_bf)
    # 02-开始生成接触对包覆层-封头:从面
    s1 = a.instances['fengtou-1'].faces
    side1FacesSlave_bf= s1.findAt(Slave_bf)
    # 02完成定义两个面之后，开始生成tie绑定关系
    region_Master_bf = a.Surface(side1Faces=side1FacesMaster_bf, name='CP_bf_M')
    region_Slave_bf = a.Surface(side1Faces=side1FacesSlave_bf, name='CP_bf_S')
    mdb.models['Model-1'].Tie(name='Constraint_bf', master=region_Master_bf,
                              slave=region_Slave_bf, positionToleranceMethod=SPECIFIED,
                              positionTolerance=Position_bf,
                              adjust=ON, tieRotations=ON, thickness=ON)
    if var_bf == True:
        mdb.models['Model-1'].constraints['Constraint_bf'].swapSurfaces()
    # **********03**********-开始生成接触对包覆层-火药:主面
    s1 = a.instances['bfc-1'].faces
    side1FacesMaster_bh = s1.findAt(cor_list[num])
    # 03-开始生成接触对包覆层-火药:从面
    s1 = a.instances['propeller-1'].faces
    side1FacesSlave_bh = s1.findAt(cor_list[num])
    # 03完成定义两个面之后，开始生成tie绑定关系
    region_Master_bh = a.Surface(side1Faces=side1FacesMaster_bh, name='CP_bh_M')
    region_Slave_bh = a.Surface(side1Faces=side1FacesSlave_bh, name='CP_bh_S')
    mdb.models['Model-1'].Tie(name='Constraint_bh', master=region_Master_bh,
                              slave=region_Slave_bh, positionToleranceMethod=SPECIFIED,
                              positionTolerance=Position_bh,
                              adjust=ON, tieRotations=ON, thickness=ON)
    if var_bh == True:
        mdb.models['Model-1'].constraints['Constraint_bh'].swapSurfaces()
    # **********04**********-开始生成接触对火药-封头:主面
    s1 = a.instances['propeller-1'].faces
    side1FacesMaster_hf = s1.findAt(cor_list[num])
    # -开始生成接触对火药-封头:从面
    s1 = a.instances['fengtou-1'].faces
    side1FacesSlave_hf = s1.findAt(cor_list[num])
    # 完成定义两个面之后，开始生成tie绑定关系
    region_Master_hf = a.Surface(side1Faces=side1FacesMaster_hf, name='CP_hf_M')
    region_Slave_hf = a.Surface(side1Faces=side1FacesSlave_hf, name='CP_hf_S')
    # 04-开始生成接触对火药-封头
    mdb.models['Model-1'].Tie(name='Constraint_hf', master=region_Master_hf,
                              slave=region_Slave_hf, positionToleranceMethod=SPECIFIED,
                              positionTolerance=Position_hf,
                              adjust=ON, tieRotations=ON, thickness=ON)
    if var_hf == True:
        mdb.models['Model-1'].constraints['Constraint_hf'].swapSurfaces()



# n = (
#     ((138.202799, -35.3656, 3.08615),),
#  ((112.299998, 3.08615, 35.3656),),
#  ((112.299998, -3.08615, -35.3656),),
#  ((140.297195, 35.3656, -3.08615),)
# )

def tag(str):
    print(type(str.pointOn))

def fun_sub(num):
    n1 = num +12
    print(n1)

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


t = (((158.2, 3.924884, -21.724326),), ((158.2, 1.219623, 10.574432),), ((158.2, -3.924882, 21.724325),), ((158.2, -1.735526, -11.006278),))
# f = open('d.txt', 'w')
# f.write(str(t))
# f.close()
def str2tup(str):
    tup = list(str)
    return tup
