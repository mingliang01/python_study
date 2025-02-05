import requests
import uuid
import time

'''
农产品批发价格周数据库-表2-蔬菜产品
'''
for page in range(1,26):
    print(page)
    session=requests.session()
    url_1="http://zdscxx.moa.gov.cn:8080/nyb/updateFrequencyConditions"
    url_2="http://zdscxx.moa.gov.cn:8080/nyb/getFrequencyData"
    data={
        "page":page,
        "rows": 20,
        "type": "周度数据",
        "subType": "农产品批发价格",
        "time": '["2016-24","2020-24"]',
        "product": "蔬菜",
        "level":0
    }
    print(data)
    header={
        "Cookie":"JSESSIONID=5F4D9473577EDE5C931B67A4EB24BFE3",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML"
                     ", like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        "Host":"zdscxx.moa.gov.cn:8080",
        "Origin":"http://zdscxx.moa.gov.cn:8080",
        "Referer": "http://zdscxx.moa.gov.cn:8080/nyb/pc/frequency.jsp",
        "X-Requested-With":"XMLHttpRequest"
    }
    res1=session.post(url_1,data=data,headers=header)
    res=session.post(url_2,data=data,headers=header)
    if(data_list:=res.json()["result"]["pageInfo"]["table"]):
        print(data_list)
        s_data_list = []
        for item in data_list:
            data = {}
            data["id"] = str(uuid.uuid4())
            data["zs_time"] = item["time"]
            data["category"] = item["product"]
            data["zs_index"] = item["item"]
            data["area"] = item["area"]
            data["unit"] = item["unit"]
            data["z_value"] = item["value"]
            # 爬虫采集时间
            data["ct_time"] = str(time.strftime('%Y-%m-%d %H:%M:%S', 
                                                time.localtime(time.time())))
            print(data)
            # s_data_list.append(data)
    time.sleep(5)