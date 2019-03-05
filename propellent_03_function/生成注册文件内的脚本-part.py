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
part_name = ['c', 'b', 'f', 'h']
property_name = ['d', 'e', 'p', 'c', 's', 'ep', 'mesh_size']

f = open('temp_part_plugin.txt', 'a')
for i in range(4):
    for j in range(7):
        s = ''.join(['    data_', part_name[i], '_', property_name[j],
                     ' = Data_file().', part_name[i], '_', property_name[j] + '\n'
                     ])
        f.write(s)
f.write('\n')
f.close()