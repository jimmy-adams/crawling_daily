# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from tutorial.items import TutorialItem
class BlogSpider(scrapy.Spider):
    name = 'Qingdao_daily'
    start_urls = ['http://www.dailyqd.com/epaper/html/2020-06/17/node_2.htm']

    def parse(self, response):
        print('receive')
        items = TutorialItem()
        items['Pubtime'] = response.css('div.dzb_time span::text').get() # get the current publish time of the daily, jihuidong
        for content in response.css('div.dzb_right_bt_nav li'):
            items['Url'] = content.css('span a::attr(href)').get() # store the link  jihuidong 2020/6/18
            items['Title'] = content.css('span a::text').get()     # store the title span is a label in html and css, jihuidong 2020/6/18
            sub_page = content.css('span a::attr(href)').get()
            if sub_page is not None:
               yield response.follow(sub_page,meta={'items': items},callback=self.sub_parse)
    def sub_parse(self, response):
        items = response.meta['items']
        content = response.css('div.dzb_dy_box')
        content1 = content.css('span.px12')
        final_text = []
        for content in content1:
           text = content.css('p::text')
           for sub_text in text:
              sub_text = sub_text.get()
              final_text.append(sub_text)
              
              
        items['Content'] = final_text
        yield items
            
        