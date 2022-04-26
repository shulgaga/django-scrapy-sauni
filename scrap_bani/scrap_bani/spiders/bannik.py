import scrapy
from ..items import ScrapBaniItem
from parse.models import BannikUrls
from scrapy.loader import ItemLoader
from datetime import date


class BannikSpider(scrapy.Spider):
    name = 'bannik'
    allowed_domains = ['bannik.ru']
    start_urls = ['https://bannik.ru/msk/catalog']

    def parse(self, response, **kwargs):
        urls = BannikUrls.objects.all()
        for one in urls:
            one = one.hrefs
            yield scrapy.Request(url=one, callback=self.parse_start)

    def parse_start(self, response):
        l = ItemLoader(item=ScrapBaniItem(), selector=response.css('body'))
        l.add_css('discription', 'div.desc.content > p')
        l.add_css('discription', 'div.desc.content > ul > li')
        l.add_css('discription', 'div.desc.content > div > ul > li > a')
        l.add_css('phone_numbers', 'body > div.page > div.mobile-call.d-sm-none > a::attr(href)')
        l.add_css('name', 'div.col-lg-4.item__main-sidebar__wrapper > div > h1')
        l.add_css('adress', 'div.item__street.item__main-sidebar__row')
        l.add_css('city', 'li.main-menu__item.d-inline-block > a > span')
        l.add_css('vmestimost', 'div.item__capacity.item__main-sidebar__row')
        l.add_css('types', 'div.item__steam-room.item__main-sidebar__row > a')
        l.add_css('photos', 'img.lazy-img::attr(src)')
        l.add_value('url_istochnik', response.url)
        l.add_value('date', date.today().strftime('%Y-%m-%d'))
        l.add_value('istochnik', 'bannik')
        yield l.load_item()
