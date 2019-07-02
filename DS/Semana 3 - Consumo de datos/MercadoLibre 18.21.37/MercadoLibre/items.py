# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MercadoItem(scrapy.Item):
    Nombre=scrapy.Field()
    Ventas=scrapy.Field()
    Precio=scrapy.Field()
    Precio_Original=scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
