# -*- coding: utf-8 -*-

import json
import csv


header = [
    "分类",
    "更新频率",
    "标题",
    "feed",
    "网站主页",
    "描述",
    "feedly 订阅数",
    "标签",
]


with open("feedly.json") as feedly_file:
    data = json.loads(feedly_file.read())

with open("feeds.csv", "w+") as feeds:
     writer = csv.writer(feeds)
     writer.writerow(header)
     for item in data:
         feed_url = item['id'][5:]
         title = item['title']
         subscribers = item['subscribers']
         site = item['website']
         description = ""
         categorie = item['categories'][0]['label']
         topics = item.get('topics')
         weekly = "每周{}篇".format(item['velocity'])
         writer.writerow([
             categorie,
             weekly,
             title,
             feed_url,
             site,
             description,
             subscribers,
             topics,
        ])
