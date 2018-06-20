# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from doban_movie.items import DobanMovieItem


class AwesomeMovieSpider(CrawlSpider):
    name = 'awesome-movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/subject/3011091/']

    rules = (
        Rule(LinkExtractor(allow=r'/?from=subject-page'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = DobanMovieItem() 
        item['score'] = response.xpath('//div[contains(@class, "clearfix")]/strong/text()').extract_first()
        self.logger.info(response.xpath('//div[contains(@class,"clearfix")]/strong/text()').extract_first())
        item['url'] = response.url
        item['name'] = response.xpath('//span[@property="v:itemreviewed"]/text()').extract_first()
        item['summary'] = response.xpath('//span[@class="all hidden"]/text()').extract_first()
        if not item['summary']:
            item['summary'] = response.xpath('//span[@property="v:summary"]/text()').extract_first()
        yield item
