# -*- coding: utf-8 -*-

import scrapy


class MerchantItem(scrapy.Item):

    price_value = scrapy.Field()
    merchant = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
