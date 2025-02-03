# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql            # 导入数据库连接pymysql模块

class JdPipeline(object):
    # 初始化数据库参数
    def __init__(self,host,database,user,password,port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    @classmethod
    def from_crawler(cls,crawler):
        # 返回cls()实例对象，其中包含通过crawler获取配置文件中的数据库参数
        return cls(
            host=crawler.settings.get('SQL_HOST'),
            user=crawler.settings.get('SQL_USER'),
            password=crawler.settings.get('SQL_PASSWORD'),
            database = crawler.settings.get('SQL_DATABASE'),
            port = crawler.settings.get('SQL_PORT')
        )

    # 打开爬虫时调用
    def open_spider(self, spider):
        # 数据库连接
        self.db = pymysql.connect(self.host,self.user,self.password,self.database,self.port,charset='utf8')
        self.cursor = self.db.cursor()    #床架游标

    # 关闭爬虫时调用
    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        data = dict(item)     # 将item转换成字典类型
        # sql语句
        sql = 'insert into ranking (book_name,press,author) values(%s,%s,%s)'
        # 执行插入多条数据
        self.cursor.executemany(sql, list(zip(data['book_name'], data['press'], data['author'])))
        self.db.commit()     # 提交
        return item         # 返回item
