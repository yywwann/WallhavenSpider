# -*- coding: utf-8 -*-
import scrapy


class WallhavenimagespiderItem(scrapy.Item):
    image_urls = scrapy.Field()  # 图片的链接
    images = scrapy.Field()
