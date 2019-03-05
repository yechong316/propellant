# -* - coding:UTF-8 -*-

#Start defining data for interfaces and text
class var_data:

    def __init__(self):
        self.var_data = 'file'
        self.GUI_Force = 60
        self.GUI_Thickness = 0.25
        self.GUI_Width = 4
        self.GUI_CPUnum = 1

        self.file_Force = 59
        self.file_Thickness = 0.25
        self.file_Width = 4
        self.file_CPUnum = 1

    @property
    def extract_var(self):
        return self.var_data

#Start defining methods for extracting GUI data
class Data_GUI(var_data):
    @property
    def Force(self):
        return self.GUI_Force
    @property
    def Thickness(self):
        return self.GUI_Thickness
    @property
    def Width(self):
        return self.GUI_Width
    @property
    def CPUnum(self):
        return self.GUI_CPUnum

#Start defining methods for extracting file data
class Data_file(var_data):
    @property
    def Force(self):
        return self.file_Force
    @property
    def Thickness(self):
        return self.file_Thickness
    @property
    def Width(self):
        return self.file_Width
    @property
    def CPUnum(self):
        return self.file_CPUnum
