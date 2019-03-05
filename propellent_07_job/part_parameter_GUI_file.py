# -* - coding:UTF-8 -*-

#Start defining data for interfaces and text
class var_data:

    def __init__(self):
        self.var_data = 'file'
        self.GUI_c_d = 1.2e-6
        self.GUI_c_e = 23500
        self.GUI_c_p = 0.33
        self.GUI_c_c = 0.00043
        self.GUI_c_s = 826
        self.GUI_c_ep = 0.00143
        self.GUI_c_mesh_size = 5
        self.GUI_b_d = 1.23E-006
        self.GUI_b_e = 0.384
        self.GUI_b_p = 0.3
        self.GUI_b_c = 1
        self.GUI_b_s = 1219
        self.GUI_b_ep = 0.000326
        self.GUI_b_mesh_size = 5
        self.GUI_f_d = 0.00785
        self.GUI_f_e =  2e5
        self.GUI_f_p = 0.3
        self.GUI_f_c = 1.6578
        self.GUI_f_s = 512
        self.GUI_f_ep = 1.22E-005
        self.GUI_f_mesh_size = 3
        self.GUI_h_d = 1.65E-006
        self.GUI_h_e = 4000
        self.GUI_h_p = 0.3
        self.GUI_h_c = 0.001
        self.GUI_h_s = 1500
        self.GUI_h_ep = 0.0001263
        self.GUI_h_mesh_size = 5

        self.file_c_d = 1.23e-06
        self.file_c_e = 235200
        self.file_c_p = 0.33
        self.file_c_c = 0.00043
        self.file_c_s = 826
        self.file_c_ep = 0.00143
        self.file_c_mesh_size = 5
        self.file_b_d = 1.23e-06
        self.file_b_e = 0.384
        self.file_b_p = 0.3
        self.file_b_c = 1
        self.file_b_s = 1219
        self.file_b_ep = 0.000326
        self.file_b_mesh_size = 5
        self.file_f_d = 0.00785
        self.file_f_e = 200000
        self.file_f_p = 0.3
        self.file_f_c = 1.6578
        self.file_f_s = 512
        self.file_f_ep = 1.22e-05
        self.file_f_mesh_size = 3
        self.file_h_d = 1.65e-06
        self.file_h_e = 4000
        self.file_h_p = 0.3
        self.file_h_c = 0.001
        self.file_h_s = 1500
        self.file_h_ep = 0.0001263
        self.file_h_mesh_size = 5

    @property
    def extract_var(self):
        return self.var_data

#Start defining methods for extracting GUI data
class Data_GUI(var_data):
    @property
    def c_d(self):
        return self.GUI_c_d
    @property
    def c_e(self):
        return self.GUI_c_e
    @property
    def c_p(self):
        return self.GUI_c_p
    @property
    def c_c(self):
        return self.GUI_c_c
    @property
    def c_s(self):
        return self.GUI_c_s
    @property
    def c_ep(self):
        return self.GUI_c_ep
    @property
    def c_mesh_size(self):
        return self.GUI_c_mesh_size
    @property
    def b_d(self):
        return self.GUI_b_d
    @property
    def b_e(self):
        return self.GUI_b_e
    @property
    def b_p(self):
        return self.GUI_b_p
    @property
    def b_c(self):
        return self.GUI_b_c
    @property
    def b_s(self):
        return self.GUI_b_s
    @property
    def b_ep(self):
        return self.GUI_b_ep
    @property
    def b_mesh_size(self):
        return self.GUI_b_mesh_size
    @property
    def f_d(self):
        return self.GUI_f_d
    @property
    def f_e(self):
        return self.GUI_f_e
    @property
    def f_p(self):
        return self.GUI_f_p
    @property
    def f_c(self):
        return self.GUI_f_c
    @property
    def f_s(self):
        return self.GUI_f_s
    @property
    def f_ep(self):
        return self.GUI_f_ep
    @property
    def f_mesh_size(self):
        return self.GUI_f_mesh_size
    @property
    def h_d(self):
        return self.GUI_h_d
    @property
    def h_e(self):
        return self.GUI_h_e
    @property
    def h_p(self):
        return self.GUI_h_p
    @property
    def h_c(self):
        return self.GUI_h_c
    @property
    def h_s(self):
        return self.GUI_h_s
    @property
    def h_ep(self):
        return self.GUI_h_ep
    @property
    def h_mesh_size(self):
        return self.GUI_h_mesh_size

#Start defining methods for extracting file data
class Data_file(var_data):
    @property
    def c_d(self):
        return self.file_c_d
    @property
    def c_e(self):
        return self.file_c_e
    @property
    def c_p(self):
        return self.file_c_p
    @property
    def c_c(self):
        return self.file_c_c
    @property
    def c_s(self):
        return self.file_c_s
    @property
    def c_ep(self):
        return self.file_c_ep
    @property
    def c_mesh_size(self):
        return self.file_c_mesh_size
    @property
    def b_d(self):
        return self.file_b_d
    @property
    def b_e(self):
        return self.file_b_e
    @property
    def b_p(self):
        return self.file_b_p
    @property
    def b_c(self):
        return self.file_b_c
    @property
    def b_s(self):
        return self.file_b_s
    @property
    def b_ep(self):
        return self.file_b_ep
    @property
    def b_mesh_size(self):
        return self.file_b_mesh_size
    @property
    def f_d(self):
        return self.file_f_d
    @property
    def f_e(self):
        return self.file_f_e
    @property
    def f_p(self):
        return self.file_f_p
    @property
    def f_c(self):
        return self.file_f_c
    @property
    def f_s(self):
        return self.file_f_s
    @property
    def f_ep(self):
        return self.file_f_ep
    @property
    def f_mesh_size(self):
        return self.file_f_mesh_size
    @property
    def h_d(self):
        return self.file_h_d
    @property
    def h_e(self):
        return self.file_h_e
    @property
    def h_p(self):
        return self.file_h_p
    @property
    def h_c(self):
        return self.file_h_c
    @property
    def h_s(self):
        return self.file_h_s
    @property
    def h_ep(self):
        return self.file_h_ep
    @property
    def h_mesh_size(self):
        return self.file_h_mesh_size
