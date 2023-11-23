# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import re


class PokemonsScraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass


# def enlever_str(string):
#     chiffres = re.findall(r'\d', string)
#     return int(chiffres)


class PokemonItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    stock = scrapy.Field(stock_sans_str = enlever_str)
    sku = scrapy.Field()
    categories = scrapy.Field()
    tags = scrapy.Field()
    weight = scrapy.Field()
    length = scrapy.Field()
    width = scrapy.Field()
    height = scrapy.Field()