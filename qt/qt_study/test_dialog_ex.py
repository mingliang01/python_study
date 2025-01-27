# -*- coding:utf-8 -*-

'''
   @ 功能：
   @ author:Ming Liang
   @ create:
'''

from test_dialog import Ui_Dialog

import warnings

warnings.filterwarnings('ignore')

from PyQt6.QtWidgets import *

import sys

class Ui_DialogEx(QWidget, Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.say)

    def say(self):
        # region QMessageBox
        QMessageBox.information(self, "提示", "这是一个信息消息。")
        QMessageBox.warning(self, "警告", "这是一个警告消息。")
        QMessageBox.critical(self, "错误", "这是一个错误消息。")
        QMessageBox.about(self, '关于', '这是关于软件的说明。。。')

        choice = QMessageBox.question(self, "问题", "是否继续？",
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if choice == QMessageBox.StandardButton.Yes:
            print("用户点击了'是'")
        else:
            print("用户点击了'否'")
        # endregion

        # region QInputDialog
        value, sure = QInputDialog.getInt(self, '输入整数', '值', min=0, max=20)
        if sure:
            print(value)

        value, sure = QInputDialog.getDouble(self, '输入小数', '值', min=0, max=20)
        if sure:
            print(value)

        value, sure = QInputDialog.getText(self, '输入字符串', '值', text='')
        if sure:
            print(value)

        value, sure = QInputDialog.getMultiLineText(self, '输入整数', '值', '')
        if sure:
            print(value)

        seasons = ['春', '夏', '秋', '东']
        value, sure = QInputDialog.getItem(self, '选择季节', '值', seasons, current=0,
                                           editable=False)  # 我这里不能写items=seasons，只能seasons，不然会报错，莫名其妙的
        if sure:
            print(value)
        # endregion

        # region QFileDialog
        dir_ = QFileDialog.getExistingDirectory(self, "选取文件夹", "C:/")  # 起始路径
        print(dir_)

        file_, _ = QFileDialog.getOpenFileName(self, "选取文件", "C:/",
                                               "All Files (*);;Text Files (*.txt)")  # 文件扩展名用双分号间隔
        print(file_)

        file_, _ = QFileDialog.getSaveFileName(self, "文件保存", "C:/", "All Files (*);;Text Files (*.txt)")
        print(file_)
        # endregion

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyApp()
    w.show()
    sys.exit(app.exec())