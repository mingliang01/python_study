# -*- coding:utf-8 -*-

'''
   @ 功能：
   @ author:Ming Liang
   @ create:
'''

from window_ex import *
from get_stations import *
import os
import inspect

if __name__ == "__main__":
    # 更改工作目录
    current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    os.chdir(current_dir)
    print("新的工作目录:", os.getcwd())
    getStation()  # 下载所有车站文件
    show_MainWindow()  # 调用显示窗体的方法