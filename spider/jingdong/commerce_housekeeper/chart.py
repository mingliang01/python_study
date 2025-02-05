
# 图形画布
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib  # 导入图表模块
import matplotlib.pyplot as plt # 导入绘图模块


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=0, height=0, dpi=100):
        # 避免中文乱码
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        matplotlib.rcParams['axes.unicode_minus'] = False
        # 创建图形
        fig = plt.figure(dpi=dpi)
        # 初始化图形画布
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)  # 设置父类

    # 显示商品分类饼图
    def pie_chart(self, size):
        """
        绘制饼图
        explode：设置各部分突出
        label:设置各部分标签
        labeldistance:设置标签文本距圆心位置，1.1表示1.1倍半径
        autopct：设置圆里面文本
        shadow：设置是否有阴影
        startangle：起始角度，默认从0开始逆时针转
        pctdistance：设置圆内文本距圆心距离
        返回值
        l_text：圆内部文本，matplotlib.text.Text object
        p_text：圆外部文本
        """
        label_list = [ '鼠标','键盘','U盘','移动硬盘','其它']  # 各部分标签
        plt.pie(size, labels=label_list,  labeldistance=1.1,
                autopct="%1.1f%%", shadow=False, startangle=30, pctdistance=0.6)
        plt.axis("equal")  # 设置横轴和纵轴大小相等，这样饼才是圆的



