# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 新闻标题
    Title = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 新闻来源
    source = scrapy.Field()
    # 新闻发布时间
    Pubtime = scrapy.Field()
    # 新闻内容
    Content = scrapy.Field()
    # 新闻标签
    tags = scrapy.Field()
    # url
    Url = scrapy.Field()

