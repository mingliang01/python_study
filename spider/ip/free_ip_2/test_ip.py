import requests
from bs4 import BeautifulSoup
import socket

#获取代理
def get_ips(num):
    url="http://www.xicidaili.com/nn/{}".format(str(num))
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
                      " (KHTML, like Gecko)""Chrome/69.0.3497.100 Safari/537.36",
    }
    res=requests.get(url,headers=header)
    bs = BeautifulSoup(res.text, 'html.parser')
    res_list = bs.find_all('tr')
    ip_list = []
    for x in res_list:
        tds=x.find_all('td')
        if tds:
            ip_list.append({"ip":tds[1].text,"port":tds[2].text})
    return ip_list

#验证代理是否可用
def ip_pool():
    socket.setdefaulttimeout(2)
    ip_list = get_ips(1)
    ip_pool_list=[]
    for x in ip_list:
        proxy=x["ip"]+":"+x["port"]
        proxies = {'http': proxy}
        try:
            res=requests.get("http://www.baidu.com",proxies=proxies)
            if res.status_code==200:
                ip_pool_list.append(proxy)
        except Exception as ex:
            continue
    return ip_pool_list
#获取验证之后可用的ip
ip_list=ip_pool()