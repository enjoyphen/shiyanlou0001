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
            url_project = response.urljoin(i.xpath('.//a/@href').extract_first())
            request = scrapy.Request(url_project, callback=self.parse_nu)
            request.meta['item'] = item
            yield request
    def parse_nu(self, response):
        item = response.meta['item']
        lst= response.xpath('//ul[@class="numbers-summary"]')
        item['commits'] = lst.xpath('.//a[@data-pjax]/span/text()').extract_first().strip()
        item['branches'] = lst.xpath('.//a[contains(@href,"branches")]/span/text()').extract_first().strip()
        item['releases'] = lst.xpath('.//a[contains(@href,"releases")]/span/text()').extract_first().strip()
        yield item
