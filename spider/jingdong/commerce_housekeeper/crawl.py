# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2018/11/30  14:04
# 文件名称   ：crawl.py.py
# 开发工具   ：PyCharm

import requests # 网络请求模块
from urllib.request import urlretrieve  # 直接远程下载图片
import shutil      # 文件夹控制
import json        # 导入json模块
import re          # 导入re模块
import os          # os模块
rankings_list = []  # 保存排行数据的列表

class Crawl(object):

    # 获取排行
    def get_rankings_json(self, url):
        self.jd_id_list = []  # 保存京东id的列表
        self.name_list = []  # 保存商品名称的列表
        self.hot_list =[]   # 保存热卖指数的列表
        response = requests.get(url)  # 发送网络请求，获取服务器响应
        json_str = str(response.json())  # 将请求结果的json信息转换为字符串
        dict_json = eval(json_str)       # 将json字符串信息转换为字典，方便提取信息
        jd_id_str =''
        # 每次获取数据之前，先将保存图片的文件夹清空，清空后再创建目录
        if os.path.exists('img_download'): # 判断img目录是否存在
            shutil.rmtree('img_download') # 删除img目录
            os.makedirs('img_download')  # 创建img目录
        for index,i in enumerate(dict_json['products']):
            print(dict_json['products'])
            id = i['wareId']        # 京东id号码
            J_id = 'J_'+i['wareId'] # 京东id，添加J_用于作为获取价格参数
            self.jd_id_list.append(id) # 将商品id添加至列表中
            name = i['wareName']  # 商品名称
            self.name_list.append(name) # 将商品名称添加至列表中
            hot = i['hotScore']  # 热卖指数
            self.hot_list.append(str(hot)) # 将热卖指数添加至列表中
            jd_id_str = jd_id_str + J_id+',' # 拼接京东id字符串
            if index<=10:
                # 图片地址
                imgPath = 'https://img12.360buyimg.com/n1/s160x160_'+i['imgPath']
                urlretrieve(imgPath,'img_download/'+str(index)+'.jpg') # 根据下标命名图片名称
        return jd_id_str

    # 获取商品价格
    def get_price(self, id):
        rankings_list.clear() # 清空排行数据的列表
        price_url = 'http://p.3.cn/prices/mgets?type=1&skuIds={id_str}' # 获取价格的网络请求地址
        response = requests.get(price_url.format(id_str=id))  # 将京东id作为参数发送获取商品价格的网络请求
        price = response.json()  # 获取价格json数据，该数据为list类型
        for index, item in enumerate(price):
            # 商品名称
            name = self.name_list[index]
            # 京东价格
            jd_price = item['p']
            # 每个商品的京东id
            jd_id = self.jd_id_list[index]
            # 热卖指数
            hot = self.hot_list[index]
            # 将所有数据添加到列表中
            rankings_list.append((index+1,name, jd_price, jd_id,hot))
        return rankings_list # 返回所有排行数据列表

    # 获取评价内容,score参数差评为1、中评为2、好评为3，0为全部
    def get_evaluation(self, score, id):
        # 创建头部信息
        headers = {'User-Agent': 'OW64; rv:59.0) Gecko/20100101 Firefox/59.0'}
        # 评价请求地址参数，callback为对应书名json的id，
        # productId书名对应的京东id
        # score评价等级参数差评为1、中评为2、好评为3，0为全部
        # sortType类型，6为时间排序，5为推荐排序
        # pageSize每页显示评价10条
        # page页数
        params = {
            'callback': 'fetchJSON_comment98vv10635',
            'productId': id,
            'score': score,
            'sortType': 6,
            'pageSize': 10,
            'isShadowSku': 0,
            'page': 0,
        }
        # 评价请求地址
        url = 'https://club.jd.com/comment/skuProductPageComments.action'
        # 发送请求
        evaluation_response = requests.get(url, params=params,headers=headers)
        if evaluation_response.status_code == 200:
            evaluation_response = evaluation_response.text
            try:
                # 去除json外层的括号与名称
                t = re.search(r'({.*})', evaluation_response).group(0)
            except Exception as e:
                print('评价的json数据匹配异常！')
            j = json.loads(t)  # 加载json数据
            commentSummary = j['comments']
            for comment in commentSummary:
                # 评价内容
                c_contetn = comment['content']
                # 时间
                c_time = comment['creationTime']
                # 京东昵称
                c_name = comment['nickname']
                # 好评差评 1差评 2-3 中评 4-5好评
                c_score = comment['score']
            # 判断没有指定的评价内容时
            if len(commentSummary) == 0:
                # 返回无
                return  '无'
            else:
                # 根据不同需求返回不同数据，这里仅返回最新的评价时间
                return  commentSummary[0]['creationTime']
