# -*- coding: utf-8 -*-
import scrapy
from jd.items import JdItem     # 导入JdItem类

class JdspiderSpider(scrapy.Spider):
    name = 'jdSpider'                  # 默认生成的爬虫名称
    allowed_domains = ['book.jd.com']
    start_urls = ['http://book.jd.com/']

    def start_requests(self):
        # 需要访问的地址
        url = 'https://book.jd.com/booktop/0-0-0.html?category=3287-0-0-0-10001-1'
        yield scrapy.Request(url=url, callback=self.parse)      # 发送网络请求

    def parse(self, response):
        all=response.xpath(".//*[@class='p-detail']")                       # 获取所有信息
        book_name = all.xpath("./a[@class='p-name']/text()").extract()      # 获取所有图书名称
        author = all.xpath("./dl[1]/dd/a[1]/text()").extract()              # 获取所有作者名称
        press = all.xpath("./dl[2]/dd/a/text()").extract()                  # 获取所有出版社名称
        item = JdItem()     # 创建Item对象
        # 将数据添加至Item对象
        item['book_name'] = book_name
        item['author'] = author
        item['press'] = press
        yield item    # 打印item信息
        pass

# 导入CrawlerProcess类
from scrapy.crawler import CrawlerProcess
# 导入获取项目设置信息
from scrapy.utils.project import get_project_settings

# 程序入口
if __name__=='__main__':
    # 创建CrawlerProcess类对象并传入项目设置信息参数
    process = CrawlerProcess(get_project_settings())
    # 设置需要启动的爬虫名称
    process.crawl('jdSpider')
    # 启动爬虫
    process.start()
