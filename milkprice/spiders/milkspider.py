import scrapy


class MilkSpider(scrapy.Spider):
    name = "MilkSpider"
    allowed_domains = ["www.utkonos.ru"]
    start_urls = [
        "http://www.utkonos.ru/cat/catalogue/11/page/1"
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="goods_view_box"]'):
            id_ = sel.xpath('@data-item_id').extract()
            title = sel.xpath('a[@class="goods_caption"]/'
                              '@title').extract()
            weight = sel.xpath('div/div[@class="goods_weight"]'
                               '/text()').extract()
            price = sel.xpath('form/input[@name="price"]/@value').extract()
            print(id_, title, weight, price)