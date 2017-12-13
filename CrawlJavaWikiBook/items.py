# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class CrawljavawikibookItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()


    id = Field()
    url = Field()
    content = Field()


   # html = Field()
   # heading = Field()
   # code = Field()
    #removeCode = Field()

    # Comment this for Java Oracle Content and Uncomment for Java Wikibook Content
    html = Field()
    heading = Field()
    code = Field()
    removeCode = Field()
