import requests
from lxml import etree
from random import randint

def get_joke():
    url="http://www.qiushibaike.com/text/page/"+ str(randint(1,5))
    r = requests.get(url)
    tree = etree.HTML(r.text)
    contentlist = tree.xpath('//div[@class="content"]/span')
    jokes = []
    for content in contentlist:
        content = content.xpath('string(.)') # string() 函数将所有子文本串联起来，# 必须传递单个节点，而不是节点集。
        if '查看全文' in  content:  # 忽略包含“查看原文”笑话
            continue
        jokes.append(content)
    joke = jokes[randint(1, len(jokes))].strip()
    return joke

if __name__ == "__main__":
    content = get_joke()
    print(content)
