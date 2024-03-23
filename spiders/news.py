import scrapy
import re

class NewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["timesofindia.indiatimes.com"]
    start_urls = ["https://timesofindia.indiatimes.com"]

    def parse(self, response):
        news=response.css("a.Hn2z7").getall()
        print("-*-"*30)
        lis=[]
        for n in news:
            link=re.search(r'href="([^"]+\.cms)"',n)
            if link:
                lis.append(link.group(1))
             
        for l in lis:
            yield{"news data":l}
            print('\n')
        # yield {"news : ":news}
