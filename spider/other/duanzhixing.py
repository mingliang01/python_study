import requests                # 网络请求模块
from bs4 import BeautifulSoup  # 导入BeautifulSoup模块
import time                    # 导入时间模块
import random                  # 导入随机数模块

def get_urls(url):                   # 获取每页段子所有详情页的url
    urls = []
    # 发送网络请求
    response = requests.get(url=url)
    # 创建一个BeautifulSoup对象，解析HTML代码
    soup = BeautifulSoup(response.text, features="lxml")
    h2_all=soup.find_all(name='h2')      # 获取每页所有h2标签
    for h in h2_all:                     # 遍历h2标签
        # 获取每个h2标签中的详情页url，并添加至列表中
        urls.append(h.find('a')['href'])
    return urls                           # 返回每页的所有详情页url

def get_info(url):              # 获取每个段子的详情信息
    # 发送网络请求
    response = requests.get(url=url)
    # 创建一个BeautifulSoup对象，解析HTML代码
    soup = BeautifulSoup(response.text, features="lxml")
    # 获取段子标题
    title = soup.find(class_='article-title').find('a').get_text()
    # 获取日期、分类、阅读、评论所对应的标签
    spans = soup.find(class_='article-meta').find_all(name='span')
    date = spans[0].get_text()       # 获取日期信息
    type = spans[1].get_text()       # 获取分类信息
    read = spans[2].get_text()       # 获取阅读信息
    comment = spans[3].get_text()    # 获取评论信息
    # 获取段子内容
    content = soup.find(class_='article-content').get_text()
    print(title)      # 打印段子标题
    print(date)       # 打印日期
    print(type)       # 打印分类
    print(read)       # 打印阅读
    print(comment)    # 打印评论
    print(content)    # 打印段子
    print()           # 打印空行，作为没个段子的分隔符

if __name__ == '__main__':
    for i in range(1,92):                     # 遍历页数
        # 替换每页的请求地址
        url = 'https://duanzixing.com/page/{}/'.format(i)
        urls=get_urls(url)                    # 对每页发送网络请求获取所有详情页地址
        for u in urls:                        # 遍历每页的详情页地址
            get_info(u)                       # 发送网络请求获取每个段子对应的信息
            time.sleep(random.randint(1,3))   # 随机等待时间
