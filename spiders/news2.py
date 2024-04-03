import scrapy
from bs4 import BeautifulSoup
import requests
import json


class News2Spider(scrapy.Spider):
    name = "news2"
    allowed_domains = ["www.hindustantimes.com"]
    start_urls =  ["https://www.hindustantimes.com/world-news/us-news/diddydidit-sean-combs-pats-down-justin-bieber-to-check-for-a-wire-in-perturbing-viral-video-101712138347643.html"]
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


    def parse(self, response):
        content={'data':[]}
        req=requests.get(self.start_urls[0],headers=self.headers)       
        soup=BeautifulSoup(req.text,'html.parser')
        text=soup.find('div',class_='storyDetails').find_all('p')
        s=''
        if text:
            for t in text:
                # print(t.text)
                s+=t.text
        content['data'].append(s)

        with open('test2.json','w') as f:
            json.dump(content,f)




