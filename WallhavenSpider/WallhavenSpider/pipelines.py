# -*- coding: utf-8 -*-
import pandas as pd


class WallhavenspiderPipeline(object):
    def __init__(self):  # 定义构造器，初始化要写入的文件
        self.mypd = pd.DataFrame(columns=['url'])

    def close_spider(self, spider):  # 重写close_spider回调方法
        self.mypd.to_csv("/Users/cccccccccchy/Downloads/wallhaven.csv")

    def process_item(self, item, spider):  # 添加数据到pandas中
        self.mypd = self.mypd.append({'url': item['url'][0]}, ignore_index=True)
        print(len(self.mypd))

