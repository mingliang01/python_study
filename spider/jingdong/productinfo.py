from selenium import webdriver  # 导入浏览器驱动模块
from selenium.webdriver.support.wait import WebDriverWait  # 导入等待类
from selenium.webdriver.support import expected_conditions as EC  # 等待条件
from selenium.webdriver.common.by import By                       # 节点定位

try:
    # 创建谷歌浏览器驱动参数对象
    chrome_options = webdriver.ChromeOptions()
    # 不加载图片
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    # 使用headless无界面浏览器模式
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    # 加载谷歌浏览器驱动
    driver = webdriver.Chrome(options=chrome_options)
    # 请求地址
    driver.get('https://item.jd.com/12353915.html')
    wait = WebDriverWait(driver,10)    # 等待10秒
    # 等待页面加载class名称为m-item-inner的节点，该节点中包含商品信息
    wait.until(EC.presence_of_element_located((By.CLASS_NAME,"product-intro clearfix")))
    # 获取name节点中所有div节点
    name_div = driver.find_element_by_css_selector('#name').find_elements_by_tag_name('div')
    summary_price = driver.find_element_by_id('summary-price')
    print('提取的商品标题如下：')
    print(name_div[0].text)         # 打印商品标题
    print('提取的商品宣传语如下：')
    print(name_div[1].text)         # 打印宣传语
    print('提取的编著信息如下：')
    print(name_div[4].text)         # 打印编著信息
    print('提取的价格信息如下：')
    print(summary_price.text)       # 打印价格信息
    driver.quit()  # 退出浏览器驱动
except Exception as e:
    print('显示异常信息！', e)
