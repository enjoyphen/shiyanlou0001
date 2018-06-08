# -*- coding: utf-8 -*-
import scrapy
from gitspider.items import GitspiderItem

class GitSpider(scrapy.Spider):
    name = 'git'
    start_urls = ['https://github.com/shiyanlou?tab=repositories&page={}'.format(i) for i in range(1,5)]
    
    def parse(self, response):
        repositories = response.css('li[itemprop=owns]')
        for i in repositories:
            item = GitspiderItem()
            item['name'] = i.css('a[itemprop~="name"]::text').extract_first().strip()
            item['update_time'] = i.css('relative-time::attr(datetime)').extract_first()
            yield item
