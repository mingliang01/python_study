
import requests_html     # 网络请求模块
from pymysql import *    # 数据库操作模块
import random            # 随机数模块
import time              # 时间模块
import os                # 导入系统模块



info_url = []             # 保存所有详情页请求地址
# 主页地址
url = 'https://detail.zol.com.cn/cell_phone_index/subcate57_0_list_1000-1999_0_1_2_0_{page}.html'
session = requests_html.HTMLSession()     # 创建会话对象
# 创建connection连接mysql数据库
conn = connect(host='localhost', port=3306, database='cellphone_data', user='root',
               password='1234', charset='utf8')
#创建cursor对象
cs1 = conn.cursor()

# 获取随机请求头信息
def get_header():
        headers = ['Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
                   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
                   'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16',
                   'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1']
        ua = random.choice(headers)     # 随机抽取一个请求头信息
        header = {'User-Agent':ua}      # 组合请求头信息
        return header  # 返回请求头信息


# 获取详情页的请求地址
def get_info_url(url, page):
    header = get_header()        # 获取随机请求头信息
    url = url.format(page=page)  # 替换切换页面的url
    response = session.get(url=url,headers=header)  # 发送网络请求
    html = requests_html.HTML(html=response.text)    # 解析html
    # 将获取到的详情页请求地址，追加到列表中
    info_url.extend(html.xpath('//a[@class="pic"]/@href'))

# 向数据库中插入数据
def sql_insert(data):
    # 执行sql语句
    query = f'insert into phone (title,price,subtitle,img_url,cpu,rear_camera,front_camera,memory,battery,screen,resolving_power)' \
            f'values(%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s)'
    # 插入的值
    values = (data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10])
    cs1.execute(query, values)   # 执行sql语句
    # 提交之前的操作，如果之前已经执行多次的execute，那么就都进行提交
    conn.commit()


# 获取每个详情页中的信息
def get_info(dir_name,infos):
    for i in infos:         # 遍历所有的详情页地址
        try:
            header = get_header()      # 循环一次 获取一个随机请求头信息
            url = "https://detail.zol.com.cn/" + i    # 拼接url地址
            print(url)
            response = session.get(url=url, headers=header)  # 发送详情页的网络请求
            # 获取主标题（手机品牌基本配置）
            title = response.html.xpath('//h1[@class="product-model__name"]/text()')[0]
            # 获取参考价格
            price = response.html.xpath('//b[@class="price-type"]/text()')[0]
            # 获取副标题（手机特点）
            subtitle = response.html.xpath('//div[@class="product-model__subtitle"]/text()')[0]
            # 封面图地址
            img_url = response.html.xpath('//img[@id="big-pic"]/@src')[0]
            # 根据属性值获取所有参数对应的标签
            parameter = response.html.xpath('//*[@class="product-link"]/text()')
            print(title,price,subtitle,img_url,parameter)
            # cpu
            cpu = parameter[0]
            # 后置摄像头
            rear_camera =parameter[1]
            # 前置摄像头
            front_camera = parameter[2]
            # 内存
            memory = parameter[3]
            # 电池
            battery = parameter[4]
            # 屏幕
            screen = parameter[5]
            # 分辨率
            resolving_power = parameter[6]
            title = title.replace('/',' ')        # 将标题中特殊符号替换
            download_img(dir_name,title,img_url)  # 下载图片
            # 将数据插入数据库当中
            sql_insert([title,price,subtitle,img_url,cpu,rear_camera,front_camera,memory,battery,screen,resolving_power])
            #产生一个2~3的随机数字
            t = random.randint(2,3)
            print("数据已插入等待", t, "秒！")
            time.sleep(t)          # 随机等待时间
        except Exception as e:
            print("错误",e)
            continue              # 出现异常跳过当前循环，让爬虫继续爬取下一个页面

# 下载图片
def download_img(dir_name, img_name, img_url):
    if os.path.exists(dir_name):    # 判断文件夹是否存在
        header = get_header()       # 获取随机请求头
        # 想图片地址发送网络请求
        img_response = session.get(url=img_url,headers=header)
        # 通过open函数，将图片二进制数据写入文件夹当中
        open(dir_name + "/" + img_name + ".jpg", "wb").write(img_response.content)
    else:                       # 没有指定的文件夹就创建一个，然后下载图片到指定文件夹内
        os.mkdir(dir_name)
        header = get_header()
        img_response = session.get(url=img_url, headers=header)
        open(dir_name + "/" + img_name + ".jpg", "wb").write(img_response.content)

if __name__ == '__main__':
    for i in range(1,9):                     # 根据分类网页的页数，进行循环遍历
        get_info_url(url=url,page=i)          # 调用自定义函数获取详情页请求地址
        t = random.randint(1,2)               # 随机秒数
        print("第",i,"页地址已获取,等待",t,"秒钟")
        time.sleep(t)                         # 等待随机秒数
    get_info("手机图片",info_url)               # 获取详情信息并插入数据库当中
    # 关闭cursor对象
    cs1.close()
    # 关闭connection对象
    conn.close()
