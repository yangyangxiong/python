# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LiepingItem(scrapy.Item):
    # job = scrapy.Field()
    salary = scrapy.Field()
    position = scrapy.Field()
    education = scrapy.Field()
    operatinghours = scrapy.Field()
    company = scrapy.Field()
