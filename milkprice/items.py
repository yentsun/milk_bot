# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MilkpriceItem(scrapy.Item):

    id_ = scrapy.Field()
    title = scrapy.Field()
    volume = scrapy.Field()
    price = scrapy.Field()
