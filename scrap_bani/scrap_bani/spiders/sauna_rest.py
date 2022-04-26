import scrapy
import json
import re
from ..items import ScrapBaniItem
from scrapy.loader import ItemLoader
from datetime import date


class SaunaRestSpider(scrapy.Spider):
    name = 'sauna_rest'
    allowed_domains = ['sauna.rest']
    start_urls = ['http://sauna.rest/core/ajax/aj_cmsLoadCities.php?select-city']

    def parse(self, response, **kwargs):
        s = json.loads(response.text)
        for url in s:
            url = url['city_url']
            for p in range(1, 10):
                yield scrapy.Request(url=f'http://{url}/?page={p}', callback=self.parse_start)

    def parse_start(self, response):
        url_main = response.url
        u = re.split('/', url_main)
        main_url = f'{u[0]}//{u[1]}{u[2]}'
        for url in response.css('h4.text-uppercase.in_cat_header > a::attr(href)').extract():
            yield scrapy.Request(url=f'{main_url}{url}', callback=self.parse_items)

    def parse_items(self, response):
        l = ItemLoader(item=ScrapBaniItem(), selector=response.css('body'))
        l.add_css('name', 'header.page-header-sauna > h1')
        l.add_css('city', 'div.header__city-select > a')
        l.add_css('adress', '#sauna_address')
        l.add_css('phone_numbers', 'div.phone-inner-block > a::attr(phone)')
        for row in response.css('div.list-sauna-options__item'):
            name1 = row.css('p > b::text').get()
            if re.search('Вместимость:', name1):
                vmestimost = row.css('p::text').extract()
                l.add_value('vmestimost', vmestimost)
            elif re.search('Стоимость::', name1):
                price = row.css('p::text').extract()
                l.add_value('price', price)
            elif re.search('Парная::', name1):
                types = row.css('p::text').extract()
                l.add_value('types', types)
        uslugi = []
        for one in response.css('a.tile-content.ink-reaction'):
            title = str(one.css('div.tile-text::text').get()).replace('\r', '').replace('\n', '').replace('  ', '')
            opt = str(one.css('div.tile-text > small::text').get()).replace('\r', '').replace('\n', '').replace('  ', '')
            uslugi.append(f'{title}{opt}')
        l.add_value('usligi', uslugi)
        l.add_css('photos', 'a.gallery-one-photo.owl-gallery-link::attr(data-url)')
        l.add_value('url_istochnik', response.url)
        l.add_value('date', date.today().strftime('%Y-%m-%d'))
        l.add_value('istochnik', 'sauna_rest')
        yield l.load_item()
