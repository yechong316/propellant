# -- encoding:utf-8 --
#!/usr/bin/python3
# propellant_v0125-1100 
# Authorn:Jaime Lannister
# Time:2019/1/29-22:26
# -- encoding:utf-8 --
import tkinter as tk
GUI = tk.Tk()            # 创建父容器GUI
GUI.title("Serial Tool") # 父容器标题
GUI.geometry("460x380")  # 设置父容器窗口初始大小，如果没有这个设置，窗口会随着组件大小的变化而变化

Information = tk.LabelFrame(GUI, text="操作信息", padx=10, pady=10) # 创建子容器，水平，垂直方向上的边距均为10
Information.place(x=20, y=20)
Information_Window = scrolledtext.ScrolledText(Information, width=20, height=5, padx=10, pady=10,wrap=tk.WORD)
Information_Window.grid()
