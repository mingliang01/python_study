import re          # 导入re模块，用于正则表达式
import  requests   # 导入网络请求模块
import os          # 导入os模块，用于获取路径
import json
def get_station():
    # 发送请求获取所有车站名称,通过输入的站名称转化查询地址的参数
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9050'
    response = requests.get(url, verify=True)  # 请求并进行验证
    stations = re.findall('([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)  # 获取需要的车站名称
    stations = dict(stations)  # 转换为dic
    stations = str(stations)  # 转换为字符串类型否则无法写入文件
    write(stations,'stations.text')           #调用写入方法

# 下载车票起售时间的文件
def get_selling_time():
    url = 'https://www.12306.cn/index/otn/index12306/queryAllCacheSaleTime'
    response = requests.get(url)     # 请求并进行验证
    response_dict = response.json()  # 将返回的json数据转换为字典数据
    data = response_dict['data']     # 获取所有数据
    time_dict = dict()                  # 创建一个保存起售时间的字典
    for i in data:
        city_name = i['station_name']         # 获取车站名称
        time = i['sale_time']                 # 获取起售时间
        new_time = time[:2] + ':' + time[2:]  # 重新组合时间
        time_dict.update({city_name: new_time})  # 将每个车站对应的起售时间保存在字典中
    write(str(time_dict), 'time.text')  # 调用写入方法

# 写入数据
def write(stations,file_name):
    file = open(file_name, 'w', encoding='utf_8_sig')  # 以写模式打开文件
    file.write(stations)  # 写入数据
    file.close()
# 读取数据
def read(file_name):
    file = open(file_name, 'r', encoding='utf_8_sig')  # 以写模式打开文件
    data = file.readline()                                  #读取文件
    file.close()
    return data
# 判断文件是否存在
def is_stations(file_name):
    is_stations = os.path.exists(file_name)      #判断文件是否存在,文件名称作为参数
    return is_stations




