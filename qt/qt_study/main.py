# -*- coding:utf-8 -*-

'''
   @ 功能：
   @ author:Ming Liang
   @ create:
'''

import test_dialog_ex
import sys
from PyQt6.QtWidgets import *


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = test_dialog_ex.Ui_DialogEx()
    w.show()
    sys.exit(app.exec())