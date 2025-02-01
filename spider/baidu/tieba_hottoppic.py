import requests                # 导入requests模块
from bs4 import BeautifulSoup  # 导入BeautifulSoup模块

def send_request(url,headers):
    response = requests.get(url=url,headers=headers)      # 发送网络请求
    if response.status_code == 200:  # 如果请求成功
        return response.text  # 返回html

# 解析响应结果中的数据
def interpreting_data(html_text):
    soup = BeautifulSoup(html_text, features="lxml")  # 解析html代码
    div_name = soup.find_all(class_='topic-name')         # 获取所有包含标题的div标签
    infos = soup.find_all(class_='topic-top-item-desc')   # 获取所有简介
    for d,i in zip(div_name,infos):
        title=d.a.string       # 获取标题
        href = d.a['href']     # 获取详情页地址
        number = d.find(class_='topic-num').string  # 获取实时讨论数量
        info = i.string        # 获取简介内容
        print('标题：',title)
        print('详情页地址：',href)
        print('实时讨论：',number)
        print('简介：',info)
        print()

if __name__ == '__main__':
    url = 'http://tieba.baidu.com/hottopic/browse/topicList?res_type=1&red_tag=y0319003759'
    # 定义请求头信息
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4503.5 Safari/537.36'}
    html_text = send_request(url=url, headers=headers)  # 发送网络请求
    interpreting_data(html_text)  # 解析数据