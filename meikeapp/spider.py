# 需要调用的requests 库和 BeautifulSoup库中的bs4工具
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
class news:
    title=''
    url=''
    def __init__(self,title,url):
        self.title=title
        self.url=url

def getnews():

    url = 'http://www.sohu.com'
    headers= {'User-Agent':'Macintosh; Intel Mac OS X 10.12'}
    r = requests.get(url, headers=headers)
    print(r)
    soup = BeautifulSoup(r.text, 'html.parser')

    html = soup.find_all('a',{"class":""})
    newslist=[]
    for title in html:
        nurl=title.get('href')
        t=str(title.text)
        if t.__len__()>10:
            t=t.replace("\n","").replace("\r","")
            newslist.append(news(t,nurl))
    return newslist