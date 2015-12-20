# -*- coding: utf-8 -*-

import scrapy
from scrapy.loader import ItemLoader
from scrapy.selector import Selector
from selenium import webdriver

from scrapy_example.items import ProductItem


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['demo.thelia.net']
    start_urls = ('http://demo.thelia.net/?view=product&locale=en_US&product_id=1',)

    def __init__(self):
        super(BasicSpider, self).__init__()
        self.driver = webdriver.Firefox()

    def parse(self, response):
        self.driver.get(response.url)
        for i in xrange(5):
            next_btn = self.driver.find_element_by_xpath('//li[@class="next"]/a')
            try:
                next_btn.click()
                loader = ItemLoader(item=ProductItem(), selector=Selector(text=self.driver.page_source))
                loader.add_xpath('name', '//h1[@class="name"]//text()')
                loader.add_xpath('brand', '//span[@itemprop="brand"]/text()')
                loader.add_xpath('price', '//span[@class="price"]/text()')
                yield loader.load_item()
            except:
                break
        self.driver.close()
