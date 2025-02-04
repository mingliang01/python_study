import requests     # 导入网络请求模块
from bs4 import BeautifulSoup  # 导入BeautifulSoup库
import time         # 导入时间模块
import random       # 导入随机模块

def network_request(url):
    # 发送网络请求
    response = requests.get(url=url)
    response.encoding = "utf-8"  # 设置编码方式
    # 创建一个BeautifulSoup对象，解析HTML代码
    soup = BeautifulSoup(response.text, features="lxml")
    return soup   # 返回解析后的soup对象

def music_info(s):
    ranks=s.select('span.pc_temp_num')                # 获取所有排名编号对应的标签
    name=s.select('div.pc_temp_songlist >ul > li>a')  # 获取所有歌曲与歌手名称对应的标签
    time = s.select('span.pc_temp_time')              # 获取所有歌曲时间对应的标签
    for r,n,t in zip(ranks,name,time):                # 循环遍历所有数据
        rank = r.get_text().strip()                   # 获取排名信息
        name = n.get_text()                           # 获取歌曲名称和歌手
        time = t.get_text().strip()                   # 获取歌曲时长
        print(rank,name,time)                         # 打印歌曲信息

if __name__ == '__main__':                            # 创建程序入口
    for page in range(1,24):                              # 循环发送每页的网络请求
        # 循环切换每页的请求地址
        url = 'https://www.kugou.com/yy/rank/home/{page}-8888.html?from=rank'.format(page=page)
        soup=network_request(url)      # 发送网络请求并获取解析后的soup对象
        music_info(soup)               # 提取数据
        time.sleep(random.randint(2,4))# 等待随机时间
