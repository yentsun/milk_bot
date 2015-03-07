# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from milkbot.items import MerchantItem


class MetroSpider(BaseSpider):

    name = "metro_spider"
    download_delay = 5
    allowed_domains = ['www.metro-cc.ru']
    start_urls = [

        # milk
        'http://msk.metro-cc.ru/category/produkty/molochnye/moloko?&limit=200',

        # sour cream
        'http://msk.metro-cc.ru/category/produkty/molochnye/smetana?'
        '&limit=200',

        # cheese
        'http://msk.metro-cc.ru/category/produkty/syrnye/tverdye-syry?price_'
        'from=0&price_to=0&brands=&sorting=0&limit=200',

        # egg
        'http://msk.metro-cc.ru/category/produkty/syrnye/yajca-kurinye',

        # sunflower oil
        'http://msk.metro-cc.ru/category/produkty/bakaleya/rastitelnoe-maslo?'
        '&limit=200',

        # bread
        'http://msk.metro-cc.ru/category/produkty/hlebobulochnye-izdeliya/'
        'baton-lavash?&limit=200',

        # vegetables
        'http://msk.metro-cc.ru/category/produkty/ovoschi-griby/'
        '101009001-svezhie?&limit=200',

        # fruit
        'http://msk.metro-cc.ru/category/produkty/frukty-yagody/'
        '101010001-svezhye?&limit=200'

        # flour
        'http://msk.metro-cc.ru/category/produkty/bakaleya/101004004-vypechka?'
        'price_from=0&price_to=0&brands=&attrs=&sorting=0&limit=400'

        # sugar+salt
        # 'http://msk.metro-cc.ru/category/produkty/bakaleya/sahar-sol?&limit=200'

        # buckwheat+rice
        'http://msk.metro-cc.ru/category/produkty/bakaleya/krupy?&limit=200',

        # pasta
        'http://msk.metro-cc.ru/category/produkty/bakaleya/makaronnye-izdeliya'
        '?&limit=200',
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="items"]/'
                                  'div[@class="catalog-i"]'):
            item = MerchantItem()
            mult = int(sel.xpath('.//div[@class="bottom-line_item _count"]/'
                                 'span/text()').extract()[0].split(' ')[0])
            try:
                int_ = sel.xpath('.//span[@class="int"]/text()').extract()[0]
                decimal_ = sel.xpath('.//span[@class="float"]/'
                                     'text()').extract()[0]
                item['price_value'] = u'{}.{}'.format(int_, decimal_)
                if mult > 1:
                    item['price_value'] = float(item['price_value']) / mult
            except IndexError:
                item['price_value'] = None
            item['merchant'] = u'МЕТРО Кэш энд Керри'

            item['title'] = sel.xpath('.//div[@class="catalog-i_title"]'
                                      '/span/text()').extract()[0].strip()
            item['url'] = sel.xpath('.//a[@class="catalog-i_link"]'
                                    '/@href').extract()[0]

            yield item


class MetroTestSpider(MetroSpider):

    name = "metro_test_spider"
    start_urls = ['http://localhost:8080/page.html']