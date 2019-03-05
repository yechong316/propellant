# -* - coding:UTF-8 -*-
#!/usr/bin/python3
# propellant_v0125-1100 
# Authorn:Jaime Lannister
# Time:2019/2/14-19:00
'''
功能：在注册文件中生成形如以下的数据
    data_c_d = Data_GUI().c_d
    data_c_e = Data_GUI().c_e
    data_c_p = Data_GUI().c_p
           ...
'''
thermal_name = ['time', 'init_temp', 'CPUnum']

f = open('temp_thermal_plugin.txt', 'w')
s = "from propellent_07_job.thermal_parameter_GUI_file import *\n\n" \
    "if var_data().extract_var == 'GUI':\n"
f.write(s)


for i in range(3):
    # 核心代码下面一行为具体要生成的内容
    s = ''.join(['    data_', thermal_name[i],
                 ' = Data_GUI().', thermal_name[i], '\n'])
    f.write(s)

s = "elif var_data().extract_var == 'file':\n\n"
f.write(s)

for i in range(3):
    # 核心代码，下面一行为具体要生成的内容
    s = ''.join(['    data_', thermal_name[i],
                 ' = Data_file().', thermal_name[i], '\n'])
    f.write(s)
f.write('\n')
f.close()