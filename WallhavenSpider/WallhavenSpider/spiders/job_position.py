# -*- coding: utf-8 -*-
import scrapy
from WallhavenSpider.items import WallhavenspiderItem


class JobPositionSpider(scrapy.Spider):
    name = 'job_position'
    allowed_domains = ['wallhaven.cc']
    start_urls = []
    for i in range(221):
        url = 'https://wallhaven.cc/toplist?page=' + str(i + 1)
        start_urls.append(url)

    def parse(self, response):
        item = WallhavenspiderItem()
        # 匹配
        for jobs_primary in response.xpath('//li/figure'):
            item['url'] = jobs_primary.xpath('./a/@href').extract()
            yield item
