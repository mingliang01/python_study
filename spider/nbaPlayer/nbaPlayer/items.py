# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class NbaplayerItem(scrapy.Item):
    # define the fields for your item here like:
    # 球员名字
    name = scrapy.Field()
    # 球队
    team = scrapy.Field()
    # 出生城市
    city = scrapy.Field()
    # 出生日期
    date = scrapy.Field()
    # 位置
    position = scrapy.Field()
    # 身高
    height = scrapy.Field()
    # 体重
    weight = scrapy.Field()
    # 球衣号码
    number = scrapy.Field()
    pass
