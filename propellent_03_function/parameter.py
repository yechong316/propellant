# -* - coding:UTF-8 -*-
#!/usr/bin/python3
'''
功能：将用户在GUI或者文本导入的数据封装成一个类，供注册文件进行调用，在界面
实现显示数据

思路：首先定义一个类，在初始构造函数首先写一个文件类型标识，根据标识的不同注册文件调用不同的数据
'''

class var_data:
    '''
    功能：设置一个开关，当用户导入外部数据，则
    self.var_data = 'file'   反之为；
    elf.var_data = 'GUI'

    '''
    def __init__(self):

        # 设置设置此时界面的数据来自哪里
        # self.var_data = 'file'
        self.var_data = 'GUI'

        # GUI-
        self.GUI_cd = 1.2e-6

        # 开始定义file的参数
        self.file_c_d = 2.4e-6


    #     定义文本


    #
    @property
    def extract_var(self):
        return self.var_data


class Data_GUI(var_data):
    '''
    功能：用户在界面输入的参数封装成常量，供注册文件调用
    '''
    # def __init__(self):
    #     self.ecd = 1.2222e-6

    @property
    def cd(self):
        return self.GUI_cd


class Data_file(var_data):
    '''
    功能：用户导入文本内的参数封装成常量，供注册文件调用
    '''
    # def __init__(self):
    @property
    def cd(self):
        return self.file_cd

# Data1 = var_data()
# Data2 = Data()
# print(var_data().extract_var)
# print type(Data1.extract_var)
# print type(Data2.cd)