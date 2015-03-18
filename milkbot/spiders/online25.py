# -*- coding: utf-8 -*-

from scrapy.spider import BaseSpider
from milkbot.items import MerchantItem


class Online25Spider(BaseSpider):

    name = 'online25_spider'
    download_delay = 5
    allowed_domains = ['online25.ru']
    start_urls = [

        # milk
        'http://online25.ru/shop/food/dairy-products/milk/',

        # sour cream
        'http://online25.ru/shop/food/dairy-products/sour-cream/',

        # cheese
        'http://online25.ru/shop/food/cheeses/solid-semisolid/',

        # egg
        'http://online25.ru/shop/food/egg/',

        # sunflower oil
        'http://online25.ru/shop/food/butter-fat-products/vegetable-oil/'
        'sunflower-oil/',

        # bread

        # flour
        'http://online25.ru/shop/food/cereals/flour/',

        # fruit
        'http://online25.ru/shop/food/fresh-fruits/',

        # vegetables
        'http://online25.ru/shop/food/fresh-vegetables/',

        # sugar+salt
        'http://online25.ru/shop/food/cereals/sugar-salt/',

        # buckwheat+rice
        'http://online25.ru/shop/food/cereals/cereals/',

        # pasta
        'http://online25.ru/shop/food/cereals/pasta/',
    ]

    def parse(self, response):
        for item_cont in response.xpath('//div[@class="shop_item"]'):
            item = MerchantItem()
            item['merchant'] = u'Онлайн25'
            item['price_value'] = item_cont.xpath(
                './/div[@class="price"]/text()'
            ).extract()[0].split(' ')[0].replace(',', '.')
            if item['price_value'] != '0.00':
                item['title'] = item_cont.xpath(
                    './/div[@class="description_sell"]/p/a/@title').extract()[0]
                item['url'] = item_cont.xpath(
                    './/div[@class="description_sell"]/p/a/@href').extract()[0]

                yield item


class Online25TestSpider(Online25Spider):

    name = 'online25_test_spider'
    start_urls = ['http://online25.ru/shop/food/dairy-products/milk/']