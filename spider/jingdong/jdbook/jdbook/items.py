# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class JdItem(scrapy.Item):
    # define the fields for your item here like:
    book_name = scrapy.Field()    # 保存图书名称
    author = scrapy.Field()       # 保存作者
    press = scrapy.Field()        # 保存出版社
    pass
