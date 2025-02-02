
from requests_html import HTMLSession,HTML   # 导入会话对象类与HTML解析类
import sqlite3                               # 导入sqlite3数据库

session = HTMLSession()                              # 创建会话对象
response = session.get('https://www.xiachufang.com/category/40076/')   # 发送网络请求
html = HTML(html=response.text)   # 解析HTML代码
name_all = html.xpath('//div[@class="info pure-u"]/p[1]/a')        # 获取菜名对应的标签
material_all = html.xpath('//p[@class="ing ellipsis"]')         # 获取材料对应的标签
score_all = html.xpath('//p[@class="stats"]')                   # 获取评分对应的标签
author_all = html.xpath('//a[@class="gray-font"]')              # 获取作者名称对应的标签

# 连接到SQLite数据库
# 数据库文件是mrsoft.db，如果文件不存在，会自动在当前目录创建
conn = sqlite3.connect('menu.db')
# 创建一个Cursor
cursor = conn.cursor()
# 执行一条SQL语句，创建user表
cursor.execute('create  table if not exists menu (id int(10)  primary key,name varchar(20),'
               'material varchar(30),score varchar(10),author varchar(10))')

id = 0
for n,m,s,a in zip(name_all[:20],material_all[:20],score_all[:20],author_all[:20]):
    id+=1                             # id
    name = n.text                     # 获取菜名
    material = m.text                 # 获取做菜所需的材料
    score = "".join(s.text.split())   # 获取评分,并去除\\xa0
    author = a.text                   # 获取作者
    # 执行插入数据的sql语句
    cursor.execute('insert into menu (id,name,material,score,author) values {}'.format((id,name,material,score,author)))

# 执行查询语句
cursor.execute('select * from menu')
result = cursor.fetchall()           # 使用fetchall()方法查询多条数据
print(result)                        # 打印查询结果

# 关闭游标
cursor.close()
# 关闭Connection
conn.close()

