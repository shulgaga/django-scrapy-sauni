
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from parse.models import OldInfo


class ScrapBaniPipeline:

    def process_item(self, item, spider):
        item.save()
        return item
