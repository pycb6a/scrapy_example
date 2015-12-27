# -*- coding: utf-8 -*-


from loginform import fill_login_form
from scrapy import Request, FormRequest
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy_example.items import LinkItem


class CrawlerSpider(CrawlSpider):
    name = 'crawler'
    allowed_domains = ['demo.thelia.net']
    start_urls = ['http://demo.thelia.net/?view=category&locale=en_US&category_id=1']
    custom_settings = {
        'FEED_URI': 'links.json',
        'FEED_FORMAT': 'json'
    }

    rules = (
        Rule(LinkExtractor(allow=r'view=category|product',
                           restrict_xpaths=('//ul[contains(@class, "pagination")]', '//div[@class="product-btn"]')),
             callback='parse_item',
             follow=True),
    )

    def start_requests(self):
        yield Request(url=self.start_urls[0], callback=self.login)

    def login(self, response):
        args, url, method = fill_login_form(response.url, response.body, 'test@thelia.net', 'thelia')
        return FormRequest(response.url, method=method, formdata=args)

    def parse_item(self, response):
        item = LinkItem()
        if 'product' in response.url:
            item['url'] = response.url
            item['status_code'] = response.status
            item['title'] = response.xpath('//title/text()').extract()
            item['content_type'] = response.headers['Content-Type']
        return item
