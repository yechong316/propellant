file_name = 'abaqus-50.rpt'
import math as m
with open('D:/temp/' + file_name) as f:
    count = f.readlines()

    data = count[::-1][4]
    print(data)


    data_max = data.split('            ')[1].split('      ')[0]
    data_mid = data.split('              ')[1].split('      ')[1].split('     ')[0]
    data_min = data.split('              ')[1].split('      ')[1].split('     ')[1].split('\n')[0]
    # data_min = list(filter(None, data_min))
    data_E = [data_max, data_mid, data_min]
    data_E = list(map(float, data_E))

    print(data_E)
    e1 = m.pow(abs(data_E[0] - data_E[1]), 2)
    e2 = m.pow(abs(data_E[1] - data_E[2]), 2)
    e3 = m.pow(abs(data_E[2] - data_E[0]), 2)

    data_stard = 1.414/2 * m.pow((e1+e2+e3), 0.5)
    data_E.append(data_stard)

    result_path = "D:\旧电脑\[2019年5月7日]固体发动机报告/06_计算文件\s1\Curing\Struct01-Curing-50.txt"
    with open(result_path, 'a') as f2:
        for i in data_E:
            print(str(i))
            f2.write(str(i))
            f2.write(' ')