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
tie_pair_name = ['c_b', 'b_f', 'b_h', 'h_f']
var_name = ['position', 'var']

# 默认参数值
tie_defalut_data = [
    ['0.1', 'True'],
    ['0.1', 'False'],
    ['0.9', ' False'],
    ['0.1', 'False']
]

f = open('temp_tie_plugin.txt', 'w')
s = "from propellent_07_job.tie_parameter_GUI_file import *\n\n" \
    "if var_data().extract_var == 'GUI':\n"
f.write(s)


for i in range(4):
    for j in range(2):
        # 核心代码，下面一行为具体要生成的内容
        s = ''.join(['    data_', tie_pair_name[i], '_', var_name[j],
                     ' = Data_GUI().', tie_pair_name[i], '_', var_name[j] + '\n'])
        f.write(s)

s = "elif var_data().extract_var == 'file':\n\n"
f.write(s)

for i in range(4):
    for j in range(2):
        # 核心代码，下面一行为具体要生成的内容
        s = ''.join(['    data_', tie_pair_name[i], '_', var_name[j],
                     ' = Data_file().', tie_pair_name[i], '_', var_name[j] + '\n'])
        f.write(s)
f.write('\n')
f.close()