# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from WallhavenImageSpider.items import WallhavenimagespiderItem


class JobPositionSpider(scrapy.Spider):
    name = 'job_position'
    allowed_domains = ['wallhaven.cc']
    start_urls = ['http://wallhaven.cc/']

    def start_requests(self):  # 重写这个方法
        url = pd.read_csv("../wallhaven.csv", usecols=["url"])  # 读取csv文件,改为你的路径
        # url = url.head(5)  # 只取前5条数据
        urls = [x for x in url["url"]]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = WallhavenimagespiderItem()
        item['image_urls'] = response.xpath('//div[@class="scrollbox"]/img[1]/@src').extract()
        yield item
