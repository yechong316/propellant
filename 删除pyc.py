import os




def get_dir(path):  # 获取目录路径
    for root, dirs, files in os.walk(path):  # 遍历path,进入每个目录都调用visit函数，，有3个参数，root表示目录路径，dirs表示当前目录的目录名，files代表当前目录的文件名
        for dir in dirs:
            # print(dir)             #文件夹名
            print(os.path.join(root, dir))  # 把目录和文件名合成一个路径


def get_file(path):  # 获取文件路径
    file_path = []
    for root, dirs, files in os.walk(path):

        for file in files:
            # print(file)     #文件名
            # print()
            file_path.append(os.path.join(root, file))
    return file_path

path = r"D:\temp\abaqus_plugins\propellant"  # 文件夹路径
# list = get_dir(path)
list = get_file(path)

del_paths = [name for name in list if name.endswith('.pyc') or name.endswith('.py~')]
for del_path in del_paths:
    os.remove(del_path)
# print(list)