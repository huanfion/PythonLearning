# -*- encoding=utf-8 -*-
#https://mp.weixin.qq.com/s?__biz=MzUyNDY2MDgyMw==&mid=2247483850&idx=1&sn=0de2fbfe845589b1c0cae689ba080ab7&scene=19#wechat_redirect
# 爬虫豆瓣音乐

import requests
import bs4

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5702.400 QQBrowser/10.2.1893.400"}

def getMovielist():
    urls=["https://movie.douban.com/top250?start={}".format(str(i)) for i in range(0,25,25)]
    for url in urls:
        resp=requests.get(url,headers)
        resp.encoding="utf-8"
        soup=bs4.BeautifulSoup(resp.text,"html.parser")
        title=soup.select(".grid_view > li >.item > .info > a > span")
        print(soup.get_text())

if(__name__=="__main__"):
    getMovielist()