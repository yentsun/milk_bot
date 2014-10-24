# -*- coding: utf-8 -*-

import json
import datetime
import transaction
from collections import OrderedDict
from fabric.api import *
from fabric.colors import *
from prettytable import PrettyTable
from milkpricereport.models import (ProductCategory, StorageManager,
                                    PriceReport, PackageLookupError, Reporter,
                                    Product, Merchant)
from ZODB.FileStorage import FileStorage

MULTIPLIER = 1


def get_datetimes(days):
    """Return list with days back range"""

    result = list()
    for count in range(0, int(days)):
        date = datetime.date.today() + datetime.timedelta(-1*MULTIPLIER*count)
        date_time = datetime.datetime.combine(date,
                                              datetime.datetime.now().time())
        result.append(date_time)
    return result


@task
def make_image(days):
    """Generate graph with matplotlib"""
    import matplotlib.pyplot as plt
    from matplotlib import dates as mdates
    from matplotlib import rc
    storage = StorageManager(FileStorage('storage.fs'))
    milk = ProductCategory.fetch('milk', storage)
    sour_cream = ProductCategory.fetch('sour cream', storage)
    egg = ProductCategory.fetch('chicken egg', storage)
    oil = ProductCategory.fetch('sunflower oil', storage)
    bread = ProductCategory.fetch('bread', storage)

    dates = get_datetimes(days)
    milk_prices = [milk.get_price(date) for date in dates]
    sc_prices = [sour_cream.get_price(date) for date in dates]
    egg_prices = [egg.get_price(date) for date in dates]
    oil_prices = [oil.get_price(date) for date in dates]
    bread_prices = [bread.get_price(date) for date in dates]

    fig = plt.figure(figsize=(8, 7))
    rc('font', family='Ubuntu')
    plt.plot_date(dates, sc_prices, '-', marker='.', label=u'сметана, 400г')
    plt.plot_date(dates, egg_prices, '-', marker='.', label=u'яйцо, 1 дес.')
    plt.plot_date(dates, oil_prices, '-', marker='.', label=u'масло под., 1л')
    plt.plot_date(dates, milk_prices, '-', marker='.', label=u'молоко, 1л')
    plt.plot_date(dates, bread_prices, '-', marker='.', label=u'хлеб, 500г')
    plt.ylabel(u'Средняя цена, руб.')
    plt.yticks([sc_prices[0], milk_prices[0], egg_prices[0],
                bread_prices[0], oil_prices[0]])
    plt.xticks(dates[0::7])
    fig.autofmt_xdate()
    ax = fig.add_subplot(111)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%y'))
    plt.title(u'Динамика цен на продукты питания, Москва')
    plt.legend(loc='center left')
    plt.grid(True)
    plt.show()
    plt.savefig('milkpriceresults.png')


@task
def deploy_graph(days=7):
    """Make and deploy graph to remote host"""
    execute(make_image, days)
    local('scp milkpriceresults.png ubuntu@alpha:~/www/korinets.name/images')


@task
def output_data(days=14):
    """Generate JSON with data"""
    storage = StorageManager(FileStorage('storage.fs'))
    categories = ProductCategory.fetch_all(storage)
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
    reports = PriceReport.fetch_all(storage)
    for report in reports:
        try:
            del report.product.package
            report.product.package = report.product.get_package()
            report.normalized_price_value = \
                report._get_normalized_price(report.price_value)
            print('Report {0} updated'.format(report.uuid))
        except PackageLookupError, e:
            print(e.message)
    transaction.commit()
    storage.close()


@task
def add(merchant_str, title, price_value, url, date_string=None):
    """Add price report"""
    storage = StorageManager(FileStorage('storage.fs'))
    reporter = Reporter.fetch('MilkBot cmd line', storage)
    if not reporter:
        reporter = Reporter('MilkBot cmd line')
        storage.register(reporter)
    merchant = Merchant.fetch(merchant_str.decode('utf-8'), storage)
    if not merchant:
        merchant = Merchant(merchant_str.decode('utf-8'))
        storage.register(merchant)
    category_key = ProductCategory.get_key_from_str(title.decode('utf-8'))
    if category_key:
        category = ProductCategory.fetch(category_key, storage)
        if not category:
            category = ProductCategory(category_key)
            storage.register(category)
        product = Product.fetch(title.decode('utf-8'), storage)
        if not product:
            product = Product(title.decode('utf-8'), category=category)
            storage.register(product)
        if date_string:
            date = datetime.datetime.strptime(date_string, '%d.%m.%Y')
        else:
            date = None
        try:
            report = PriceReport(date_time=date, product=product,
                                 merchant=merchant,
                                 price_value=float(price_value),
                                 reporter=reporter, url=url)
            storage.register(report)
            transaction.commit()
            print(green('Report added'))
        except PackageLookupError, e:
            print(e.message)
    storage.close()


@task
def display_category(category_key):
    """Display category data in table"""

    table = PrettyTable(['product', 'N', 'O',
                         'pack.'])
    table.align = 'l'
    keeper = StorageManager(FileStorage('storage.fs'))
    category = ProductCategory.fetch(category_key, keeper)
    min_package_ratio = category.get_data('min_package_ratio')
    products = category.products.values()
    if min_package_ratio:
        try:
            products = [product for product in products
                        if product.get_package().get_ratio(category) >=
                        float(min_package_ratio)]
        except PackageLookupError, e:
            print(e.message)
    sorted_products = sorted(products,
                             key=lambda pr: pr.get_last_reported_price())
    for num, product in enumerate(sorted_products):
        try:
            table.add_row([u'{}. {}'.format(num+1, product.title),
                          round(product.get_last_reported_price(), 2),
                          product.get_last_reported_price(normalized=False),
                          product.package])
        except TypeError:
            pass
    print(table)


@task
def stats(category_key, days=2):
    """Show daily statistics for a category"""
    table = PrettyTable(['date/time', 'report count', 'median', 'min',
                         'max'])
    table.align = 'l'
    dates = get_datetimes(days)
    keeper = StorageManager(FileStorage('storage.fs'))
    category = ProductCategory.fetch(category_key, keeper)
    for date in dates:
        table.add_row([str(date),
                       len(category.get_reports(date)),
                       category.get_price(date),
                       category.get_price(cheap=True),
                       max(category.get_prices(date))])
    print(table)