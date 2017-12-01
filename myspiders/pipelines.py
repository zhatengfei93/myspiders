# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class MyspidersPipeline(object):
	def __init__(self):
		#可选方法，用于做参数初始化等操作，常用于保存item到文件中穿件文件并打开时用到
		self.f = open('data.json','wb')

	def process_item(self, item, spider):
    	# item(item对象) --- 被爬取的item
    	# spider(spider对象) ---爬取该item的spider
    	# 这个方法必须实现 每个item pipeline组件都需要调用该方法
    	# 这个方法必须返回一个item对象 被丢弃的item将不会被之后的pipeline组件所处理
		content = json.dumps(dict(item), ensure_ascii = False) + ",	\n"
		self.f.write(content.encode("utf-8"))
		return item

	def close_spider(self, spider):
		self.f.close()