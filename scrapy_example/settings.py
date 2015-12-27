# -*- coding: utf-8 -*-


BOT_NAME = 'scrapy_example'

SPIDER_MODULES = ['scrapy_example.spiders']
NEWSPIDER_MODULE = 'scrapy_example.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
}

ITEM_PIPELINES = {
    'scrapy_example.pipelines.MongoPipeline': 300,
}

CONCURRENT_REQUESTS = 3
DOWNLOAD_DELAY = 3
LOG_LEVEL = 'INFO'

MONGO_URI = 'localhost'
MONGO_DATABASE = 'items'
