# -*- coding: utf-8 -*-
DOWNLOAD_DELAY = 1

BOT_NAME = 'WallhavenImageSpider'

SPIDER_MODULES = ['WallhavenImageSpider.spiders']
NEWSPIDER_MODULE = 'WallhavenImageSpider.spiders'


# Obey robots.txt rules
ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {
    'scrapy.pipelines.images.ImagesPipeline': 1,
    'scrapy.pipelines.files.FilesPipeline': 2,
}
# FILES_STORE = '/Users/cccccccccchy/Downloads'  # 文件存储路径
# IMAGES_STORE = '/Users/cccccccccchy/Downloads' # 图片存储路径

# 避免下载最近90天已经下载过的文件内容
FILES_EXPIRES = 90
# 避免下载最近90天已经下载过的图像内容
IMAGES_EXPIRES = 30

# 设置图片缩略图

# 图片过滤器，最小高度和宽度，低于此尺寸不下载
IMAGES_MIN_HEIGHT = 1
IMAGES_MIN_WIDTH = 1
# 浏览器头
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
}

IMAGES_STORE='../wallhaven'

ITEM_PIPELINES = {
   'WallhavenImageSpider.pipelines.WallhavenimagespiderPipeline': 300,
}
