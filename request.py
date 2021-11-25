import requests

import bs4
from bs4 import BeautifulSoup
import re

if __name__ == "__main__":
    # markup = '<span title="Apple" class="column stock-name">Alibaba Group Holding Ltd</span>'
    # sp = BeautifulSoup(markup, 'html.parser')
    # print(sp.span['class'])
    # print(sp.span.attrs)
    # print(sp.string)

    # r = requests.get('https://www.oschina.net')
    # status_code = r.status_code
    # print(status_code)
    # print(f'html: {r.text}')
    # sp2 = BeautifulSoup(r.text, 'html.parser')
    # ps = sp2.find_all('p', 'line-clamp')
    # for p in ps:
    #     print(p.string)

    # r = requests.get('https://irdms-manager.bozhon.com/api/web-developer/v1/res/document/type/2')
    # res = r.json()
    # for i in res['data']:
    # print(i['documentUrl'])
    #r = requests.get("https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2509&k=&num=50&page=1&r=0.4560737642653927&callback=jQuery111201906300914475363_1637304659851&_=1637304659854")
    #print(r.text.encode("utf-8").decode("unicode-escape"))

    s = 0
    # 网站最新更新需要添加headers属性才能正常获取源码
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    r = requests.get(url='https://book.douban.com/subject/bookid/comments/', headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    pattern = soup.find_all('span', 'short')
    for item in pattern:
        print(item.string)
    pattern_s = re.compile('<span class="user-stars allstar(.*?) rating"')
    p = re.findall(pattern_s, r.text)
    for star in p:
        s += int(star)
    print(s)


