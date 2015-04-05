# -*- coding: utf-8 -*-

import requests
from scrapy.exceptions import DropItem


class PriceWatchPipeline(object):
    """Pipeline sending reports to a Price Watch app"""

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

        url = 'http://localhost:6543/reports'
        auth = None
        if hasattr(spider, 'target'):
            target = getattr(spider, 'target')
            if target == 'food-price.net':
                from requests.auth import HTTPBasicAuth
                url = 'http://food-price.net/reports'
                with open('security/{}'.format(target), 'r') as f:
                    user, password = f.readline().split(': ')
                    auth = HTTPBasicAuth(user, password)
        response = requests.post(url, data=self.payload, auth=auth)
        if response.status_code == 200:
            print(response.json())
        else:
            print(response.text)
            raise Exception('Server error!')
