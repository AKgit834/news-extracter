# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from bs4 import BeautifulSoup

class InqbatorPipeline:
    def process_item(self, item, spider):
        # 
        # adapter=ItemAdapter(item)
        # field_names=adapter.field_names()
        # for field_name in field_names:
        #     soup=BeautifulSoup(field_name,'html.parser')
        pass
