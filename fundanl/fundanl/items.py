# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import re

import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags

def complete_urls(text):
    return "https://www.funda.nl" + text

def clean_text(text):
    text = text.replace("/r/n", "").strip()
    return text
def showing_digits(text):
    text = re.sub("[^0-9]", "", text)
    return text

def remove_m2(text):
    return str(text.replace("m²",""))

class FundanlItem(scrapy.Item):
    # define the fields for your item here like:
    urls = scrapy.Field(output_processor= TakeFirst(),
                        input_processor = MapCompose(remove_tags, complete_urls))

    price = scrapy.Field(output_processor= TakeFirst(),
                         input_processor = MapCompose(remove_tags, clean_text))
    m2 = scrapy.Field(output_processor= TakeFirst(),
                      input_processor = MapCompose(remove_tags, remove_m2))
    address = scrapy.Field(output_processor= TakeFirst(),
                           input_processor = MapCompose(remove_tags, clean_text))
    roomNumber = scrapy.Field(output_processor= TakeFirst(),
                              input_processor = MapCompose(remove_tags, clean_text, showing_digits))