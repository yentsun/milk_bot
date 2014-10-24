# -*- coding: utf-8 -*-

import transaction
import logging
from ZODB.FileStorage import FileStorage
from scrapy.exceptions import DropItem
from milkpricereport.models import (PriceReport, Product, ProductCategory,
                                    Reporter, Merchant, StorageManager,
                                    CategoryLookupError, PackageLookupError)

logging.basicConfig(filename='dropped.log', level=logging.DEBUG)


class PersistencePipeline(object):
    """Pipeline to persist items in ZODB"""

    def __init__(self):
        self.keeper = StorageManager(FileStorage('storage.fs'))
        self.errors = list()
        self.success = list()

    def process_item(self, item, spider):

        merchant = Merchant.fetch(item['merchant'], self.keeper)
        reporter = Reporter.acquire(spider.name, self.keeper)
        try:
            report, stats = PriceReport.assemble(
                price_value=float(item['price_value']),
                product_title=item['title'],
                url=item['url'],
                merchant=merchant,
                reporter=reporter,
                storage_manager=self.keeper
            )
            self.success.append(report)
        except CategoryLookupError, e:
            logging.debug(e.message.encode('utf-8'))
            self.errors.append(e)
            raise DropItem(e.message)
        except PackageLookupError, e:
            logging.debug(e.message.encode('utf-8'))
            self.errors.append(e)
            raise DropItem(e.message.encode('utf-8'))

        return item

    def close_spider(self, spider):

        if len(self.success) > 0:
            transaction.commit()
        else:
            transaction.abort()
        self.keeper.close()