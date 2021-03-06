# -*- coding: utf-8 -*-
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from scrapy_example.spiders.basic import BasicSpider


def main():
    process = CrawlerProcess(get_project_settings())
    process.crawl(BasicSpider)
    process.start()


if __name__ == '__main__':
    main()
