import scrapy
import re

class NewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["timesofindia.indiatimes.com"]
    start_urls = ["https://timesofindia.indiatimes.com"]

    def parse(self, response):
        news=response.css("a.Hn2z7").getall()
        lis=[]
        for n in news:
            link=re.search(r'href="([^"]+\.cms)"',n)
            if link:
                lis.append(link.group(1))
        print("\n"*5,"content")
        
        for l in lis:
            yield response.follow(l,self.parse_page)
               
        print("\n"*5)

    def parse_page(self,response):
        #scrapy.req
        content=response.css('div[class^="_s30J"]').get()
        
        yield {'content':content}



        # if div_text:
        #     extracted_text = scrapy.Selector(text=div_text).xpath('//text()').getall()
        #    
        #     extracted_text = ''.join(extracted_text).strip()
        #     yield{'text':extracted_text}
        # else:
        #     pass




