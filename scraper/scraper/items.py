# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem
from properties.models import Property
import scrapy

class ScraperItem(DjangoItem):
    django_model = Property

# class ScraperItem(scrapy.Item):
#     pass
