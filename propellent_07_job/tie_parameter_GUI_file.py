# -* - coding:UTF-8 -*-

#Start defining data for interfaces and text
class var_data:

    def __init__(self):
        self.var_data = 'file'
        self.GUI_c_b_position = 0.1
        self.GUI_c_b_var = True
        self.GUI_b_f_position = 0.1
        self.GUI_b_f_var = False
        self.GUI_b_h_position = 0.9
        self.GUI_b_h_var =  False
        self.GUI_h_f_position = 0.1
        self.GUI_h_f_var = False

        self.file_c_b_position = 0.1
        self.file_c_b_var = True
        self.file_b_f_position = 0.1
        self.file_b_f_var = False
        self.file_b_h_position = 0.9
        self.file_b_h_var =  False
        self.file_h_f_position = 0.1
        self.file_h_f_var = False

    @property
    def extract_var(self):
        return self.var_data

#Start defining methods for extracting GUI data
class Data_GUI(var_data):
    @property
    def c_b_position(self):
        return self.GUI_c_b_position
    @property
    def c_b_var(self):
        return self.GUI_c_b_var
    @property
    def b_f_position(self):
        return self.GUI_b_f_position
    @property
    def b_f_var(self):
        return self.GUI_b_f_var
    @property
    def b_h_position(self):
        return self.GUI_b_h_position
    @property
    def b_h_var(self):
        return self.GUI_b_h_var
    @property
    def h_f_position(self):
        return self.GUI_h_f_position
    @property
    def h_f_var(self):
        return self.GUI_h_f_var

#Start defining methods for extracting file data
class Data_file(var_data):
    @property
    def c_b_position(self):
        return self.file_c_b_position
    @property
    def c_b_var(self):
        return self.file_c_b_var
    @property
    def b_f_position(self):
        return self.file_b_f_position
    @property
    def b_f_var(self):
        return self.file_b_f_var
    @property
    def b_h_position(self):
        return self.file_b_h_position
    @property
    def b_h_var(self):
        return self.file_b_h_var
    @property
    def h_f_position(self):
        return self.file_h_f_position
    @property
    def h_f_var(self):
        return self.file_h_f_var
