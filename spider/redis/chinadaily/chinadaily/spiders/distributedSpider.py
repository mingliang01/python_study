
# -*- coding: utf-8 -*-
import scrapy
from distributed.items import DistributedItem   # 导入Item对象
class DistributedspiderSpider(scrapy.Spider):
    name = 'distributedSpider'
    allowed_domains = ['china.chinadaily.com.cn']
    start_urls = ['http://china.chinadaily.com.cn/']
    # 发送网络请求
    def start_requests(self):
        for i in  range(1,101):    # 由于新闻网页共计100页，所以循环执行100次
            # 拼接请求地址
            url = self.start_urls[0] + '5bd5639ca3101a87ca8ff636/page_{page}.html'.format(page=i)
            # 执行请求
            yield scrapy.Request(url=url,callback=self.parse)

    # 处理请求结果
    def parse(self, response):
        item = DistributedItem()               # 创建item对象
        all = response.css('.busBox3')         # 获取每页所有新闻内容
        for i in all:                          # 循环遍历每页中每条新闻
            title = i.css('h3 a::text').get()    # 获取每条新闻标题
            synopsis = i.css('p::text').get()    # 获取每条新闻简介
            url = 'http:'+i.css('h3 a::attr(href)').get()      # 获取每条新闻详情页地址
            time_ = i.css('p b::text').get()       # 获取新闻发布时间
            item['news_title'] = title            # 将新闻标题添加至item
            item['news_synopsis'] = synopsis      # 将新闻简介内容添加至item
            item['news_url'] = url                # 将新闻详情页地址添加至item
            item['news_time'] = time_                   # 将新闻发布时间添加至item
            yield item  # 打印item信息
        pass

# 导入CrawlerProcess类
from scrapy.crawler import CrawlerProcess
# 导入获取项目配置信息
from scrapy.utils.project import get_project_settings

# 程序入口
if __name__=='__main__':
    # 创建CrawlerProcess类对象并传入项目设置信息参数
    process = CrawlerProcess(get_project_settings())
    # 设置需要启动的爬虫名称
    process.crawl('distributedSpider')
    # 启动爬虫
    process.start()
