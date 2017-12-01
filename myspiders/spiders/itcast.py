# -*- coding: utf-8 -*-
import scrapy
from myspiders.items import MyspidersItem


class ItcastSpider(scrapy.Spider):
	# 爬虫名 启动爬虫时需要的参数 必须参数
	name = 'itcast'
	# 爬取域范围 允许爬虫在这个域名下进行爬取(可选参数)
	allowed_domains = ['http://www.itcast.cn']
	start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

	# parse方法 (固定)
	def parse(self, response):
		node_list = response.xpath("//div[@class='li_txt']")
		# 用来储存所有的item字段
		# items = []
		for node in node_list:
			item = MyspidersItem()

			name = node.xpath("./h3/text()").extract()
			title = node.xpath("./h4/text()").extract()
			info = node.xpath("./p/text()").extract()

			item['name'] = name[0]
			item['title'] = title[0]
			item['info'] = info[0]
			# items.append(item)
		# 返回提取到的每个item数据 给管道文件处理
# 		return items
			yield item