from requests import packages   # 导入模块中的包
import requests  # 导入网络请求模块
import re            # 导入re模块
import pandas as pd  # 导入pandas模块


ip_list = []  # 创建保存ip地址的列表

def get_ip(url,headers):
    packages.urllib3.disable_warnings()   # 关闭ssl警告
    # 发送网络请求
    response = requests.get(url,headers=headers,verify=False)
    response.encoding = 'utf-8'  # 设置编码方式
    if response.status_code == 200:  # 判断请求是否成功
        # 提取所有ip对应的标签
        ip_all = re.findall("<span class='f-address'>(.*?)</span>",response.text)
        # 提取所有端口号对应的标签
        port_all = re.findall("<span class='f-port'>(.*?)</span>",response.text)
        port_list = list(filter(lambda x:x.isdigit(),port_all))   # 将端口号筛选出来
        for ip,port in zip(ip_all[1:],port_list):    # 遍历ip与端口号
            ip_list.append(ip + ':' + port)  # 将ip与端口组合并添加至列表当中
            print('代理ip为：', ip, '对应端口为：', port)

# 头部信息
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/72.0.3626.121 Safari/537.36'}
if __name__ == '__main__':

    ip_table = pd.DataFrame(columns=['ip'])  # 创建临时表格数据
    for i in range(1,5):
        # 获取免费代理IP的请求地址
        url = 'https://www.dieniao.com/FreeProxy/{page}.html'.format(page=i)
        get_ip(url,headers)
    ip_table['ip'] = ip_list  # 将提取的ip保存至excel文件中的ip列
    # 生成xlsx文件
    ip_table.to_excel('ip.xlsx', sheet_name='data')
