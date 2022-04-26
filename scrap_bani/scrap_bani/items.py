from scrapy_djangoitem import DjangoItem
import scrapy
from parse.models import OldInfo
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose, Join
from w3lib.html import remove_tags


def clean(value):
    return value.replace('\n', '').strip().replace('\r', '').replace(u'\\r', u'').replace('\t', '').replace(u'\\xa0', u' ').replace(u'\xa0', u' ').replace(u'\xad', u' ')


class ScrapBaniItem(DjangoItem):
    django_model = OldInfo
    discription = scrapy.Field(input_processor=MapCompose(remove_tags, clean), output_processor=Join(', '))
    vmestimost = scrapy.Field(input_processor=MapCompose(remove_tags, clean), output_processor=Join(', '))
    adress = scrapy.Field(input_processor=MapCompose(remove_tags, clean), output_processor=Join(', '))
    url_istochnik = scrapy.Field(input_processor=MapCompose(remove_tags, clean))
    name = scrapy.Field(input_processor=MapCompose(remove_tags, clean), output_processor=Join(', '))
    city = scrapy.Field(input_processor=MapCompose(remove_tags, clean), output_processor=Join(', '))
    mail = scrapy.Field(input_processor=MapCompose(remove_tags, clean), output_processor=Join(', '))
    phone_numbers = scrapy.Field(input_processor=MapCompose(remove_tags, clean), output_processor=Join(', '))
    time = scrapy.Field(input_processor=MapCompose(remove_tags, clean), output_processor=Join(', '))
    photos = scrapy.Field(input_processor=MapCompose(remove_tags, clean), output_processor=Join(', '))
    usligi = scrapy.Field(input_processor=MapCompose(remove_tags, clean), output_processor=Join(', '))
    price = scrapy.Field(input_processor=MapCompose(remove_tags, clean), output_processor=Join(', '))
    types = scrapy.Field(input_processor=MapCompose(remove_tags, clean), output_processor=Join(', '))
    cite = scrapy.Field(input_processor=MapCompose(remove_tags, clean), output_processor=Join(', '))
    date = scrapy.Field(output_processor=Join(', '))
    url_istochnik = scrapy.Field(output_processor=Join(', '))
    istochnik = scrapy.Field(output_processor=Join(', '))
