# -*- coding: utf-8 -*-
import datetime
from sqlalchemy.orm import sessionmaker
from gitspider.model import repositor, engine


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class GitspiderPipeline(object):
    def process_item(self, item, spider):
        item['update_time'] = datetime.datetime.strptime(item['update_time'],'%Y-%m-%dT%H:%M:%SZ')
        self.session.add(repositor(**item))
        return item
    def open_spider(self,spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()
    def close_spider(self,spider):
        self.session.commit()
        self.session.close()


