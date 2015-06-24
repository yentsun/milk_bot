# -*- coding: utf-8 -*-

from scrapy.spider import BaseSpider
from milkbot.items import MerchantItem


class KorzinaSpider(BaseSpider):

    name = 'korzina_spider'
    download_delay = 5
    allowed_domains = ['korzinamag.ru']
    start_urls = [

        # milk
        'http://korzinamag.ru/catalog/produkty_pitaniya/molochnye_produkty/moloko_slivki_molochnye_kokteyli/moloko_toplenoe/?_PRICE_TYPE=10#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/molochnye_produkty/moloko_slivki_molochnye_kokteyli/moloko_toplenoe/?_PRICE_TYPE=10&PAGEN_1=2#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/molochnye_produkty/moloko_slivki_molochnye_kokteyli/moloko_toplenoe/?_PRICE_TYPE=10&PAGEN_1=3#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/molochnye_produkty/moloko_slivki_molochnye_kokteyli/moloko_toplenoe/?_PRICE_TYPE=10&PAGEN_1=4#top_catalog_position',

        # sour cream
        'http://korzinamag.ru/catalog/produkty_pitaniya/molochnye_produkty/kislomolochnye_produkty/smetana/#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/molochnye_produkty/kislomolochnye_produkty/smetana/?_PRICE_TYPE=10&PAGEN_1=2#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/molochnye_produkty/kislomolochnye_produkty/smetana/?_PRICE_TYPE=10&PAGEN_1=3#top_catalog_position',

        # cheese
        'http://korzinamag.ru/catalog/produkty_pitaniya/molochnye_produkty/syry/?_PRICE_TYPE=10#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/molochnye_produkty/syry/?_PRICE_TYPE=10&PAGEN_1=2#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/molochnye_produkty/syry/?_PRICE_TYPE=10&PAGEN_1=3#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/molochnye_produkty/syry/?_PRICE_TYPE=10&PAGEN_1=4#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/molochnye_produkty/syry/?_PRICE_TYPE=10&PAGEN_1=5#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/molochnye_produkty/syry/?_PRICE_TYPE=10&PAGEN_1=6#top_catalog_position',

        # egg
        'http://korzinamag.ru/catalog/produkty_pitaniya/myaso_ptitsa_yaytsa/yaytsa/#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/myaso_ptitsa_yaytsa/yaytsa/?_PRICE_TYPE=10&PAGEN_1=2#top_catalog_position',

        # sunflower oil
        'http://korzinamag.ru/catalog/produkty_pitaniya/bakaleya_1/maslo_rastitelnoe/podsolnechnoe/#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/bakaleya_1/maslo_rastitelnoe/podsolnechnoe/?_PRICE_TYPE=10&PAGEN_1=2#top_catalog_position',

        # bread
        'http://korzinamag.ru/catalog/produkty_pitaniya/khleb/khleb_1/#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/khleb/khleb_1/?_PRICE_TYPE=10&PAGEN_1=2#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/khleb/khleb_1/?_PRICE_TYPE=10&PAGEN_1=3#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/khleb/khleb_1/?_PRICE_TYPE=10&PAGEN_1=4#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/khleb/khleb_1/?_PRICE_TYPE=10&PAGEN_1=5#top_catalog_position',

        # flour
        'http://korzinamag.ru/catalog/produkty_pitaniya/bakaleya_1/muka_i_kompo'
        'nenty_dlya_vypechki/muka_pshenichnaya/#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/bakaleya_1/muka_i_komp'
        'onenty_dlya_vypechki/muka_pshenichnaya/?_PRICE_TYPE=10&PAGEN_1=2#top_'
        'catalog_position'

        # fruit
        'http://korzinamag.ru/catalog/produkty_pitaniya/ovoshchi_frukty/frukty/svezhie_1/#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/ovoshchi_frukty/frukty/svezhie_1/?_PRICE_TYPE=10&PAGEN_1=2#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/ovoshchi_frukty/frukty/svezhie_1/?_PRICE_TYPE=10&PAGEN_1=3#top_catalog_position',

        # vegetables
        'http://korzinamag.ru/catalog/produkty_pitaniya/ovoshchi_frukty/ovoshchi_1/svezhie_2/#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/ovoshchi_frukty/ovoshchi_1/svezhie_2/?_PRICE_TYPE=10&PAGEN_1=2#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/ovoshchi_frukty/ovoshchi_1/svezhie_2/?_PRICE_TYPE=10&PAGEN_1=3#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/ovoshchi_frukty/ovoshchi_1/svezhie_2/?_PRICE_TYPE=10&PAGEN_1=4#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/ovoshchi_frukty/ovoshchi_1/svezhie_2/?_PRICE_TYPE=10&PAGEN_1=5#top_catalog_position',

        # sugar+salt
        'http://korzinamag.ru/catalog/produkty_pitaniya/bakaleya_1/sakhar_sol_pishchevye_dobavki/sakhar/#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/bakaleya_1/sakhar_sol_pishchevye_dobavki/sakhar/?_PRICE_TYPE=10&PAGEN_1=2#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/bakaleya_1/sakhar_sol_pishchevye_dobavki/sol/#top_catalog_position',

        # buckwheat+rice
        'http://korzinamag.ru/catalog/produkty_pitaniya/bakaleya_1/krupy/grechnevaya_krupa/#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/bakaleya_1/krupy/grechnevaya_krupa/?_PRICE_TYPE=10&PAGEN_1=2#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/bakaleya_1/krupy/ris/#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/bakaleya_1/krupy/ris/?_PRICE_TYPE=10&PAGEN_1=2#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/bakaleya_1/krupy/ris/?_PRICE_TYPE=10&PAGEN_1=3#top_catalog_position',

        # pasta
        'http://korzinamag.ru/catalog/produkty_pitaniya/bakaleya_1/makaronnye_izdeliya/#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/bakaleya_1/makaronnye_izdeliya/?_PRICE_TYPE=10&PAGEN_1=2#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/bakaleya_1/makaronnye_izdeliya/?_PRICE_TYPE=10&PAGEN_1=3#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/bakaleya_1/makaronnye_izdeliya/?_PRICE_TYPE=10&PAGEN_1=4#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/bakaleya_1/makaronnye_izdeliya/?_PRICE_TYPE=10&PAGEN_1=5#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/bakaleya_1/makaronnye_izdeliya/?_PRICE_TYPE=10&PAGEN_1=6#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/bakaleya_1/makaronnye_izdeliya/?_PRICE_TYPE=10&PAGEN_1=7#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/bakaleya_1/makaronnye_izdeliya/?_PRICE_TYPE=10&PAGEN_1=8#top_catalog_position',
        'http://korzinamag.ru/catalog/produkty_pitaniya/bakaleya_1/makaronnye_izdeliya/?_PRICE_TYPE=10&PAGEN_1=9#top_catalog_position',
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="productElementJson '
                                  'prodlist col"]'):
            out_of_stock = len(sel.xpath('.//div[@class="'
                                         'stikerNone"]').extract())
            if not out_of_stock:
                item = MerchantItem()
                item['merchant'] = u'Корзина'
                # item['merchant_location'] = u'Новосибирск'
                item['price_value'] = sel.xpath('.//span[@class="price"]'
                                                '/@data-price').extract()[0]
                item['title'] = sel.xpath('.//div[@class="prodlist-title"]'
                                          '/a/text()').extract()[0].strip().encode('utf-8')
                item['sku'] = sel.xpath('@data-productid').extract()[0]
                item['url'] = sel.xpath('.//a[@class="big_link '
                                        'popup_detail_click"]/@href').extract()[0]

                yield item


class KorzinaTestSpider(KorzinaSpider):

    name = "korzina_test_spider"
    start_urls = ['http://korzinamag.ru/catalog/produkty_pitaniya/molochnye_produkty/moloko_slivki_molochnye_kokteyli/moloko_toplenoe/?_PRICE_TYPE=10&PAGEN_1=2#top_catalog_position']