import re
import requests
import os
import inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
data_path = os.path.join(current_dir, 'data')
if not os.path.isdir(data_path):
    os.mkdir(data_path)
station_path = os.path.join(data_path, 'stations.text')
def getStation():
    # 发送请求获取所有车站名称,通过输入的站名称转化查询地址的参数
    # url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9006'
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9338'
    response = requests.get(url, verify=True)  # 请求并进行验证
    stations = re.findall(u'([\u4e00-\u9fa5]+)\\|([A-Z]+)', response.text)  # 获取需要的车站名称
    stations = dict(stations)  # 转换为dic
    stations = str(stations)  # 转换为字符串类型否则无法写入文件
    write(stations)           #调用写入方法
def write(stations):
    file = open(station_path, 'w', encoding='utf_8_sig')  # 以写模式打开文件
    file.write(stations)  # 写入数据
    file.close()
def read():
    file = open(station_path, 'r', encoding='utf_8_sig')  # 以写模式打开文件
    data = file.readline()                                  #读取文件
    file.close()
    return data

def isStations():
    isStations = os.path.exists(station_path)      #判断车站文件是否存在
    return isStations






