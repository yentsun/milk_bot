# -*- coding: utf-8 -*-

from scrapy.spider import BaseSpider
from milkbot.items import MerchantItem


class MnogomartSpider(BaseSpider):

    name = 'mnogomart_spider'
    download_delay = 5
    allowed_domains = ['mnogomart.ru']
    start_urls = [

        # milk
        'http://www.mnogomart.ru/catalog/dairy/moloko/?SHOWALL_1=1',

        # sour cream
        'http://www.mnogomart.ru/catalog/dairy/smetana/',

        # cheese
        'http://www.mnogomart.ru/catalog/dairy/syry/?SHOWALL_1=1',

        # egg
        'http://www.mnogomart.ru/catalog/myaso-ptitsa/yaytso/',

        # sunflower oil
        'http://www.mnogomart.ru/catalog/bakaleya/maslo/?SHOWALL_1=1',

        # bread
        'http://www.mnogomart.ru/catalog/khleb/khleb/',
        'http://www.mnogomart.ru/catalog/khleb/batony_bagety/',

        # flour
        'http://www.mnogomart.ru/catalog/bakaleya/muka_i_vse_dlya_vypechki/',

        # fruit
        'http://www.mnogomart.ru/catalog/ovoshchi-frukty/svezhie_frukty/'
        '?SHOWALL_1=1',

        # vegetables
        'http://www.mnogomart.ru/catalog/ovoshchi-frukty/svezhie_ovoshchi/'
        '?SHOWALL_1=1',

        # sugar+salt
        'http://www.mnogomart.ru/catalog/bakaleya/sol_sakhar/?SHOWALL_1=1',

        # buckwheat+rice
        'http://www.mnogomart.ru/catalog/bakaleya/krupy/?SHOWALL_1=1',

        # pasta
        'http://www.mnogomart.ru/catalog/bakaleya/makarony/?SHOWALL_1=1',
    ]

    def parse(self, response):
        for item_cont in response.xpath('//li[@class="item-catalog-list item"]'):
            item = MerchantItem()
            item['merchant'] = u'Многомарт'
            item['price_value'] = item_cont.xpath(
                './/span[@class="sum"]/text()').extract()[0]
            item['title'] = item_cont.xpath(
                './/div[@class="name-wrap"]/text()').extract()[0]
            item['sku'] = item_cont.xpath(
                './/input[@name="id"]/@value').extract()[0]
            item['url'] = item_cont.xpath('.//a/@href').extract()[0]

            yield item


class MnogomartTestSpider(MnogomartSpider):

    name = 'mnogomart_test_spider'
    start_urls = ['http://www.mnogomart.ru/catalog/dairy/moloko/']