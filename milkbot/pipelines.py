# -*- coding: utf-8 -*-

import transaction
from ZODB.FileStorage import FileStorage
from scrapy.exceptions import DropItem
from milkpricereport.models import (PriceReport, Product, ProductCategory,
                                    Reporter, Merchant, StorageManager)


class PersistencePipeline(object):
    """Pipeline to persist items in ZODB"""

    def __init__(self):
        self.storage = StorageManager(FileStorage('storage.fs'))

    def process_item(self, item, spider):
        category = ProductCategory.fetch('milk', self.storage)
        cat_keyword = category.get_data('keyword')
        if cat_keyword not in item['title'].lower():
            raise DropItem(u'Dropping no-keyword title '
                           u'({0})'.format(item['title']))
        price_value = float(item['price_value'])
        product = Product.fetch(item['title'], self.storage)
        product.category = category
        category.add_products(product)
        reporter = Reporter.fetch(spider.name, self.storage)
        merchant = Merchant.fetch(item['merchant'], self.storage)
        merchant.location = 'Europe/Moscow'
        new_report = PriceReport(price_value=price_value,
                                 product=product,
                                 reporter=reporter,
                                 url=item['url'],
                                 merchant=merchant)
        self.storage.register(new_report)
        print(u'Added new report {0} to {1} category'.format(new_report,
                                                             category))
        return item

    def close_spider(self, spider):
        transaction.commit()
        self.storage.close()