# -*-encoding:utf-8 -*-
'''
房天下租房信息爬虫
'''
import requests
import bs4
def getlastdata():
    headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5702.400 QQBrowser/10.2.1893.400"}

    # get请求
    resp=requests.get("http://zu.gz.fang.com/",headers)
    '''
    print(resp.encoding)
    resp.encoding="gbk"
    print(resp.text)
    '''
    resp.encoding = "gbk"
    soup=bs4.BeautifulSoup(resp.text,"html.parser")
    title=soup.find_all("p","title")

    price=soup.select("div.houseList > dl > dd > div.moreInfo > p > span")

    concretedata =soup.select("#listBox .houseList > dl > dd > p.font15.mt12.bold")
    for title,price, concretedata  in zip(title,price,concretedata ):
        lastdata={
            "title":title.get_text().strip(),
            "price":price.get_text().strip(),
            "concretedata":concretedata.get_text().strip()
        }
        print(lastdata)

if __name__=="__main__":
    getlastdata()
#print(soup.prettify())