# -* - coding:UTF-8 -*-

#Start defining data for interfaces and text
class var_data:

    def __init__(self):
        self.var_data = 'file'
        self.GUI_time = 3600
        self.GUI_init_temp = 303
        self.GUI_CPUnum = 1

        self.file_time = 3600

        self.file_init_temp = 300

        self.file_CPUnum = 1

    @property
    def extract_var(self):
        return self.var_data

#Start defining methods for extracting GUI data
class Data_GUI(var_data):
    @property
    def time(self):
        return self.GUI_time
    @property
    def init_temp(self):
        return self.GUI_init_temp
    @property
    def CPUnum(self):
        return self.GUI_CPUnum

#Start defining methods for extracting file data
class Data_file(var_data):
    @property
    def time(self):
        return self.file_time
    @property
    def init_temp(self):
        return self.file_init_temp
    @property
    def CPUnum(self):
        return self.file_CPUnum
