import scrapy
from ..items import ScrapBaniItem
import re
import json
from scrapy.loader import ItemLoader
from datetime import date


class BanyaSpider(scrapy.Spider):
    name = 'banya'
    allowed_domains = ['banya.ru']

    start_urls = ['https://www.banya.ru/map/ajax/get-map-objects.php?iblock=93']

    def parse(self, response):
        resp = response.text
        resp = json.loads(resp)
        for i in resp:
            url = f'https://www.banya.ru{i["URL"]}'
            yield scrapy.Request(url=url, callback=self.parse_start)

    def parse_start(self, response):
        l = ItemLoader(item=ScrapBaniItem(), selector=response.css('body'))
        l.add_css('name', 'div.left-part > div.main-item-info > div.mobile-hide > h1')
        adress1 = response.css('div.mobile-hide > div.address > span::text').get()
        adress1 = re.split(',', adress1)
        l.add_value('city', adress1[0])
        l.add_value('adress', adress1[1:])
        l.add_css('discription', '#detail-part-1 > div.desc-wrapper > div.description-wrapper > div.description-block')
        l.add_css('discription', '#detail-part-1 > div.desc-wrapper > div.description-wrapper > div.description-block > ul > li')
        l.add_css('discription', '#detail-part-1 > div.desc-wrapper > div.description-wrapper > div.description-block > i')
        l.add_css('discription', '#room-description > div.text > div.text-block > div.text-content')
        l.add_css('discription', '#room-description > div.text > div.text-block > div.text-content > li')
        l.add_css('types', '#detail-part-1 > div.desc-wrapper > div.subitem-data > div:nth-child(2) > div.data')
        l.add_css('vmestimost', '#detail-part-1 > div.desc-wrapper > div.subitem-data > div:nth-child(5) > div.data')
        l.add_css('usligi', '#detail-part-1 > div.desc-wrapper > div.subitem-data > div:nth-child(7) > div.data')
        price = []
        for one in response.css('#tariffs_id > div'):
            price1 = one.css('div.price::text').get()
            opt = one.css('div.desc::text').get()
            price.append(f"{price1} - {opt}")
        l.add_value('price', price)
        l.add_css('cite', 'div.addons > div > div.link_item > noindex > a::attr(href)')
        l.add_css('phone_numbers', '#callmePhoneBathInp::attr(value)')
        l.add_value('url_istochnik', response.url)
        l.add_value('date', date.today().strftime('%Y-%m-%d'))
        l.add_value('istochnik', 'banya')
        yield l.load_item()


