# -*- coding: utf-8 -*-

import scrapy


class MerchantItem(scrapy.Item):
    """A general merchant product item"""
    price_value = scrapy.Field()
    merchant = scrapy.Field()
    title = scrapy.Field()
    sku = scrapy.Field()
    url = scrapy.Field()
