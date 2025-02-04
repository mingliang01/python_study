from lxml import etree    # 导入etree子模块
import time               # 导入时间模块
import random             # 导入随机模块
import requests           # 导入网络请求模块
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
# 处理字符串中的空白符，并拼接字符串
def processing(strs):
    s = ''  # 定义保存内容的字符串
    for n in strs:
        n = ''.join(n.split())  # 去除空字符
        s = s + n  # 拼接字符串
    return s      # 返回拼接后的字符串

# 获取电影信息
def get_movie_info(url):
    response = requests.get(url,headers=header)                    # 发送网络请求
    html = etree.HTML(response.text)                               # 解析html字符串
    div_all = html.xpath('//div[@class="info"]')
    for div in div_all:
        names = div.xpath('./div[@class="hd"]/a//span/text()')   # 获取电影名字相关信息
        name = processing(names)                                    # 处理电影名称信息
        infos = div.xpath('./div[@class="bd"]/p/text()')         # 获取导演、主演等信息
        info = processing(infos)                                   # 处理导演、主演等信息
        score = div.xpath('./div[@class="bd"]/div/span[2]/text()')      # 获取电影评分
        evaluation = div.xpath('./div[@class="bd"]/div/span[4]/text()') # 获取评价人数
        # 获取电影总结文字
        summary = div.xpath('./div[@class="bd"]/p[@class="quote"]/span/text()')
        print('电影名称：',name)
        print('导演与演员：',info)
        print('电影评分：',score)
        print('评价人数：',evaluation)
        print('电影总结：',summary)
        print('--------分隔线--------')
if __name__ == '__main__':
    for i in range(0,250,25):    # 每页25为间隔，实现循环，共10页
        # 通过format替换切换页码的url地址
        url = 'https://movie.douban.com/top250?start={page}&filter='.format(page=i)
        get_movie_info(url)                      # 调用爬虫方法,获取电影信息
        time.sleep(random.randint(1,3))          # 等待1至3秒随机时间
