import requests  # 导入网络请求模块
import pandas    # 导入pandas模块
import re            # 导入re模块
import random            # 导入随机模块

ip_table = pandas.read_excel('ip.xlsx')  # 读取代理IP文件内容
ip = ip_table['ip']                      # 获取代理ip列信息
effective_ip = []             # 保存验证后的IP,然后可以从这个列表中随机抽取一个有效的代理IP

# 头部信息
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/72.0.3626.121 Safari/537.36'}
# 循环遍历代理IP并通过代理发送网络请求
for i in ip:
    proxies = {'http':'http://{ip}'.format(ip=i),
               'https':'https://{ip}'.format(ip=i)}
    try:
        response = requests.get('https://2021.ip138.com/',
                                headers=headers,proxies=proxies,timeout=2)
        if response.status_code==200:   # 判断请求是否成功,请求成功说明代理IP可用
            response.encoding='utf-8'     # 进行编码
            # 获取IP地址
            ip = re.findall('<title>(.*?)</title>',response.text)[0]
            # 获取位置
            position = re.findall('] (.*?)</p>',response.text,re.S)[0]
            info = ip+position          # 组合匿名ip的信息
            print(info)                 # 输出当前ip匿名信息
            effective_ip.append(i)         # 将有效的代理IP保存在列表中
    except Exception as e:
        pass
        # print('错误异常信息为：',e)    # 打印异常信息

random_ip = random.choice(effective_ip)      # 有效代理IP的列表中随机抽取一个代理IP
print("随机抽取的有效代理IP：",random_ip)    # 打印随机抽取的代理IP
