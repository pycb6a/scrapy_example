# -*- coding: utf-8 -*-


import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose


class ProductItem(scrapy.Item):
    name = scrapy.Field()
    brand = scrapy.Field(input_processor=MapCompose(lambda x: x.title()))
    price = scrapy.Field(output_processor=TakeFirst())
