
import scrapy                                # 导入scrapy模块
import sys

sys.path.append('../..')

from nbaPlayer.items import NbaplayerItem    # 导入Item对象

class PlayerspiderSpider(scrapy.Spider):
    name = 'playerSpider'     # 爬虫名称
    allowed_domains = ['data.sports.sohu.com/nba']
    start_urls = ['http://data.sports.sohu.com/nba/']   # 起始地址


    # 执行发送网络请求
    def start_requests(self):
        # 发送网络请求
        yield scrapy.Request(url=self.start_urls[0]+'nba_players.html',callback=self.parse)

    # 执行解析数据
    def parse(self, response):
        # 获取所有球员详情地址
        info_urls = response.xpath('//ul[@class="w250"]/li/a/@href').extract()
        for url in info_urls:   # 遍历球员详情的地址
            # 对每个球员的详情页发送网络请求,dont_filter表示不进行过滤
            yield scrapy.Request(url=self.start_urls[0]+url,callback=self.info_parse,dont_filter=True)
        pass

    # 解析球员的信息
    def info_parse(self,response):
        # 获取球员名字
        name = response.xpath('//div[@class="blockA"]/h2/span/text()').extract_first()
        # 获取球队名称
        team = response.xpath('//div[@class="pt"]/ul/li/a/text()').extract_first()
        # 获取出生城市
        city = response.xpath('//div[@class="pt"]/ul/li[2]/text()').extract_first()
        # 获取出生日期
        date = response.xpath('//div[@class="pt"]/ul/li[3]/text()').extract_first()
        # 获取位置
        position = response.xpath('//div[@class="pt"]/ul/li[4]/text()').extract_first()
        # 获取身高
        height= response.xpath('//div[@class="pt"]/ul/li[5]/text()').extract_first()
        # 获取体重
        weight= response.xpath('//div[@class="pt"]/ul/li[6]/text()').extract_first()
        # 获取球衣号码
        number = response.xpath('//div[@class="pt"]/ul/li[7]/text()').extract_first()
        # 数据结构化
        item = NbaplayerItem(name=name,team=team,city=city,date=date,
                             position=position,height=height,weight=weight,number=number)
        yield item



# 导入CrawlerProcess类
from scrapy.crawler import CrawlerProcess
# 导入获取项目设置信息
from scrapy.utils.project import get_project_settings


# 程序入口
if __name__=='__main__':
    # 创建CrawlerProcess类对象并传入项目设置信息参数
    process = CrawlerProcess(get_project_settings())
    # 设置需要启动的爬虫名称
    process.crawl('playerSpider')
    # 启动爬虫
    process.start()
