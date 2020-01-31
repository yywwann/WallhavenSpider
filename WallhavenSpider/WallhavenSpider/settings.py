# -*- coding: utf-8 -*-
BOT_NAME = 'WallhavenSpider'
SPIDER_MODULES = ['WallhavenSpider.spiders']
NEWSPIDER_MODULE = 'WallhavenSpider.spiders'
ROBOTSTXT_OBEY = True
# 配置默认的请求头
DEFAULT_REQUEST_HEADERS = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}
ITEM_PIPELINES = {
   'WallhavenSpider.pipelines.WallhavenspiderPipeline': 300,
}
