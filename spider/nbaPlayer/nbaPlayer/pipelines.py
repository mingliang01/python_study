# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql           # 导入数据库操作模块

class NbaplayerPipeline:
    # 初始化数据库参数
    def __init__(self,host,database,user,password,port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    @classmethod
    def from_crawler(cls, crawler):
        # 返回cls()实例对象，其中包含通过crawler获取的配置文件中的数据库参数
        return cls(
            host=crawler.settings.get('SQL_HOST'),
            user=crawler.settings.get('SQL_USER'),
            password=crawler.settings.get('SQL_PASSWORD'),
            database=crawler.settings.get('SQL_DATABASE'),
            port=crawler.settings.get('SQL_PORT')
        )

    # 打开爬虫时调用
    def open_spider(self, spider):
        # 数据库连接
        self.db = pymysql.connect(host=self.host,user=self.user,password= self.password,database=self.database,port=self.port, charset='utf8mb4')
        self.cursor = self.db.cursor()  # 创建游标
        # 创建数据表
        self.cursor.execute('create  table if not exists player_info (id int(10)  primary key,name varchar(20),'
                       'team varchar(20),city varchar(20),date varchar(20),position varchar(20),height varchar(20)'
                            ',weight varchar(20),number varchar(20))')

    # 关闭爬虫时调用
    def close_spider(self, spider):
        self.db.close()

    # 将爬取的数据插入数据库当中
    i=0
    def process_item(self, item, spider):
        self.i+=1        # 自增id
        if item['city'] is None:  # 如果出生城市为None
            city = '无'           # 修改为字符串“无”
        else:
            city = item['city']

        # sql语句
        sql = 'insert into player_info (id,name,team,city,date,position,height,weight,number) values {}'\
                                .format((self.i,item['name'],item['team'],city,
                                item['date'],item['position'],item['height'],
                                item['weight'],item['number']))
        # 执行插入多条数据
        self.cursor.execute(sql)
        self.db.commit()  # 提交
        return item  # 返回item

