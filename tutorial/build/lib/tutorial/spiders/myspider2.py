# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem
import sys
sys.path.append('..')
from tutorial.spiders import myspider
class BlogSpider1(scrapy.Spider):
    name = 'Qingdao_daily1'
    start_urls = ['http://www.dailyqd.com/epaper/']
    #start_urls = ['http://www.dailyqd.com/epaper/index_4.html']

    print(myspider.BlogSpider.name)
    def parse(self, response):
       link = response.xpath("//div[@id='displaypagenum']")         # go to <div id = 'displaypagenum'>  :ji huidong 2020/06/20
       Total_pagenum = link.css('::attr(totalcount)').extract()     # get the totalcount attribute value ; ji huidong 2020/06/20
       Total_pagenum = int(Total_pagenum[0])                        # convert the pagenumber string into an int; ji huidong 2020/06/20
       Current_pagenum = link.css('::attr(currentpage)').extract()  # get the currentpage attribute value; ji huidong; 2020/06/20
       Current_pagenum = int(Current_pagenum[0])                    # convert the currentpage attribute to an int; ji huidong;2020/06/20
       papers_link = response.xpath("//div[@class='papper']")    
       #print(Current_pagenum)
       sub_page = link.xpath("//a[@class='aa']")
       for element in sub_page:
           if element.css('a::text').get() == '下一页':
              #print('found it')
              sub_page = element
              sub_page = sub_page.css('::attr(href)').get()
           else:
              sub_page = None
       #yield {'subpage': sub_page}
       #print('The page link is:',sub_page)
       
       for paper_link in papers_link:
           #===========function block for data fetching; Ji huidong;2020/06/22========#
           Info_date = paper_link.css('p::text').extract()     
           year = Info_date[0][0:4]
           month = Info_date[0][5:7]
           day = Info_date[0][8:10]
           data=year+'-'+month+'/'+day
           #===========================================================================#
           href='http://www.dailyqd.com/epaper/html/'+data+'/node_2.htm'# Link combination; Ji huidong; 2020/06/22
           yield response.follow(href,callback=myspider.BlogSpider().parse)
           #yield {'link':href}
       
       if sub_page is not None:
          #print('scanning')
          yield response.follow(sub_page,callback=self.parse)
          
       
       

        

            
        