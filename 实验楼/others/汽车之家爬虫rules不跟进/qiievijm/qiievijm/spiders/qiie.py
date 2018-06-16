# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from qiievijm.items import QiieBrandItem, QiieXyItem, QiieItem

class QiieSpider(CrawlSpider):
    name = 'qiie'
    name_lst = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#    start_urls = ['http://www.autohome.com.cn/grade/carhtml/{}.html'.format(i) for i in name_lst]
    start_urls = ['http://www.autohome.com.cn/grade/carhtml/A.html']
    rules = (
        Rule(LinkExtractor(allow=('.*?/price/series.*')), callback='parse_iexi',follow=True),
    )
    @classmethod
    def test_ss(cls):
        print(cls.rules[0].follow)

    #def parse(self, response):
    #    item = QiieBrandItem()
    #    brands = response.xpath('//dl')
    #    for i in brands:  
    #        item['brand'] = i.xpath('.//dt//text()').extract_first()
    #        item['iexi']=i.xpath('.//h4/a[1]/text()').extract()
    #        yield item'''
    def parse_iexi(self, response):
        print('----------------------------')
        return {
            'name':2
            }
        '''
        item = QiieXyItem()
        item['iexi'] = response.xpath('//title/text()').re_first(r'_(.+)价格')
        item['iexy'] = QiieItem()
        if '在售' in  response.xpath('//li[@class="current"]/text()').extract():
            qiies = response.xpath('//div[@id="divSeries"]//li')
            for i in qiies:
                item['iexi']['qiiemy'] = qiies.xpath('.//p//text()').extract_first()
                item['iexi']['grvudu'] = qiies.xpath('.//span/@style').re_first(r'\:\s(.+);')

                item['iexi']['vidkjw'] = qiies.xpth('.//div/text()').re_first(r'\d+万')
        yield item
        '''
QiieSpider.test_ss()
