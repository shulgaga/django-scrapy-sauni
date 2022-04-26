import scrapy
from ..items import ScrapBaniItem
from datetime import date
from scrapy.loader import ItemLoader


class DvhabSpider(scrapy.Spider):
    name = 'dvhab'
    allowed_domains = ['dvhab.ru']
    start_urls = [
        'https://www.dvhab.ru/khabarovsk/fun/saunas?page=3',
        'https://www.dvhab.ru/khabarovsk/fun/saunas?page=2',
        'https://www.dvhab.ru/khabarovsk/fun/saunas?page=1'
    ]

    def parse(self, response, **kwargs):
        urls = response.css('div.company-wrap > div.company__info > header > h4 > a::attr(href)').extract()
        for url in urls:
            yield scrapy.Request(url=f'https://www.dvhab.ru{url}', callback=self.parse_start)

    def parse_start(self, response):
        l = ItemLoader(item=ScrapBaniItem(), selector=response.css('body'))
        l.add_value('city', 'Xaбаровск')
        l.add_css('time', 'div.company-contacts__column.company-contacts__schedule-column > div > div > div.schedule-block__caption > a > span > span')
        l.add_css('adress', 'a.address-string.j_addressString')
        l.add_css('adress', 'span.address-string.j_addressString')
        l.add_css('phone_numbers', 'div.company-contacts__phones > div > div > span')
        l.add_css('cite', 'div.contacts-item.website.company-contacts__paragraph > a::attr(href)')
        l.add_css('mail', 'div.contacts-item.email.company-contacts__paragraph > a')
        l.add_css('name', 'div.col.info > div.company-name-wrap > h1')
        l.add_css('types', 'div > div > div:nth-child(1) > div.spr-attribute__body > a')
        l.add_css('vmestimost', '#attributes > div > div > div:nth-child(2) > div.spr-attribute__body > span')
        l.add_css('discription', '#full_description > div > p')
        l.add_css('discription', '#full_description > div > p > strong')
        l.add_css('discription', '#full_description > div > ul > li')
        l.add_css('photos', '#images > div > ul > li > a::attr(href)')
        l.add_value('url_istochnik', response.url)
        l.add_value('date', date.today().strftime('%Y-%m-%d'))
        l.add_value('istochnik', 'dvhab')
        yield l.load_item()
