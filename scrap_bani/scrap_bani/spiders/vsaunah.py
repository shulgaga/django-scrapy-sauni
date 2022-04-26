import re

import scrapy
from ..items import ScrapBaniItem
from parse.models import VsaunahUrls
from scrapy_playwright.page import PageMethod
from datetime import date
import json


class VsaunahSpider(scrapy.Spider):
    name = 'vsaunah'
    allowed_domains = ['vsaunah.ru']
    start_urls = ['https://vsaunah.ru']

    def parse(self, response, **kwargs):
        urls = VsaunahUrls.objects.all()
        for one in urls:
            one = one.hrefs
            yield scrapy.Request(url=one, callback=self.parse_start, dont_filter=True)

    def parse_start(self, response):
        headers = {
            'x-requested-with': 'XMLHttpRequest',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'accept': 'application/json, text/javascript, */*; q=0.01'
        }
        item = ScrapBaniItem()
        price_try = response.css('div.price > div > span::text').extract()
        if price_try:
            item['name'] = response.css('div.sauna__header > h1::text').get()
            today = date.today()
            item['date'] = today.strftime('%Y-%m-%d')
            item['url_istochnik'] = response.url
            adress = str(response.css(
                "div.sauna-paid__address-block > div:nth-child(1) > span.sauna__info-text > a::text"
            ).get()).split()
            item['city'] = adress[0]
            item['adress'] = adress[1:]
            price = response.css('div.price > div > span::text').extract()
            item['price'] = str(price).replace('[', '').replace(']', '')
            discription_1 = response.css('div.sauna-paid__advantages > div.sauna-paid__advantages-wrap > div > div '
                                         '> div > div::text').extract()
            discription_1 = str(discription_1).replace('\n', '').replace('\r', '').replace('  ', '').replace(u'\xa0', u'').replace('\\n', '').replace('[', '').replace(']', '')
            item['usligi'] = discription_1
            types = response.css('div.sauna__info-block > div:nth-child(2) > span.sauna__info-text > a::text').extract()
            item['types'] = str(types).replace('[', '').replace(']', '')
            item['istochnik'] = 'vsaunah'
            vmest = response.css('div.sauna__info-block > div:nth-child(3) > span.sauna__info-text::text').extract()
            item['vmestimost'] = str(vmest).replace('[', '').replace(']', '')
            discription_2 = response.css('div.sauna__desc.sauna-paid__desc > div > p::text').extract()
            discription_2 = str(discription_2).replace('\n', '').replace('\r', '').replace('  ', '').replace(u'\xa0', u'').replace('\\n', '').replace('[', '').replace(']', '')
            item['discription'] = discription_2
            photos = response.css('img::attr(data-lazy)').extract()
            item['photos'] = photos[0:4]
            item['cite'] = response.css('a.sauna__info-text.stat-site-link::attr(href)').extract()
            phone_id = response.css('div.sauna__info-phone.phone_number.show_number::attr(number)').get()
            phone_id = str(phone_id)
            form_data = {
                'id': phone_id,
                'get_cat_phone': '1'
            }
            yield scrapy.FormRequest(url='https://vsaunah.ru/ajax/', formdata=form_data, method="POST", headers=headers, callback=self.parse_phone, meta={'item':item})
        else:
            item['name'] = response.css('div.sauna__header > h1::text').get()
            item['istochnik'] = 'vsaunah'
            today = date.today()
            item['date'] = today.strftime('%Y-%m-%d')
            item['adress'] = response.css('div.sauna.sauna-free > div.sauna-free__cols > div.sauna-free__col-info > '
                                          'div > div:nth-child(1) > span.sauna__info-text > a::text').get()
            item['url_istochnik'] = response.url
            city = response.css('div.sauna.sauna-free > div.sauna-free__cols > div.sauna-free__col-info > div '
                                        '> div:nth-child(1) > span.sauna__info-text > span.hidden::text').get()
            city = re.split(',', city)[1]
            item['city'] = city.lstrip()
            photos = response.css('img::attr(data-lazy)').extract()
            item['photos'] = photos[0:4]

            if response.css('div.sauna__desc > div > noindex::text').extract():
                discription_1 = response.css('div.sauna__desc > div > noindex::text').extract()
                discription_1 = str(discription_1).replace('\n', '').replace('\r', '').replace('  ', '').replace(u'\xa0', u'').replace('\\n', '').replace('[', '').replace(']', '')
                item['discription'] = discription_1
            else:
                discription_1 = response.css('div.sauna-free__col-main > div.sauna__desc > div > p::text').extract()
                discription_1 = str(discription_1).replace('\n', '').replace('\r', '').replace('  ', '').replace(
                    u'\xa0', u'').replace('\\n', '').replace('[', '').replace(']', '')
                item['discription'] = discription_1
            discription_2 = response.css('div.sauna-paid__advantages-text::text').extract()
            discription_2 = str(discription_2).replace('\n', '').replace('\r', '').replace('  ', '').replace(u'\xa0', u'').replace('\\n', '').replace('[', '').replace(']', '')
            item['usligi'] = discription_2
            price = response.css('div.sauna__hall > div.sauna__hall-place > div.sauna__hall-price::text').extract()
            price = str(price).replace('\n', '').replace('\r', '').replace('  ', '').replace(u'\xa0', u'').replace('\\n', '').replace('[', '').replace(']', '')
            item['price'] = price
            if response.css('div.sauna__info-phone.phone_number.show_number > meta::attr(content)').get():
                item['phone_numbers'] = response.css('div.sauna__info-phone.phone_number.show_number > meta::attr(content)').get()
                yield item
            else:
                phone_id = response.css('div.sauna__info-phone.phone_number.showed::attr(number)').get()
                phone_id = str(phone_id)
                form_data = {
                    'id': phone_id,
                    'get_cat_phone': '1'
                }
                yield scrapy.FormRequest(url='https://vsaunah.ru/ajax/', formdata=form_data, method="POST", headers=headers, callback=self.parse_phone, meta={'item':item})

    def parse_phone(self, response):
        item = response.meta['item']
        js = response.text
        js = json.loads(js)
        item['phone_numbers'] = js['phone']
        yield item





"""
Добавить столбцы 
null True 
Фотки
"""