
import time                     # 导入时间模块
from selenium import webdriver  # 导入浏览器驱动模块
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By          # 节点定位
import os

# 创建谷歌浏览器驱动参数对象
chrome_options = webdriver.ChromeOptions()
# 不加载图片
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
# 使用headless无界面浏览器模式
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
git_dir = r'../../'
chrome_options.binary_location = os.path.join(git_dir, r'chrome-win64/chrome.exe')  # 指定Chrome的路径，如果不需要可以省略这行

# 指定ChromeDriver的路径
chrome_driver_path = os.path.join(git_dir, r'chromedriver-win64/chromedriver.exe')
print(chrome_driver_path)
chrome_service = Service(executable_path=chrome_driver_path)
# 加载谷歌浏览器驱动
driver = webdriver.Chrome(options=chrome_options, service=chrome_service)
# driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

# 请求地址
driver.get('https://read.douban.com/charts?index=featured&type=unfinished_column&dcm=charts-nav&dcs=charts')
time.sleep(2)    # 根据网速适当的等待一段时间，让页面加载完
name_all = driver.find_elements(By.XPATH,'//span[@class="title-text"]')     # 获取所有小说名称对应的标签
author_all = driver.find_elements(By.XPATH,'//span[@class="author-link"]')     # 获取所有小说作者对应的标签
info_all = driver.find_elements(By.XPATH,'//div[@class="intro"]/span')     # 获取所有简介对应的标签
type_all = driver.find_elements(By.XPATH,'//div[@class="sticky-info"]/span[2]') # 获取所有类型对应的标签
word_all = driver.find_elements(By.XPATH,'//div[@class="sticky-info"]/span[4]') # 获取所有字数对应的标签
for n,a,i,t,w in zip(name_all,author_all,info_all,type_all,word_all):   # 遍历所有标签
    print('小说名称：',n.text)
    print('小说作者：',a.text)
    print('小说简介：',i.text)
    print('小说类型：',t.text)
    print('小说字数：',w.text)
    print()
driver.quit()  # 退出浏览器驱动


