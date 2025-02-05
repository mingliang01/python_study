# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DistributedItem(scrapy.Item):
    news_title = scrapy.Field()  # 保存新闻标题
    news_synopsis = scrapy.Field()  # 保存新闻简介
    news_url = scrapy.Field()  # 保存新闻详情页面的地址
    news_time = scrapy.Field()  # 保存新闻发布时间
    pass
