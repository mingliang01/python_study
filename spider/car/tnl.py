# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import time
import urllib
import urllib.request
import os
from bs4 import BeautifulSoup
from PIL import Image


# 获取汽车图片方法类
class ReTbmm():
    def Retbmm(self):
        # 爬虫开始时间
        start = time.time()
        # 用于返回当前工作目录。
        self.cdir = os.getcwd()
        # 爬取的网址：https://www.autohome.com.cn/spec/32890/?pvareaid=2023562
        # 车身外观
        url1 = 'https://car.autohome.com.cn/pic/series-s32890/385-1.html#pvareaid=2023594'
        # 中控方向盘
        url2 = 'https://car.autohome.com.cn/pic/series-s32890/385-10.html#pvareaid=2023594'
        # 车厢座椅
        url3 = 'https://car.autohome.com.cn/pic/series-s32890/385-3.html#pvareaid=2023594'
        # 其它细节
        url4 = 'https://car.autohome.com.cn/pic/series-s32890/385-12.html#pvareaid=2023594'
        self.getImg('车身外观', url1)
        self.getImg('中控方向盘', url2)
        self.getImg('车厢座椅', url3)
        self.getImg('其它细节', url4)
        end = time.time()
        # 输出运行时间
        print("run time:" + str(end - start))
    # 下载图片方法
    def getImg(self, name, urls):
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240'
        headers = {'User-Agent': user_agent}
        # 访问连接
        request = urllib.request.Request(urls, headers=headers)
        # # 获取数据
        response = urllib.request.urlopen(request)
        # 解析数据
        bsObj = BeautifulSoup(response, 'html.parser')
        # 查找所有img标记
        t1 = bsObj.find_all('img')
        for t2 in t1:
            t3 = t2.get('src')
            print(t3)
        # 创建图片路径
        path = self.cdir + '/mrsoft/' + str(name)
        # 读取路径
        if not os.path.exists(path):
            # 根据路径建立图片文件夹
            os.makedirs(path)
        # 每次调用初始化图片序号
        n = 0
        # 循环图片集合
        for img in t1:
            # 每次图片顺序加1
            n = n + 1
            # 获取图片路径
            link = img.get('src')
            # 判断图片路径是否纯在
            if link:
                # 拼接图片链接
                s = "http:" + str(link)
                # 分离文件扩展名
                i = link[link.rfind('.'):]
                try:
                    # 访问图片链接
                    request = urllib.request.Request(s)
                    # 获取返回事件
                    response = urllib.request.urlopen(request)
                    # 读取返回内容
                    imgData = response.read()
                    # 创建文件
                    pathfile = path + r'/' + str(n) + i
                    # 打开文件
                    with open(pathfile, 'wb') as f:
                        # 图片写入文件
                        f.write(imgData)
                        # 图片写入完成关闭文件
                        f.close()
                        print("thread " + name + " write:" + pathfile)
                except:
                    print(str(name) + " thread write false:" + s)
# 第二个页面
# 创建窗口类，继承object
class Ui_Form(object):
    # 初始化窗体方法
    def setupUi(self, Form):
        # 设置窗口名
        Form.setObjectName("Form")
        # 设置窗口大小
        Form.resize(1300, 900)
        # 创建一个滑动控件，并加入到窗口Form中
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(20, 70, 181, 800))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 179, 800))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.treeView = QTreeWidget(self.scrollAreaWidgetContents)
        self.treeView.setGeometry(QtCore.QRect(0, 0, 181, 761))
        self.treeView.setObjectName("treeView")
        self.treeView.setHeaderLabel('爬虫爬出的结果')
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        # 创建一个竖向布局容器，并加入到窗口Form中
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        # 创建一个滑动控件，并加入到窗口Form中
        self.scrollArea_2 = QtWidgets.QScrollArea(Form)
        self.scrollArea_2.setGeometry(QtCore.QRect(200, 70, 1000, 800))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        # 创建一个网格布局，并加入到窗口scrollAreaWidgetContents_2中
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        # 创建一个按钮，并将按钮加入到窗口Form中
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 161, 41))
        self.pushButton.setObjectName("pushButton")
        # 创建一个滑动按钮，并将按钮加入到窗口Form中
        self.pushButton1 = QtWidgets.QPushButton(Form)
        self.pushButton1.setGeometry(QtCore.QRect(20, 20, 161, 41))
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton1.setVisible(False)
        # 开启方法
        self.retranslateUi(Form)
        # 关联信号槽
        QtCore.QMetaObject.connectSlotsByName(Form)

    # UI设置方法 设置ui属性
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        # 设置窗体名称
        Form.setWindowTitle(_translate("Form", "明日科技"))
        # 设置按钮显示文字
        self.pushButton.setText(_translate("Form", "阿斯顿·马丁 汽车图片"))
        # 设置按钮显示文字
        self.pushButton1.setText(_translate("Form", "搜索完成"))
        # 为按钮添加点击事件
        self.pushButton.clicked.connect(self.btnstate)
        # 获取树像结构根节点
        self.root = QTreeWidgetItem(self.treeView)
        # 在跟节点中添加数据
        self.root.setText(0, 'V8 Vantage 2018款 4.0T V8')

    # 搜索方法
    def btnstate(self):
        # 开始搜索 隐藏按钮
        self.pushButton.setVisible(False)
        # 实例化爬虫类
        ui = ReTbmm()
        # 开启爬虫方法
        ui.Retbmm()
        # 显示已完成按钮
        self.pushButton1.setVisible(True)
        # 设置文件夹路径 为了树形结构做准备
        self.path = cdir + '/mrsoft'
        # 查找路径下的所有文件名称
        dirs = os.listdir(self.path)
        # 循环文件名称
        for dir in dirs:
            # 添加文件名称到树形结构
            QTreeWidgetItem(self.root).setText(0, dir)
        self.treeView.clicked.connect(self.onTreeClicked)

    #  树形结构点击后在这里处理
    def onTreeClicked(self, Qmodelidx):
        # 获取点击的树形结构
        items = self.treeView.currentItem()
        # 判断单击的节点
        if items.text(0) == 'V8 Vantage 2018款 4.0T V8':
            # 单机的主节点在这里出来
            # 删除节点root下的子节点
            self.root.takeChildren()
            # 获取路径下的所有文件
            dirs = os.listdir(self.path)
            # 循环文件
            for dir in dirs:
                # 设置子节点
                QTreeWidgetItem(self.root).setText(0, dir)
            # 注册点击事件
            self.treeView.clicked.connect(self.onTreeClicked)
            pass
        else:
            # 每次点循环删除管理器的组件
            while self.gridLayout.count():
                # 获取第一个组件
                item = self.gridLayout.takeAt(0)
                # 删除组件
                widget = item.widget()
                widget.deleteLater()
            # 每次点击 树形结构把图片集合清空
            filenames = []
            # 根据路径查找文件夹下所有文件 ，循环文件夹下文件名称
            for filename in os.listdir(cdir + '/mrsoft/' + items.text(0)):  # listdir的参数是文件夹的路径
                # 把名称添加到集合中
                filenames.append(filename)
            # 行数标记
            i = -1
            # 根据图片的数量进行循环
            for n in range(len(filenames)):
                # x 确定每行显示的个数 0，1，2 每行3个
                x = n % 3
                # 当x为0的时候设置换行 行数+1
                if x == 0:
                    i += 1
                # 创建布局
                self.widget = QWidget()
                # 设置布局大小
                self.widget.setGeometry(QtCore.QRect(110, 40, 200, 200))
                # 给布局命名
                self.widget.setObjectName("widget" + str(n))
                # 创建个Qlabel控件用于显示图片 设置控件在QWidget中
                self.label = QLabel(self.widget)
                # 设置大小
                self.label.setGeometry(QtCore.QRect(0, 0, 350, 300))
                # 设置要显示的图片
                self.label.setPixmap(QPixmap(self.path + '/' + items.text(0) + '/' + filenames[n]))
                # 图片显示方式 让图片适应QLabel的大小
                self.label.setScaledContents(True)
                # 给图片控件命名
                self.label.setObjectName("label" + str(n))
                # 创建按钮 用于点击后放大图 设置按钮在QWidget中
                self.commandLinkButton = QCommandLinkButton(self.widget)
                # 设置按钮位置
                self.commandLinkButton.setGeometry(QtCore.QRect(0, 0, 111, 41))
                # 给按钮命名
                self.commandLinkButton.setObjectName("label" + str(n))
                # 设置按钮上显示文字
                self.commandLinkButton.setText(filenames[n])
                # # 注册信号槽 使用lambda 传递参数给方法
                self.commandLinkButton.clicked.connect(lambda: self.wichbtn(self.path + '/' + items.text(0) + '/'))
                # self.commandLinkButton.objectName()
                # 吧动态添加的widegt布局添加到gridLayout中 i，x分别代表：行数以及每行的个数
                self.gridLayout.addWidget(self.widget, i, x)
            # 设置上下滑动控件可以滑动 把scrollAreaWidgetContents_2添加到scrollArea中
            self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
            self.verticalLayout.addWidget(self.scrollArea_2)
            # 设置scrollAreaWidgetContents_2最大宽度 为 scrollArea_2宽度 可以都显示下来不用左右滑动
            self.scrollAreaWidgetContents_2.setMinimumWidth(800)
            # 设置高度为动态高度根据 行数确定高度 每行500
            self.scrollAreaWidgetContents_2.setMinimumHeight(i * 300)

    # 信号槽 点击按钮显示大图功能
    def wichbtn(self, tppath):
        # 获取信号源 点击的按钮
        sender = self.gridLayout.sender()
        print('信号源',sender.objectName())
        # 使用电脑中的看图工具打开图片
        img = Image.open(tppath + sender.text())
        img.show()

# 第一个页面
class FirstWindow(QWidget):
    def __init__(self):
        super().__init__()
        # 设置标题
        self.setWindowTitle("登录")
        self.textfield()
        self.center()

    # 初始化位置
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # 初始化页面
    def textfield(self):
        QToolTip.setFont(QFont('SansSerif', 12))
        user = QLabel("用户名(mingri):")
        self.userEdit = QLineEdit()
        self.userEdit.setToolTip("请输入你的帐号")

        passWord = QLabel("密码(666666):")
        self.passWordEdit = QLineEdit()
        self.passWordEdit.setToolTip("请输入你的密码")

        grid = QGridLayout()
        grid.setSpacing(0)

        grid.addWidget(user, 0, 0)
        grid.addWidget(self.userEdit, 1, 0)
        grid.addWidget(passWord, 2, 0)
        grid.addWidget(self.passWordEdit, 3, 0)
        empty = QLabel()
        grid.addWidget(empty, 4, 0)

        btn_logon = QPushButton("登录")
        btn_quit = QPushButton("退出")
        grid.addWidget(btn_logon, 5, 0, 1, 2)
        grid.addWidget(btn_quit, 6, 0, 1, 2)
        # 登录按钮绑定单击事件
        btn_logon.clicked.connect(self.onclick)
        # 退出按钮
        btn_quit.clicked.connect(quit)
        self.setLayout(grid)
    # 登录按钮单击事件
    def onclick(self):
        if self.userEdit.text()=="mingri":
            if self.passWordEdit.text()=='666666':
                ex.close()
                MainWindow.show()
            else:
                self.passWordEdit.setText('密码错误请重新输入')
        else:
            self.userEdit.setText('账号错误请重新输入')

# 程序主方法
if __name__ == '__main__':
    App = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    # 初始化第二个窗体
    ui = Ui_Form()
    # 获取文件的路径
    cdir = os.getcwd()
    # 调用创建窗体方法
    ui.setupUi(MainWindow)
    # 初始化第一个页面
    ex = FirstWindow()
    # 显示第一个页面
    ex.show()
    sys.exit(App.exec_())



