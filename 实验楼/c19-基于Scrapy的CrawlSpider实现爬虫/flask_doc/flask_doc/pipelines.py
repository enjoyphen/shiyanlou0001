# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
from functools import reduce
import redis
import json

class FlaskDocPipeline(object):
    def process_item(self, item, spider):
        item['text'] = reduce(lambda x,y:x+y, item['text'])
        item['text'] = re.sub('\s+', ' ', item['text'])
        #item = json.dumps(item)
        # item = '{'+'url:'+item['url']+','+'text:'+item['text']+'}'
        self.redis.lpush('flask_doc:items', json.dumps(dict(item)))
        return item
    
    def open_spider(self, spider):
        self.redis = redis.StrictRedis(host='localhost',port='6379',db=0)
