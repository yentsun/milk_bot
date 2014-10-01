import json
import datetime
import transaction
from collections import OrderedDict
from fabric.api import *
from milkpricereport.models import (ProductCategory, StorageManager,
                                    PriceReport)
from ZODB.FileStorage import FileStorage


@task
def output_data(days=14):
    """Generate JSON with data"""
    storage = StorageManager(FileStorage('storage.fs'))
    categories = ProductCategory.fetch_all(storage=storage)
    dates = [datetime.date.today() + datetime.timedelta(-1*count)
             for count in range(0, int(days))]
    result = dict()
    for category in categories:
        result[category.get_key()] = OrderedDict()
        for date in dates:
            data_dict = dict()
            prices = category.get_prices(date)
            if len(prices) > 0:
                data_dict['median'] = category.get_price(date, prices=prices)
                data_dict['min'] = min(prices)
                data_dict['max'] = max(prices)
                result[category.title][str(date)] = data_dict
    with open('data.json', 'w') as f:
        json.dump(result, f, indent=2)
    storage.close()


@task
def set_normalized_price():
    """Walk through all reports and set normalized price_value"""

    storage = StorageManager(FileStorage('storage.fs'))
    report_keys = PriceReport.fetch_all(storage)
    for report in report_keys:
        report.normalized_price_value = \
            report.get_normalized_price(report.price_value)
        print('Report {0} updated'.format(report.uuid))
    transaction.commit()
    storage.close()