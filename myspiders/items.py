# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspidersItem(scrapy.Item):
    # define the fields for your item here like:
    # 老师的姓名
    name = scrapy.Field()
    # 老师的职称
    title = scrapy.Field()
    # 老师的信息
    info = scrapy.Field()
    #pass
