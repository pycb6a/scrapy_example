# -*- coding: utf-8 -*-
BOT_NAME = 'scrapy_example'

SPIDER_MODULES = ['scrapy_example.spiders']
NEWSPIDER_MODULE = 'scrapy_example.spiders'

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

USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16',
]
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_example.middlewares.RandomUserAgentMiddleware': 400,
}
