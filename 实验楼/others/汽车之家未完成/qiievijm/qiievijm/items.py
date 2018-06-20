# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QiieBrandItem(scrapy.Item):
    # define the fields for your item here like:
    brand = scrapy.Field()
    iexi = scrapy.Field()
class QiieXyItem(scrapy.Item):
    iexi = scrapy.Field()
    iexy = scrapy.Field()
class QiieItem(scrapy.Item):
    iekrmy = scrapy.Field()
    grvudu = scrapy.Field()
    vidkjw = scrapy.Field()
