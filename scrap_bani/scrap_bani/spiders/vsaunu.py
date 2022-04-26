import re

import scrapy
import json
from ..items import ScrapBaniItem
from scrapy.loader import ItemLoader
from datetime import date


class VsaunuSpider(scrapy.Spider):
    name = 'vsaunu'
    allowed_domains = ['vsaunu.ru']
    start_urls = ['https://www.vsaunu.ru']

    def parse(self, response, **kwargs):
        js = response.css('body > div.index > script:nth-child(1)::text').get().replace('\n', '').replace('var search_cities = ', '').lstrip().replace(';', '')
        js = json.loads(js)
        for i in js:
            url = i['id']
            for p in range(1, 39):
                yield scrapy.Request(url=f'https://www.{url}', callback=self.parse_start)

    def parse_start(self, response):
        for url in response.css('div.infocard__content > a::attr(href)').extract():
            yield scrapy.Request(url=f'https://www.vsaunu.ru{url}', callback=self.parse_item)

    def parse_item(self, response):
        l = ItemLoader(item=ScrapBaniItem(), selector=response.css('body'))
        l.add_css('name', 'body > div.sauna.sauna_mult > div.sauna__head > div > h1')
        l.add_css('city', '#current-city')
        l.add_css('phone_numbers', 'div.card-contacts__section.card-contacts__section_bottom > div > div > p > a')
        adress = response.css('div.card-address__section.card-address__section_top > p.card-address__link > a').get()
        adress = re.split(',', adress)[1:]
        l.add_value('adress', adress)
        l.add_css('time', 'div.sauna__innercol.sauna__innercol_left > div > div > p > span.card-contacts__text-span')
        l.add_css('price', 'p.card-contacts__price')
        l.add_css('discription', 'body > div.sauna > div.sauna__content > div:nth-child(2) > div.sauna__cols.sauna__cols_top > div.sauna__col.sauna__col_left > div.card-desc.sauna__card > div > div.card-desc__desc > div.card-desc__text')
        l.add_css('usligi', 'div.card-desc__services > p.card-desc__service')
        l.add_css('vmestimost', 'div.card-desc__services > p.card-desc__service.card-desc__service_count')
        l.add_css('photos', 'a.sauna__imgblock > img::attr(src)')
        l.add_css('cite', 'div.card-desc__side > p.card-desc__sitelink > a')
        l.add_value('url_istochnik', response.url)
        l.add_value('date', date.today().strftime('%Y-%m-%d'))
        l.add_value('istochnik', 'vsaunu')
        yield l.load_item()

