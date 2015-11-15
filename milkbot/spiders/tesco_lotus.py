# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from milkbot.items import MerchantItem


class TescoLotusSpider(BaseSpider):

    name = "tesco_spider"
    download_delay = 5
    allowed_domains = ['shoponline.tescolotus.com']
    start_urls = [

        # milk
        'http://shoponline.tescolotus.com/en-GB/Search/List?searchQuery='
        'milk&Hierarchy=Department%3A11793%3AMilk%2BAisle%3A11794%3A'
        'Fresh%20Milk&Shelf=4294966662%2B4294966663',
        'http://shoponline.tescolotus.com/en-GB/Search/List?searchQuery='
        'milk&pageNo=2&SortBy=Relevance&Hierarchy=Department%3A11793%3A'
        'Milk%2BAisle%3A11794%3AFresh%20Milk&Shelf=4294966662%2B4294966663'

        # sour cream
        'http://shoponline.tescolotus.com/en-GB/Product/BrowseProducts?'
        'taxonomyId=Cat00001336',

        # cheese
        'http://shoponline.tescolotus.com/en-GB/Search/List?searchQuery='
        'cheese&Search=Search&Hierarchy=Department%3A11436%3ADairy%C2%A0&'
        'Shelf=4294966675%2B4294966687%2B4294966223%2B4294966676',
        'http://shoponline.tescolotus.com/en-GB/Search/List?searchQuery='
        'cheese&pageNo=2&SortBy=Relevance&Hierarchy=Department%3A11436%3A'
        'Dairy%C2%A0&Shelf=4294966675%2B4294966687%2B4294966223%2B4294966676',
        'http://shoponline.tescolotus.com/en-GB/Search/List?searchQuery='
        'cheese&pageNo=3&SortBy=Relevance&Hierarchy=Department%3A11436%3A'
        'Dairy%C2%A0&Shelf=4294966675%2B4294966687%2B4294966223%2B4294966676',
        'http://shoponline.tescolotus.com/en-GB/Search/List?searchQuery='
        'cheese&pageNo=4&SortBy=Relevance&Hierarchy=Department%3A11436%3A'
        'Dairy%C2%A0&Shelf=4294966675%2B4294966687%2B4294966223%2B4294966676',
        'http://shoponline.tescolotus.com/en-GB/Search/List?searchQuery='
        'cheese&pageNo=5&SortBy=Relevance&Hierarchy=Department%3A11436%3A'
        'Dairy%C2%A0&Shelf=4294966675%2B4294966687%2B4294966223%2B4294966676',
        'http://shoponline.tescolotus.com/en-GB/Search/List?searchQuery='
        'cheese&pageNo=6&SortBy=Relevance&Hierarchy=Department%3A11436%3A'
        'Dairy%C2%A0&Shelf=4294966675%2B4294966687%2B4294966223%2B4294966676',
        'http://shoponline.tescolotus.com/en-GB/Search/List?searchQuery='
        'cheese&pageNo=7&SortBy=Relevance&Hierarchy=Department%3A11436%3A'
        'Dairy%C2%A0&Shelf=4294966675%2B4294966687%2B4294966223%2B4294966676'

        # egg
        'http://shoponline.tescolotus.com/en-GB/Product/BrowseProducts?'
        'taxonomyId=Cat00001341&Shelf=4294966312',

        # sunflower oil
        'http://shoponline.tescolotus.com/en-GB/Product/BrowseProducts?'
        'taxonomyId=Cat00001414',

        # bread
        'http://shoponline.tescolotus.com/en-GB/Product/BrowseProducts?'
        'taxonomyId=Cat00002779',

        # fruit
        'http://shoponline.tescolotus.com/en-GB/Product/BrowseProducts?'
        'taxonomyId=Cat00002617',

        # vegetables
        'http://shoponline.tescolotus.com/en-GB/Product/BrowseProducts?'
        'taxonomyId=Cat00001165',

        # sugar
        'http://shoponline.tescolotus.com/en-GB/Product/BrowseProducts?'
        'taxonomyId=Cat00002440',

        # salt
        'http://shoponline.tescolotus.com/en-GB/Product/BrowseProducts?'
        'taxonomyId=Cat00002445',

        # flour
        'http://shoponline.tescolotus.com/en-GB/Product/BrowseProducts?'
        'taxonomyId=Cat00001483',

        # rice
        'http://shoponline.tescolotus.com/en-GB/Product/BrowseProducts?'
        'taxonomyId=Cat00001454',
        'http://shoponline.tescolotus.com/en-GB/Product/BrowseProducts?'
        'taxonomyID=Cat00001454&pageNo=2',
        'http://shoponline.tescolotus.com/en-GB/Product/BrowseProducts?'
        'taxonomyID=Cat00001454&pageNo=3',
        'http://shoponline.tescolotus.com/en-GB/Product/BrowseProducts?'
        'taxonomyID=Cat00001454&pageNo=4',
        'http://shoponline.tescolotus.com/en-GB/Product/BrowseProducts?'
        'taxonomyID=Cat00001454&pageNo=5',
        'http://shoponline.tescolotus.com/en-GB/Product/BrowseProducts?'
        'taxonomyID=Cat00001454&pageNo=6',

        # pasta
        'http://shoponline.tescolotus.com/en-GB/Product/BrowseProducts?'
        'taxonomyId=Cat00002483',
        'http://shoponline.tescolotus.com/en-GB/Product/BrowseProducts?'
        'taxonomyID=Cat00002483&pageNo=2',
        'http://shoponline.tescolotus.com/en-GB/Product/BrowseProducts?'
        'taxonomyID=Cat00002483&pageNo=3'
    ]

    def parse(self, response):

        for sel in response.xpath("//div[@id='listedProductItems']"
                                  "//div[@class='t product']"):
            item = MerchantItem()
            price_in_baht = sel.xpath('.//span[@class="linePrice"]'
                                      '/text()').extract()[0].split(' ')[1]
            item['price_value'] = float(price_in_baht) * 1.86095327
            item['merchant'] = 'Tesco Lotus'
            item['title'] = sel.xpath('.//div[@class="description"]/'
                                      'h2/a/@title').extract()[0]
            item['sku'] = sel.xpath('.//input[@name="pIs.index"]/'
                                    '@value').extract()[0]
            item['url'] = sel.xpath('.//div[@class="description"]/'
                                    'h2/a/@href').extract()[0]
            yield item


class TescoTestSpider(TescoLotusSpider):

    name = "tesco_test_spider"
    start_urls = ['http://localhost:8080/page.html']
