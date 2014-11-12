from scrapy.spider import BaseSpider
from milkbot.items import MerchantItem


class UtkonosSpider(BaseSpider):

    name = "utkonos_spider"
    download_delay = 5
    allowed_domains = ["www.utkonos.ru"]
    start_urls = [
        #milk
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
        #sour cream
        'http://www.utkonos.ru/cat/catalogue/12?property[]=8:72',
        'http://www.utkonos.ru/cat/catalogue/12/page/2?property[]=8:72',
        'http://www.utkonos.ru/cat/catalogue/12/page/3?property[]=8:72',
        #egg
        'http://www.utkonos.ru/cat/catalogue/108/page/1',
        'http://www.utkonos.ru/cat/catalogue/108/page/2',
        #sunflower oil
        'http://www.utkonos.ru/cat/catalogue/43?property[]=61:430',
        'http://www.utkonos.ru/cat/catalogue/43/page/2?property[]=61:430',
        #bread
        'http://www.utkonos.ru/cat/catalogue/111',
        'http://www.utkonos.ru/cat/catalogue/111/page/2',
        'http://www.utkonos.ru/cat/catalogue/111/page/3',
        'http://www.utkonos.ru/cat/catalogue/111/page/4',
        #potato
        'http://www.utkonos.ru/cat/catalogue/28?catalogue_id=28&property'
        '%5B%5D=132%3A232043&property%5B%5D=20%3A237',
        #sugar
        'http://www.utkonos.ru/cat/catalogue/44?catalogue_id=44&property%5B%5D'
        '=63%3A437&property%5B%5D=65%3A436',
        #salt
        'http://www.utkonos.ru/cat/catalogue/44?property[]=63:434',
        'http://www.utkonos.ru/cat/catalogue/44/page/2?property%5B%5D=63:434'
    ]

    def parse(self, response):
        for sel in response.xpath("//div[@class='goods_container "
                                  "goods_view_box']/div[contains(@class, "
                                  "'goods_view')]"):
            item = MerchantItem()
            item['price_value'] = sel.xpath('form/input[@name="price"]/'
                                            '@value').extract()[0]
            item['merchant'] = 'utkonos'
            item['title'] = sel.xpath('a[@class="goods_caption"]/'
                                      '@title').extract()[0]
            item['url'] = sel.xpath('a[@class="goods_caption"]/'
                                    '@href').extract()[0]
            item['weight'] = sel.xpath(
                'div/div[@class="goods_weight"]'
                '/text()'
            ).extract()[0].split(' ')[0].replace(',', '.')
            yield item


class UtkonosTestSpider(UtkonosSpider):

    name = "utkonos_test_spider"
    start_urls = ['http://localhost:8080/page.html']