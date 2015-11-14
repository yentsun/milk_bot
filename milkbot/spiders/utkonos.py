# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from milkbot.items import MerchantItem


class UtkonosSpider(BaseSpider):

    name = "utkonos_spider"
    download_delay = 5
    allowed_domains = ["www.utkonos.ru"]
    start_urls = [

        # milk
        'http://www.utkonos.ru/cat/catalogue/11/page/1?property[]=4:4'
        '&property[]=5:5',
        'http://www.utkonos.ru/cat/catalogue/11/page/2?property[]=4:4'
        '&property[]=5:5',
        'http://www.utkonos.ru/cat/catalogue/11/page/3?property[]=4:4'
        '&property[]=5:5',
        'http://www.utkonos.ru/cat/catalogue/11/page/4?property[]=4:4'
        '&property[]=5:5',
        'http://www.utkonos.ru/cat/catalogue/11/page/5?property[]=4:4'
        '&property[]=5:5',
        'http://www.utkonos.ru/cat/catalogue/11/page/6?property[]=4:4'
        '&property[]=5:5',

        # sour cream
        'http://www.utkonos.ru/cat/catalogue/12?property[]=8:72',
        'http://www.utkonos.ru/cat/catalogue/12/page/2?property[]=8:72',
        'http://www.utkonos.ru/cat/catalogue/12/page/3?property[]=8:72',

        # cheese
        'http://www.utkonos.ru/cat/16',
        'http://www.utkonos.ru/cat/catalogue/16/page/2',
        'http://www.utkonos.ru/cat/catalogue/16/page/3',
        'http://www.utkonos.ru/cat/catalogue/16/page/4',
        'http://www.utkonos.ru/cat/catalogue/16/page/5',
        'http://www.utkonos.ru/cat/catalogue/16/page/6',
        'http://www.utkonos.ru/cat/catalogue/16/page/7',
        'http://www.utkonos.ru/cat/catalogue/16/page/8',

        # egg
        'http://www.utkonos.ru/cat/catalogue/108/page/1',
        'http://www.utkonos.ru/cat/catalogue/108/page/2',

        # sunflower oil
        'http://www.utkonos.ru/cat/catalogue/43?property[]=61:430',
        'http://www.utkonos.ru/cat/catalogue/43/page/2?property[]=61:430',

        # bread
        'http://www.utkonos.ru/cat/catalogue/111',
        'http://www.utkonos.ru/cat/catalogue/111/page/2',
        'http://www.utkonos.ru/cat/catalogue/111/page/3',
        'http://www.utkonos.ru/cat/catalogue/111/page/4',

        # fruit
        'http://www.utkonos.ru/cat/29',
        'http://www.utkonos.ru/cat/catalogue/29/page/2'

        # vegetables
        'http://www.utkonos.ru/cat/catalogue/28',
        'http://www.utkonos.ru/cat/catalogue/28/page/2',
        'http://www.utkonos.ru/cat/catalogue/28/page/3',
        'http://www.utkonos.ru/cat/catalogue/28/page/4',
        'http://www.utkonos.ru/cat/catalogue/28/page/5',

        # sugar
        'http://www.utkonos.ru/cat/catalogue/44?catalogue_id=44&property%5B%5D'
        '=63%3A437&property%5B%5D=65%3A436',

        # salt
        'http://www.utkonos.ru/cat/catalogue/44?property[]=63:434',
        'http://www.utkonos.ru/cat/catalogue/44/page/2?property%5B%5D=63:434',

        # flour
        'http://www.utkonos.ru/cat/45',
        'http://www.utkonos.ru/cat/catalogue/45/page/2',
        'http://www.utkonos.ru/cat/catalogue/45/page/3',
        'http://www.utkonos.ru/cat/catalogue/45/page/4',

        # buckwheat
        'http://www.utkonos.ru/cat/catalogue/41?catalogue_id=41&property%5B%5D'
        '=56%3A410',
        'http://www.utkonos.ru/cat/catalogue/41/page/2?property%5B%5D=56:410',

        # rice
        'http://www.utkonos.ru/cat/catalogue/41?catalogue_id=41&property%5B%5D'
        '=56%3A409',
        'http://www.utkonos.ru/cat/catalogue/41/page/2?property%5B%5D=56:409',
        'http://www.utkonos.ru/cat/catalogue/41/page/3?property%5B%5D=56:409',

        # pasta
        'http://www.utkonos.ru/cat/catalogue/42',
        'http://www.utkonos.ru/cat/catalogue/42/page/2',
        'http://www.utkonos.ru/cat/catalogue/42/page/3',
        'http://www.utkonos.ru/cat/catalogue/42/page/4',
        'http://www.utkonos.ru/cat/catalogue/42/page/5',
        'http://www.utkonos.ru/cat/catalogue/42/page/6',
        'http://www.utkonos.ru/cat/catalogue/42/page/7',
        'http://www.utkonos.ru/cat/catalogue/42/page/8',
        'http://www.utkonos.ru/cat/catalogue/42/page/9',
        'http://www.utkonos.ru/cat/catalogue/42/page/10',
        'http://www.utkonos.ru/cat/catalogue/42/page/11'
    ]

    def parse(self, response):

        for sel in response.xpath("//div[@class='goods_view_block']"
                                  "/div[@class='goods_view']"):
            item = MerchantItem()
            item['price_value'] = sel.xpath('.//input[@name="price"]/'
                                            '@value').extract()[0]
            item['merchant'] = u'Утконос'
            item['title'] = sel.xpath('a[@class="goods_caption"]/'
                                      '@title').extract()[0]
            item['sku'] = sel.xpath('.//input[@name="original_id"]/'
                                    '@value').extract()[0]
            item['url'] = sel.xpath('a[@class="goods_caption"]/'
                                    '@href').extract()[0]
            yield item


class UtkonosTestSpider(UtkonosSpider):

    name = "utkonos_test_spider"
    start_urls = ['http://localhost:8080/page.html']