import scrapy
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

class NewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["timesofindia.indiatimes.com"]
    start_urls = ["https://timesofindia.indiatimes.com"]

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    
    def parse(self, response):
        content={'data':[]}
        news=response.css("a.Hn2z7").getall()
        lis=[]
        for n in news:
            link=re.search(r'href="([^"]+\.cms)"',n)
            if link:
                lis.append(link.group(1))
        for l in lis:
            try:
            #yield response.follow(l,self.parse_page)
                r=requests.get(l,headers=self.headers)
                soup=BeautifulSoup(r.text,'html.parser')             
                text=soup.find('div', class_='_s30J clearfix')
                if text:
                    #print(text.get_text())
                    content['data'].append(text.get_text())
            except:
                print("connection error")
        #df=pd.DataFrame.from_dict(content)
        #df.to_csv('test.csv')

        with open('test.json','w') as f:
            json.dump(content,f)


