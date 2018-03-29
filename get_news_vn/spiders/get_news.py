# -*- coding: utf-8 -*-
import scrapy
import urlparse
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from craigslist_sample.items import CraigslistSampleItem

BMSID = 42
class get_news(scrapy.Spider):
    name = 'get_news'
 
    start_urls = ['https://tuoitre.vn/the-gioi/trang-1.htm']
    num_pages = 3
    
    for page in range(2, num_pages):
        start_urls.append('https://tuoitre.vn/the-gioi/trang-%d.htm'%page)
    
    def parse(self, response):
        domain_name = 'https://tuoitre.vn'      
        global BMSID
        BMSModel = []
        #Extracting the content using css selectors
        #
        news_name = response.xpath("//div[@class='block-left-info-fl']//a/@href").extract()
        new_url = response.xpath("//div[@class='block-left-info-fl']//p/text()").extract() 
        for i in range(len(products_url)):
            # ... compute some result based on item ...
            BMSID = BMSID + 1
            BMSModel.append('BMS%04d'%BMSID)
            url = urlparse.urljoin(domain_name,new_url[i])
            new_url[i] = url
                         
 
        for item in zip(products_name,products_url,BMSModel):    
            #create a dictionary to store the scraped info
            scraped_info = {
                'new_name' : item[0],
                'new_url' : item[1],
                'new_model' : item[2],
                #'new_model' : item[1]
 
            }
 
            #yield or give the scraped info to scrapy
            yield scraped_info