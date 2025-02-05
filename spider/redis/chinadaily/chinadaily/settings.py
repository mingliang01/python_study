# -*- coding: utf-8 -*-

# Scrapy settings for distributed project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'distributed'

SPIDER_MODULES = ['distributed.spiders']
NEWSPIDER_MODULE = 'distributed.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# 启用redis调度存储请求队列
SCHEDULER  = 'scrapy_redis.scheduler.Scheduler'
#确保所有爬虫通过redis共享相同的重复筛选器。
DUPEFILTER_CLASS  = 'scrapy_redis.dupefilter.RFPDupeFilter'
#不清理redis队列，允许暂停/恢复爬虫
SCHEDULER_PERSIST =True
#使用默认的优先级队列调度请求
SCHEDULER_QUEUE_CLASS ='scrapy_redis.queue.PriorityQueue'
REDIS_URL ='redis://192.168.3.67:6379'
DOWNLOADER_MIDDLEWARES = {
    # 启动自定义随机请求头中间件
    'distributed.middlewares.RandomHeaderMiddleware': 200,
    # 'distributed.middlewares.DistributedDownloaderMiddleware': 543,
}
# 配置请求头类型为随机，此处还可以设置为ie、firefox以及chrome
RANDOM_UA_TYPE = "random"
ITEM_PIPELINES = {
   'distributed.pipelines.DistributedPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline':400
}
# 配置数据库连接信息
SQL_HOST = '192.168.3.67'      # 数据库地址
SQL_USER = 'root'            # 用户名
SQL_PASSWORD='root'          # 密码
SQL_DATABASE = 'news_data'    # 数据库名称
SQL_PORT = 3306              # 端口

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'distributed (+http://www.yourdomain.com)'



# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'distributed.middlewares.DistributedSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html



# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
