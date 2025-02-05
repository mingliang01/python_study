import requests
from bs4 import BeautifulSoup

def get_ips(num):
    url="http://www.xicidaili.com/nn/{}".format(str(num))
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/69.0.3497.100 Safari/537.36",
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
#获取第一页的ip，这个可以自己随便填
ip_list=get_ips(1)
#循环打印看一下我们的所获取到ip
for item in ip_list:
    print(item)