from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from scraper import settings as my_settings
from scrapy.utils.project import get_project_settings
from scraper.spiders.otodom_spider import PropertiesSpider
# from scraper.spiders.js_rendered_spider import PropertiesSpider
# from scraper.spiders.headless_browser_spider import PropertiesSpider

class Command(BaseCommand):
    help = 'Release spider'

    def handle(self, *args, **options):
        # crawler_settings = Settings()
        # crawler_settings.setmodule(my_settings)

        # process = CrawlerProcess(settings=crawler_settings)
        process = CrawlerProcess(get_project_settings())

        process.crawl(PropertiesSpider)
        process.start()