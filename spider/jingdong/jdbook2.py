import requests_html  # 导入网络请求模块
import sqlite3        # 导入sqlite3数据库模块
import os             # 导入系统模块


# 执行创建数据库与数据表
create_sql = 'create  table  book (id int(10) ,title varchar(20),author varchar(20),' \
             'publish varchar(20),d_price varchar(20),j_price varchar(20))'
# 插入数据
insert_sql = 'insert into book (id,title,author,publish,d_price,j_price) values (?,?,?,?,?,?)'

# 连接SQLite数据库
def connect_sqlite():
    # 连接到SQLite数据库
    # 数据库文件是mrsoft.db，如果文件不存在，会自动在当前目录创建
    conn = sqlite3.connect('jd_book.db')
    # 创建一个Cursor
    cursor = conn.cursor()
    return conn, cursor

# 关闭数据库与游标
def close_sqlite(cursor, conn):
    # 关闭游标
    cursor.close()
    # 关闭Connection
    conn.close()

session = requests_html.HTMLSession()  # 创建会话对象

# 发送网络请求
def send_request(page,cursor,conn):
    # 请求地址
    url = 'https://book.jd.com/booktop/0-0-0.html?category=3287-0-0-0-10003-{page}#comfort'.format(page=page)
    response = session.get(url)                                   # 发送网络请求
    response.html.render()                                        # 加载网页动态渲染的信息
    id_all = response.html.xpath('//div[@class="p-num"]/text()')  # 获取每页所有图书排名
    # 获取每页所有图书名称
    title_all = response.html.xpath('//div[@class="p-detail"]/a/text()')
    # 获取每页所有作者对应的标签
    author_all = response.html.xpath('//div[@class="p-detail"]/dl[1]/dd')
    # 获取每页所有出版社对应的标签
    publish_all = response.html.xpath('//div[@class="p-detail"]/dl[2]/dd')
    # 获取每页所有定价对应的标签
    d_price_all = response.html.xpath('//div[@class="p-detail"]/dl[3]/dd')
    # 获取每页所有京东价对应的标签
    j_price_all = response.html.xpath('//div[@class="p-detail"]/dl[4]/dd')

    for id,title,author,publish,d_price,j_price in zip(id_all,title_all,author_all,publish_all,d_price_all,j_price_all):
        # 执行插入数据的sql语句
        cursor.execute(insert_sql,(id,title,author.text,publish.text,d_price.text,j_price.text))
        conn.commit()                             # 提交数据

if __name__ == '__main__':
    if not os.path.exists('jd_book.db'):     # 如果数据库不存在
        conn, cursor = connect_sqlite()      # 连接数据库
        cursor.execute(create_sql)           # 创建数据表
        for i in range(1,6):
            send_request(page=i,cursor=cursor,conn=conn)
        cursor.execute('select * from book')  # 查询数据表
        result = cursor.fetchall()  # 使用fetchall()方法查询多条数据
        print(result)  # 打印数据库中的数据
        close_sqlite(cursor,conn)
    else:
        conn, cursor = connect_sqlite()  # 连接数据库
        for i in range(1,6):
            send_request(page=i, cursor=cursor, conn=conn)
        cursor.execute('select * from book')  # 查询数据表
        result = cursor.fetchall()  # 使用fetchall()方法查询多条数据
        print(result)  # 打印数据库中的数据
        close_sqlite(cursor, conn)
