import scrapy
from ..items import ScrapBaniItem
import re
from parse.models import ZoonUrls
from scrapy.loader import ItemLoader
from datetime import date


class ZoonSpider(scrapy.Spider):
    name = 'zoon'
    allowed_domains = ['zoon.ru']
    start_urls = ['https://zoon.ru']

    def parse(self, response):
        urls = ZoonUrls.objects.all()
        for one in urls:
            one = one.hrefs
            yield scrapy.Request(url=one, callback=self.parse_start)

    def parse_start(self, response):
        l = ItemLoader(item=ScrapBaniItem(), selector=response.css('body'))
        phone = response.css('div.service-phones-box > div > span > a::attr(href)').extract()
        phone = str(phone).replace('tel:', '').replace('[', '').replace(']', '')
        l.add_value('phone_numbers', phone)
        adress = response.css('div > address::text').get()
        adress = re.split(',', adress)
        city = adress[0]
        adress1 = adress[1:]
        l.add_value('city', city)
        l.add_value('adress', adress1)
        l.add_css('adress', 'div.invisible-links > address > a')
        if response.css('div > dl.fluid.uit-cover > dd > div::text').get() is None:
            l.add_css('time', 'div > dl.fluid.uit-cover > dd > div')
        else:
            l.add_css('time', 'dl.fluid.uit-cover > dd > div > a')
        l.add_css('price', 'div.service-box-description.box-padding.btop > div > dl > dd > div > div > div > span')
        l.add_css('cite', 'div.service-box-description.box-padding.btop > div > dl:nth-child(3) > dd > div > a::attr('
                          'href)')
        l.add_css('name', 'div.service-block._no-margin-bottom.service-main-container.clearfix > div > h1 > span')
        l.add_css('name', 'div.service-block._no-margin-bottom.service-main-container.clearfix > div > h1')
        l.add_css('discription', 'div.params-list.params-list-new > dl > dd > p')
        l.add_css('usligi', 'div.service-description-block.invisible-links > div > dl:nth-child(1) > dd > a')
        l.add_css('types', 'div.service-description-block.invisible-links > div > dl:nth-child(2) > dd > a')
        for i in response.css('div.pull-left.service-description-box > div > div > div > '
                              'div.service-description-block.invisible-links > div > dl'):
            name3 = i.css('dt.fs-small.gray::text').get()
            if re.search('Общая вместимость ', name3):
                vmest = response.css('nobr::text').extract()
                l.add_value('vmestimost', vmest)
        l.add_css('photos', 'img.service-block-photo-item-content::attr(src)')
        l.add_value('url_istochnik', response.url)
        l.add_value('date', date.today().strftime('%Y-%m-%d'))
        l.add_value('istochnik', 'zoon')
        yield l.load_item()
