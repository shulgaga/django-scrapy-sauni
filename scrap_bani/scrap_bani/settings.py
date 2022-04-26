import sys
import os
import django


sys.path.append(os.path.dirname(os.path.abspath('.')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'bani.settings'


django.setup()
BOT_NAME = 'scrap_bani'

SPIDER_MODULES = ['scrap_bani.spiders']
NEWSPIDER_MODULE = 'scrap_bani.spiders'


ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {'scrap_bani.pipelines.ScrapBaniPipeline': 300}

