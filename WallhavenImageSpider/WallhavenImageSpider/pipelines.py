# -*- coding: utf-8 -*-
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline   #内置的图片管道


class WallhavenimagespiderPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            print("图片连接:", image_url)
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item
