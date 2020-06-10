# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MymeishiItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field() #名字
    categories = scrapy.Field() #类别
    main_ingredients = scrapy.Field() #主料
    auxiliary_ingredients = scrapy.Field() #辅料
    seasonings = scrapy.Field() #配料
    craft = scrapy.Field()  #工艺
    taste = scrapy.Field() #口味