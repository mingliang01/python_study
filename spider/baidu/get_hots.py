# -*- coding:utf-8 -*-

'''
   @ 功能：获取百度热搜
   @ author:Ming Liang
   @ create:
'''
import urllib.request  # 导入urllib.request模块
import re              # 导入re模块

# 实现发送网络请求，返回响应结果
def send_request(url,headers):
    # 创建Request对象
    r = urllib.request.Request(url=url,headers=headers)
    response = urllib.request.urlopen(r)  # 发送网络请求
    # 读取HTML代码并进行utf-8解码
    html_text = response.read().decode('utf-8')
    return html_text

# 解析响应结果中的数据
def interpreting_data(html_text):
    # 提取热搜排名
    ranking_all = re.findall('<span class="title-content-index c-index-single c-index-single-hot.*?">(.*?)</span>',html_text)
    # 提取热搜标题
    title_all = re.findall('<span class="title-content-title">(.*?)</span>',html_text)
    # 提取热搜关键词
    keyword_all = re.findall(r'(<span class="title-content-mark ie-vertical c-text c-gap-left-small c-text-hot.*?">|<span class="title-content-mark ie-vertical c-text c-gap-left-small ">)(.*?)</span>',html_text)
    # 提取热搜标题对应的地址
    href_all = re.findall(r'(<a class="title-content tag-width c-link c-font-medium c-line-clamp1"|<a class="title-content  c-link c-font-medium c-line-clamp1") href="(.*?)"',html_text)
    for r,t,k,h in zip(ranking_all,title_all,keyword_all,href_all):
        if k[1] =='':    # 如果热搜关键词为空
            print('排名：'+r,'热搜标题：'+t,'关键词：无','地址：'+h[1])
        else:
            print('排名：' + r, '热搜标题：' + t, '关键词：'+k[1], '地址：' + h[1])
        print()       # 打印空行

if __name__ == '__main__':
    url = 'https://www.baidu.com/'  # 请求地址
    # 定义请求头信息
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
    html_text = send_request(url=url,headers=headers)    # 调用自定义发送网络请求的方法
    interpreting_data(html_text=html_text)               # 调用解析响应结果的方法