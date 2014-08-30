# -*- coding: utf-8 -*-

from peewee import SqliteDatabase, Model, CharField, DecimalField

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

DATABASE_PATH = 'milkprice_items.db'
database = SqliteDatabase(DATABASE_PATH)


class BaseModel(Model):
    class Meta:
        database = database


class MilkpriceItem(BaseModel):
    id_ = CharField()
    title = scrapy.Field()
    volume = scrapy.Field()
    price = scrapy.Field()


class MilkpricePipeline(object):
    """Pipeline to persist items in SQLite"""
    def __init__(self):



    def process_item(self, item, spider):
        return item
