# -*- coding: utf-8 -*-

import requests
from scrapy.exceptions import DropItem


class PersistencePipeline(object):
    """Pipeline to persist items in ZODB"""

    def __init__(self):
        self.payload = list()

    def process_item(self, item, spider):

        if item['price_value'] is None:
            raise DropItem
        self.payload.append(('price_value', item['price_value']))
        self.payload.append(('url', item['url']))
        self.payload.append(('product_title', item['title']))
        self.payload.append(('merchant_title', item['merchant']))
        self.payload.append(('reporter_name', spider.name))

        return item

    def close_spider(self, spider):

        response = requests.post('http://food-price.net/reports',
                                 data=self.payload)
        if response.status_code == 200:
            print(response.json())
        else:
            print(response.text)
            raise Exception('Server error!')