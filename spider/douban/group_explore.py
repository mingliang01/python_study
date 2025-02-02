
from requests_html import HTMLSession,HTML   # 导入会话对象类与HTML解析类
import pandas                                # 导入pandas模块

session = HTMLSession()                              # 创建会话对象
response = session.get('https://www.douban.com/group/explore')   # 发送网络请求
html = HTML(html=response.text)                             # 解析HTML代码
title_all = html.xpath('//div[@class="bd"]/h3/a/text()')    # 获取所有标题
like_all = html.xpath('//div[@class="likes"]/text()[1]')    # 获取喜欢数
info_all = html.xpath('//div[@class="block"]/p/text()')     # 获取简介内容
user_all = html.xpath('//span[@class="from"]/a/text()')     # 获取用户名称
pubtime = html.xpath('//span[@class="pubtime"]/text()')     # 获取时间

df = pandas.DataFrame(columns=['标题','喜欢','简介','用户名称','时间'])   # 创建临时表格对象
# 设置每列数据
df['标题'] = title_all
df['喜欢'] = like_all
df['简介'] = info_all
df['用户名称'] = user_all
df['时间'] = pubtime
df.to_excel('豆瓣小组（讨论精选）.xlsx')   # 将数据写入excel文件中