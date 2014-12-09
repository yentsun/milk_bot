# -*- coding: utf-8 -*-

import requests


class PersistencePipeline(object):
    """Pipeline to persist items in ZODB"""

    def __init__(self):
        self.payload = list()

    def process_item(self, item, spider):

        self.payload.append(('url', item['url']))
        self.payload.append(('price_value', item['price_value']))
        self.payload.append(('product_title', item['title']))
        self.payload.append(('merchant_title', item['merchant']))
        self.payload.append(('reporter_name', spider.name))

        return item

    def close_spider(self, spider):

        response = requests.post('http://localhost:6543/reports',
                                 data=self.payload)
        if response.status_code == 200:
            print(response.json())
        if response.status_code == 500:
            print(response.text)
            raise Exception('Server error!')