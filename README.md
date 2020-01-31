# WallhavenSpider

## 环境
Scrapy
python

## 使用方法

```shell
git clone https://github.com/yywwann/WallhavenSpider.git
```

第一次使用需要修改文件保存路径
1. /WallhavenSpider/WallhavenSpider/WallhavenSpider/pipelines.py 保存csv的位置
2. /WallhavenSpider/WallhavenImageSpider/WallhavenImageSpider/spiders/job_position.py 读取csv的位置
3. /WallhavenSpider/WallhavenImageSpider/WallhavenImageSpider/settings.py中的 `IMAGES_STORE`

进入WallhavenSpider, 执行

```shell
scrapy crawl job_position
```

完成后进入WallhavenImageSpider, 执行


```shell
WallhavenImageSpider
```

500张壁纸大概需要25分钟