import scrapy
from ..items import ScrapBaniItem
from datetime import date
from scrapy.loader import ItemLoader


class A101Spider(scrapy.Spider):
    name = 'a101'
    allowed_domains = ['101sauna.ru']
    start_urls = ['https://101sauna.ru/Moscow']

    def parse(self, response, **kwargs):
        for url in response.css('#main-page > footer > div > div > div.hidden-md-down.col-lg-5 > div > div > a::attr('
                                'href)').extract():
            for p in range(1, 10):
                yield scrapy.Request(url=f'https://101sauna.ru{url}/:tpl_page-search:part-{p}', callback=self.start_parse)

    def start_parse(self, response):
        for url in response.css('body > div > div > div.card-content > h3 > a::attr(href)').extract():
            yield scrapy.Request(url=f'https://101sauna.ru{url}', callback=self.parse_items)

    def parse_items(self, response):
        l = ItemLoader(item=ScrapBaniItem(), selector=response.css('body'))
        l.add_css('name', '#sectionSaun > div.saunaInfo > div:nth-child(1) > div > h1')
        l.add_css('city', '#citySelect')
        l.add_css('price', '#price')
        l.add_css('phone_numbers', '#sectionSaun > div.saunaInfo > div > div > div.d-none > span')
        l.add_css('adress', 'span.street-address')
        l.add_css('vmestimost', 'div.col-xl-6.mb-3.mb-xl-0 > div > div:nth-child(1) > div > div > div:nth-child(3) > p:nth-child(2)')
        l.add_css('types', 'div.col-xl-6.mb-3.mb-xl-0 > div > div:nth-child(1) > div > div > div:nth-child(3) > p:nth-child(3)')
        if not response.css(
                'div.col-xl-6.mb-3.mb-xl-0 > div > div:nth-child(2) > div.d-sm-none.d-lg-block.parametrs > p').extract():
            l.add_css('usligi', 'div.col-md-6 > p.d-sm-none.d-lg-block')
        else:
            l.add_css('usligi', 'div.col-xl-6.mb-3.mb-xl-0 > div > div:nth-child(2) > div.d-sm-none.d-lg-block.parametrs > p')
        l.add_css('discription', 'div > div.columns > p')
        l.add_css('discription', 'div.col > div.columns > p')
        l.add_css('photos', 'a.photo.mb-4.d-inline-block.z-depth-2::attr(href)')
        l.add_value('url_istochnik', response.url)
        today = date.today().strftime('%Y-%m-%d')
        l.add_value('date', today)
        l.add_value('istochnik', '101sauna')
        yield l.load_item()
