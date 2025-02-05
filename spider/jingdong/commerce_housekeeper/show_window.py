from window import Ui_MainWindow  # 导入主窗体类
from attention_window import Attention_MainWindow  # 导入关注窗体文件中的ui类
from heat_window import Heat_MainWindow  # 导入热卖排行榜窗体文件中的ui类
from evaluate_warning_window import Evaluate_Warning_MainWindow  # 导入评价预警窗体中的ui类
from price_warning_window import Price_Warning_MainWindow  # 导入价格预警窗体中的ui类
from about_window import About_MainWindow                  # 导入关于窗体ui类
# 导入Pyqt5
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys  # 导入系统模块

from mysql import MySQL  # 导入自定义数据库操作类
from crawl import Crawl  # 导入自定义爬虫类
mycrawl = Crawl()  # 创建爬虫类对象

mysql = MySQL() # 创建数据库对象
# 连接数据库
sql = mysql.connection_sql()
# 创建游标
cur = sql.cursor()


attention_info = ''  # 关注商品信息

from chart import PlotCanvas  # 导入自定义饼图类

import requests  # 网络请求


# 显示消息提示框，参数title为提示框标题文字，message为提示信息
def messageDialog(title, message):
    msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, title, message)
    msg_box.exec()


# 主窗体初始化类
class Main(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)

        # 获取热卖排行榜信息
        id_str = mycrawl.get_rankings_json('https://ch.jd.com/hotsale2?cateid=686')
        rankings_list = mycrawl.get_price(id_str)  # 获取价格，然后在该方法中将所有数据保存至列表并返回
        mysql.insert_ranking(cur, rankings_list, 'jd_ranking')  # 将数据插入数据库

    # 显示前10名
    def show_top10(self):
        top_10_info = mysql.query_top10_info(cur)  # 查询排行数据表前10名商品名称,价格，热卖指数
        # 行数标记
        i = -1
        for n in range(10):
            # x 确定每行显示的个数 0，1，2 每行2个
            x = n % 2
            # 当x为0的时候设置换行 行数+1
            if x == 0:
                i += 1
            # 创建布局
            self.widget = QtWidgets.QWidget()
            # 给布局命名
            self.widget.setObjectName("widget" + str(n))
            # 设置布局样式
            self.widget.setStyleSheet('QWidget#' + "widget" + str(
                n) + "{border:2px solid rgb(175, 175, 175);background-color: rgb(255, 255, 255);}")

            # 创建个Qlabel控件用于显示图片 设置控件在QWidget中
            self.label = QtWidgets.QLabel(self.widget)
            # 设置大小
            self.label.setGeometry(QtCore.QRect(15, 15, 160, 160))
            # 设置要显示的图片
            self.label.setPixmap(QtGui.QPixmap('img_download/' + str(n) + '.jpg'))
            # 图片显示方式 让图片适应QLabel的大小
            self.label.setScaledContents(True)
            # 给显示图片的label控件命名
            self.label.setObjectName("img_download" + str(n))
            # 设置控件样式
            self.label.setStyleSheet('border:2px solid rgb(175, 175, 175);')

            # 显示热卖指数的Label控件
            self.label_hot = QtWidgets.QLabel(self.widget)
            # 给热卖指数控件命名
            self.label_hot.setObjectName("hot" + str(n))
            self.label_hot.setGeometry(QtCore.QRect(24, 180, 141, 40))  # 设置控件位置及大小
            # 设置控件样式，边框与颜色
            self.label_hot.setStyleSheet("border: 2px solid rgb(255, 148, 61);color: rgb(255, 148, 61);")
            self.label_hot.setAlignment(QtCore.Qt.AlignCenter)  # 控件内文字居中显示
            self.label_hot.setText('热卖指数' + top_10_info[n][2])  # 显示热卖指数的文字
            font = QtGui.QFont()    # 创建字体对象
            font.setPointSize(18)   # 设置字体大小
            font.setBold(True)     # 开启粗体属性
            font.setWeight(75)     # 设置文字粗细
            self.label_hot.setFont(font) # 设置字体

            # 显示名称的Label控件
            self.label_name = QtWidgets.QLabel(self.widget)
            # 给显示名称控件命名
            self.label_name.setObjectName("hot" + str(n))
            # 设置控件位置及大小
            self.label_name.setGeometry(QtCore.QRect(185, 30, 228, 80))
            self.label_name.setText(top_10_info[n][0])  # 设置显示名称的文字
            # 左上角为主显示文字
            self.label_name.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
            self.label_name.setWordWrap(True)  # 设置文字自动换行
            font = QtGui.QFont()  # 创建字体对象
            font.setPointSize(9)  # 设置字体大小
            font.setBold(True)    # 开启粗体属性
            font.setWeight(75)    # 设置文字粗细
            self.label_name.setFont(font)   # 设置字体

            # 显示价格的Label控件
            self.label_price = QtWidgets.QLabel(self.widget)
            # 给显示价格控件命名
            self.label_price.setObjectName("price" + str(n))
            # 设置控件位置及大小
            self.label_price.setGeometry(QtCore.QRect(200, 80, 228, 80))
            # 设置控件样式
            self.label_price.setStyleSheet("color: rgb(255, 0, 0);")
            self.label_price.setText('￥' + top_10_info[n][1])  # 设置显示的价格文字
            font = QtGui.QFont()    # 创建字体对象
            font.setPointSize(20)   # 设置字体大小
            font.setBold(True)     # 开启粗体属性
            font.setWeight(75)     # 设置文字粗细
            self.label_price.setFont(font)   # 设置字体

            # 显示关注按钮控件
            self.pushButton = QtWidgets.QPushButton(self.widget)
            # 给显示价格控件命名
            self.pushButton.setObjectName(str(n))
            # 设置控件位置及大小
            self.pushButton.setGeometry(QtCore.QRect(300, 160, 100, 50))
            font = QtGui.QFont()     # 创建字体对象
            font.setFamily("楷体")   # 设置字体
            font.setPointSize(18)    # 设置字体大小
            font.setBold(True)      # 开启粗体属性
            font.setWeight(75)      # 设置文字粗细
            self.pushButton.setFont(font)   # 设置字体
            # 设置关注按钮控件样式
            self.pushButton.setStyleSheet("background-color: rgb(223, 48, 51);color: rgb(255, 255, 255);")
            self.pushButton.setText('关注')   # 设置关注按钮显示的文字
            # 注册关注按钮信号槽
            self.pushButton.clicked.connect(self.attention_btn)
            # 把动态创建的widegt布局添加到gridLayout中 i，x分别代表：行数以及每行的个数
            self.gridLayout.addWidget(self.widget, i, x)
            # 设置高度为动态高度根据 行数确定高度 每行300
        self.scrollAreaWidgetContents.setMinimumHeight((i+1) * 240)
        # 设置网格布局控件动态高度
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 850, ((i+1) * 240)))

    # 关注按钮事件
    def attention_btn(self):
        # 获取信号源 点击的按钮
        sender = self.gridLayout.sender()
        global attention_info
        # 因为创建关注按钮对象名称是以0为起始，最后一个关注按钮为9，
        # 所以用单击按钮的对象名称+1作为数据库中的id
        attention_info = mysql.query_id_info(cur, int(sender.objectName()) + 1)
        # 将商品名称显示在关注窗体的编辑框内
        attention.lineEdit.setText(attention_info[0])
        attention.open()  # 显示关注窗体

    # 显示商品分类比例饼图
    def show_classification(self):
        name_all = mysql.query_rankings_name(cur, 'jd_ranking')  # 获取排行榜中所有商品名称
        name_number = len(name_all)  # 排行榜中所有商品数量
        number = 0   # 定义统计分类数量的变量
        remove_list = []  # 保存需要移除的商品名称
        class_list = []  # 保存所有分类比例数据列表
        # 因为鼠标垫与鼠标名称接近，所以先移除鼠标垫
        for name in name_all:
            if '鼠标垫' in name:
                remove_list.append(name)
        for r_name in remove_list:
            name_all.remove(r_name)

        # 获取鼠标占有比例
        for name in name_all:
            if '鼠标' in name:
                number += 1
        # 计算鼠标百分比
        mouse_ratio = float('%.1f' % ((number / name_number) * 100))
        class_list.append(mouse_ratio)
        # 获取键盘占有比例
        number = 0
        for name in name_all:
            if '键盘' in name:
                number += 1
        # 计算键盘百分比
        keyboard_ratio = float('%.1f' % ((number / name_number) * 100))
        class_list.append(keyboard_ratio)
        # 获取U盘占有比例
        number = 0
        for name in name_all:
            if 'U盘' in name or 'u盘' in name:
                number += 1
        # 计算U盘百分比
        u_ratio = float('%.1f' % ((number / name_number) * 100))
        class_list.append(u_ratio)
        # 获取移动硬盘占有比例
        number = 0
        for name in name_all:
            if '移动硬盘' in name:
                number += 1
        # 计算移动硬盘百分比
        move_ratio = float('%.1f' % ((number / name_number) * 100))
        class_list.append(move_ratio)
        # 计算其他百分比
        other_ratio = float('%.1f' % (100 - (mouse_ratio + keyboard_ratio + u_ratio + move_ratio)))
        class_list.append(other_ratio)
        pie = PlotCanvas()  # 创建饼图类对象
        pie.pie_chart(class_list)  # 调用显示饼图的方法
        self.horizontalLayout.addWidget(pie)  # 将饼图添加在主窗体的水平布局当中

    # 显示已经关注的商品名称
    def show_attention_name(self):
        self.name_list= []
        # 查询已经关注的商品信息
        row, column, results = mysql.query_evaluate_info(cur,'attention')
        if row !=0:
            for index,i in enumerate(results):
                self.name_list.append('关注商品'+str(index+1)+':\n'+i[1])  # 将关注商品名称添加至名称列表中
            # 设置字体
            font = QtGui.QFont()
            font.setPointSize(12)
            self.listView.setFont(font)
            # 设置列表内容不可编辑
            self.listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            self.listView.setWordWrap(True)  # 自动换行
            model = QtCore.QStringListModel()  # 创建字符串列表模式
            model.setStringList(self.name_list)  # 设置字符串列表
            self.listView.setModel(model)  # 设置模式
        else:
            model = QtCore.QStringListModel()  # 创建字符串列表模式
            model.setStringList(self.name_list)  # 设置字符串列表
            self.listView.setModel(model)  # 设置模式

    # 更新预警信息按钮的单击事件处理方法
    def up(self):
        warningDialog = QtWidgets.QMessageBox.warning(self,
                                                      '警告', '关注商品的预警信息更新后，将以新的信息进行对比并预警！',
                                                      QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if warningDialog == QtWidgets.QMessageBox.Yes:
            # 查询已经关注的商品信息
            row, column, results = mysql.query_evaluate_info(cur,'attention')
            if row !=0:
                jd_id_str = ''
                for i in range(len(results)):
                    jd_id = 'J_' + results[i][3] + ','
                    jd_id_str = jd_id_str + jd_id
                price_url = 'http://p.3.cn/prices/mgets?type=1&skuIds={id_str}'
                response = requests.get(price_url.format(id_str=jd_id_str))  # 获取关注商品的价格
                price_json = response.json()  # 获取价格json数据，该数据为list类型
                for index, item in enumerate(results):
                    # 获取中评最新的时间,由于返回的关注商品信息中包含行与列信息所有进行i+2
                    middle_time = mycrawl.get_evaluation(2, item[3])
                    # 获取差评最新的时间
                    poor_time = mycrawl.get_evaluation(1, item[3])
                    price = price_json[index]['p']
                    up = "middle_time='{mi_time}',poor_time='{p_time}',jd_price='{price}'".format(
                        mi_time=middle_time,
                        p_time=poor_time, price=price)
                    # 更新关注商品的预警信息
                    mysql.update_attention(cur, 'attention', up, results[index][0])
                messageDialog('提示！','已更新预警信息！')
            else:
                messageDialog('警告！','您并没有关注某件商品！')
    def close_main(self):
        mysql.close_sql()  # 关掉数据库连接
        self.close()       # 关掉窗体

# 关注窗体初始化类
class Attention(QMainWindow, Attention_MainWindow):
    def __init__(self):
        super(Attention, self).__init__()
        self.setupUi(self)
        # 开启自动填充背景
        self.centralwidget.setAutoFillBackground(True)
        palette = QtGui.QPalette()  # 调色板类
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(
            QtGui.QPixmap('img_resources/attention_bg.png')))  # 设置背景图片
        self.centralwidget.setPalette(palette)  # 为控件设置对应的调色板即可
        # 设置背景透明
        self.pushButton_yes.setStyleSheet("background-color:rgba(0,0,0,0)")
        # 设置确认关注按钮的背景图片
        self.pushButton_yes.setIcon(QtGui.QIcon('img_resources/yes_btn.png'))
        # 设置按钮背景图大小
        self.pushButton_yes.setIconSize(QtCore.QSize(100, 50))
        # 设置背景透明
        self.pushButton_no.setStyleSheet("background-color:rgba(0,0,0,0)")
        # 设置确认关注按钮的背景图片
        self.pushButton_no.setIcon(QtGui.QIcon('img_resources/no_btn.png'))
        # 设置按钮背景图大小
        self.pushButton_no.setIconSize(QtCore.QSize(100, 50))

    # 打开关注窗体
    def open(self):
        self.show()

    def insert_attention_message(self, attention_info):
        is_identical = mysql.query_is_name(cur, attention_info[0])  # 判断数据库中是否已经关注了该商品
        if is_identical == 0:
            middle_time = mycrawl.get_evaluation(2, attention_info[2])
            poor_time = mycrawl.get_evaluation(1, attention_info[2])
            # 判断信息状态
            if middle_time != None and poor_time != None:
                attention_info = attention_info + (middle_time, poor_time)  # 将评价时间添加至商品数据中
                mysql.insert_attention(cur, [attention_info], 'attention')  # 插入关注信息
                messageDialog('提示！', '已关注' + attention_info[0])  # 提示
                attention.close()  # 关闭关注对话框
                main.show_attention_name() # 显示关注商品的名称
            else:
                print('无法获取评价时间！')
        else:
            messageDialog('警告！', '不可以关注相同的商品！')
            attention.close()
# 取消关注窗体初始化类
class Cancel_Attention(QMainWindow, Attention_MainWindow):
    def __init__(self):
        super(Cancel_Attention, self).__init__()
        self.setupUi(self)
        # 开启自动填充背景
        self.centralwidget.setAutoFillBackground(True)
        palette = QtGui.QPalette()  # 调色板类
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(
            QtGui.QPixmap('img_resources/cancel_attention_bg.png')))  # 设置背景图片
        self.centralwidget.setPalette(palette)  # 为控件设置对应的调色板即可
        # 设置背景透明
        self.pushButton_yes.setStyleSheet("background-color:rgba(0,0,0,0)")
        # 设置确认关注按钮的背景图片
        self.pushButton_yes.setIcon(QtGui.QIcon('img_resources/yes_btn.png'))
        # 设置按钮背景图大小
        self.pushButton_yes.setIconSize(QtCore.QSize(100, 50))
        # 设置背景透明
        self.pushButton_no.setStyleSheet("background-color:rgba(0,0,0,0)")
        # 设置确认关注按钮的背景图片
        self.pushButton_no.setIcon(QtGui.QIcon('img_resources/no_btn.png'))
        # 设置按钮背景图大小
        self.pushButton_no.setIconSize(QtCore.QSize(100, 50))

    # 显示取消关注的窗体
    def open(self,qModeIndex):
        # 在关注商品名称列表中，获取单击了哪一个商品的名称
        name = main.name_list[qModeIndex.row()].lstrip('关注商品'+str(qModeIndex.row()+1)+':\n')
        # 将商品名称显示在关注窗体的编辑框内
        cancel_attention.lineEdit.setText(name)
        cancel_attention.show()  # 显示关注窗体

    #  取消关注的方法
    def unfollow(self):
        # 获取编辑框内的商品名称
        name = cancel_attention.lineEdit.text()
        mysql.delete_attention(cur,name)
        main.show_attention_name()     # 显示关注商品名称列表
        cancel_attention.close()       # 关掉取消关注的窗体


# 热卖榜窗体初始化类
class Heat(QMainWindow, Heat_MainWindow):
    def __init__(self):
        super(Heat, self).__init__()
        self.setupUi(self)
        # 开启自动填充背景
        self.centralwidget.setAutoFillBackground(True)
        palette = QtGui.QPalette()  # 调色板类
        palette.setBrush(QtGui.QPalette.Background,
                         QtGui.QBrush(QtGui.QPixmap('img_resources/rankings_bg.png')))  # 设置背景图片
        self.centralwidget.setPalette(palette)  # 为控件设置对应的调色板即可
        # 获取热卖排行榜数据信息
        row, column, results = mysql.query_rankings(cur, 'jd_ranking')
        # 设置表格内容不可编辑
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.verticalHeader().setHidden(True)  # 隐藏行号
        self.tableWidget.setRowCount(row)  # 根据数据库内容设置表格行
        self.tableWidget.setColumnCount(column)  # 设置表格列
        # 设置表格头部
        self.tableWidget.setHorizontalHeaderLabels(['排名', '商品名称', '京东价', '京东id','热卖指数'])
        self.tableWidget.setStyleSheet("background-color:rgba(0,0,0,0)")  # 设置背景透明
        # 根据窗体大小拉伸表格
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeToContents)
        for i in range(row):
            for j in range(column):
                temp_data = results[i][j]  # 临时记录，不能直接插入表格
                data = QtWidgets.QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                self.tableWidget.setItem(i, j, data)               # 设置表格显示的数据

    # 打开热卖榜窗体
    def open(self):
        self.show()

    # 热卖榜窗体双击事件处理方法
    def heat_itemDoubleClicked(self):
        item = self.tableWidget.currentItem()  # 表格item对象
        # 判断是否是商品名称的列
        if item.column() == 1:
            # 将商品名称显示在关注窗体的编辑框内
            attention.lineEdit.setText(item.text())
            global attention_info
            # 查询需要关注商品的信息
            attention_info = mysql.query_id_info(cur, item.row() + 1)
            attention.open()  # 显示关注窗体

# 评价预警窗体初始化类
class Evaluate_Warning(QMainWindow, Evaluate_Warning_MainWindow):
    def __init__(self):
        super(Evaluate_Warning, self).__init__()
        self.setupUi(self)


    def open_warning(self):
        # 开启自动填充背景
        self.centralwidget.setAutoFillBackground(True)
        palette = QtGui.QPalette()  # 调色板类
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QtGui.QPixmap('img_resources/evaluate_warning_bg.png')))  # 设置背景图片
        self.centralwidget.setPalette(palette)  # 为控件设置对应的调色板即可
        warning_list = []  # 保存评价分析后得数据
        # 查询关注商品的信息
        row, column, results = mysql.query_evaluate_info(cur, 'attention')
        # 设置表格内容不可编辑
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.verticalHeader().setHidden(True)  # 隐藏行号
        self.tableWidget.setRowCount(row)  # 根据数据库内容设置表格行
        self.tableWidget.setColumnCount(column-4)  # 设置表格列
        # 分别设置列宽度
        self.tableWidget.setColumnWidth(0,600)
        self.tableWidget.setColumnWidth(1,140)
        self.tableWidget.setColumnWidth(2,140)
        self.tableWidget.setStyleSheet("background-color:rgba(0,0,0,0)")  # 设置背景透明

        # 判断是否有关注商品的信息
        if row != 0:
            middle_time = ''
            poor_time = ''
            for i in range(len(results)):
                # 获取热卖指数与中评最新的时间
                new_middle_time = mycrawl.get_evaluation(2,results[i][3])
                # 获取差评最新的时间
                new_poor_time = mycrawl.get_evaluation(1,results[i][3])
                if results[i][5] == new_middle_time:
                    middle_time = '无'
                else:
                    middle_time = '有'
                if results[i][6] == new_poor_time:
                    poor_time = '无'
                else:
                    poor_time = '有'
                warning_list.append((results[i][1], middle_time, poor_time))
            for i in range(len(results)):
                for j in range(3):
                    temp_data = warning_list[i][j]  # 临时记录，不能直接插入表格
                    data = QtWidgets.QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                    data.setTextAlignment(QtCore.Qt.AlignCenter)
                    evaluate.tableWidget.setItem(i, j, data)
            self.show()  # 显示窗体
        else:
            messageDialog('警告！', '您并没有关注某件商品！')


# 价格预警窗体初始化类
class Price_Warning(QMainWindow, Price_Warning_MainWindow):
    def __init__(self):
        super(Price_Warning, self).__init__()
        self.setupUi(self)

    # 价格信息处理
    def open_price(self):
        # 开启自动填充背景
        self.centralwidget.setAutoFillBackground(True)
        palette = QtGui.QPalette()  # 调色板类
        palette.setBrush(QtGui.QPalette.Background,
                         QtGui.QBrush(QtGui.QPixmap('img_resources/price_warning_bg.png')))  # 设置背景图片
        self.centralwidget.setPalette(palette)  # 为控件设置对应的调色板即可
        price_list = []  # 保存价格分析后的数据
        # 查询关注商品的信息
        row, column, results = mysql.query_evaluate_info(cur, 'attention')
        # 设置表格内容不可编辑
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.verticalHeader().setHidden(True)  # 隐藏行号
        self.tableWidget.setRowCount(row)  # 根据数据库内容设置表格行
        self.tableWidget.setColumnCount(column - 5)  # 设置表格列
        # 分别设置列宽度
        self.tableWidget.setColumnWidth(0, 600)
        self.tableWidget.setColumnWidth(1, 140)
        self.tableWidget.setStyleSheet("background-color:rgba(0,0,0,0)")  # 设置背景透明
        # 判断是否有关注的商品信息
        if row != 0:
            jd_id_str = ''
            for i in range(len(results)):
                jd_id = 'J_' + results[i][3] + ','
                jd_id_str = jd_id_str + jd_id
            price_url = 'http://p.3.cn/prices/mgets?type=1&skuIds={id_str}'
            response = requests.get(price_url.format(id_str=jd_id_str))  # 获取关注商品的价格
            price_json = response.json()  # 获取价格json数据，该数据为list类型
            change = ''
            for index, item in enumerate(price_json):
                # 京东价格
                new_jd_price = item['p']
                if float(results[index][2]) < float(new_jd_price):
                    change = '上涨'
                if float(results[index][2]) == float(new_jd_price):
                    change = '无'
                if float(results[index][2]) > float(new_jd_price):
                    change = '下浮'
                price_list.append((results[index][1], change))
            for i in range(len(results)):
                for j in range(2):
                    temp_data = price_list[i][j]  # 临时记录，不能直接插入表格
                    data = QtWidgets.QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                    data.setTextAlignment(QtCore.Qt.AlignCenter)
                    price.tableWidget.setItem(i, j, data)
            self.show()
        else:
            messageDialog('警告！', '您并没有关注某件商品！')


# 关于窗体初始化类
class About_Window(QMainWindow, About_MainWindow):
    def __init__(self):
        super(About_Window, self).__init__()
        self.setupUi(self)
        img = QtGui.QPixmap('img_resources/about_bg.png')  # 打开顶部位图
        self.label.setPixmap(img)  # 设置位图


if __name__ == '__main__':
    app = QApplication(sys.argv) # 创建QApplication对象，作为GUI主程序入口
    main = Main()   # 创建主窗体对象
    # 关注窗体对象
    attention = Attention()
    # 取消关注窗体对象
    cancel_attention = Cancel_Attention()
    # 热卖排行榜窗体对象
    heat = Heat()
    # 评价预警窗体对象
    evaluate = Evaluate_Warning()
    # 价格预警窗体对象
    price = Price_Warning()
    # 关于窗体对象
    about = About_Window()
    main.show()
    main.show_top10()           # 显示前10名热卖榜图文信息
    main.show_classification()  # 显示商品分类比例饼图
    main.show_attention_name()  # 显示关注商品名称
    # 指定关注窗体按钮(是)单击事件处理方法
    attention.pushButton_yes.clicked.connect(
        lambda: attention.insert_attention_message(attention_info))
    # 指定关注窗体按钮（否）单击事件处理方法
    attention.pushButton_no.clicked.connect(attention.close)
    # 指定销量榜表格的双击事件处理方法
    heat.tableWidget.itemDoubleClicked.connect(heat.heat_itemDoubleClicked)
    # 指定打开热卖排行榜窗体的事件处理方法
    main.action_heat.triggered.connect(heat.open)
    # 指定打开关注商品评价预警窗体的事件处理方法
    main.action_evaluate.triggered.connect(evaluate.open_warning)
    # 指定打开关注商品价格预警窗体的事件处理方法
    main.action_price.triggered.connect(price.open_price)
    # 指定打开更新关注商品信息的对话框
    main.action_up.triggered.connect(main.up)
    # 指定显示关注商品名称列表事件
    main.listView.clicked.connect(cancel_attention.open)
    # 指定取消关注窗体按钮（是）单击事件处理方法
    cancel_attention.pushButton_yes.clicked.connect(cancel_attention.unfollow)
    # 指定取消关注窗体按钮（否）单击事件处理方法
    cancel_attention.pushButton_no.clicked.connect(cancel_attention.close)
    # 指定关于事件处理方法
    main.action_about.triggered.connect(about.show)
    # 指定退出事件处理方法
    main.action_out.triggered.connect(main.close_main)
    sys.exit(app.exec_())
