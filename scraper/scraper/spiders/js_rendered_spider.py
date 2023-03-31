import os
from scrapy.spiders import CrawlSpider, Spider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from bs4 import BeautifulSoup
from properties.parser import otodom_search_parser, otodom_get_parser
from scraper.items import ScraperItem
from scrapy_splash import SplashRequest

# current_dir = os.path.dirname(__file__)
# url = os.path.join(current_dir, 'otodom-results.html')


# class PropertiesSpider(CrawlSpider):
class PropertiesSpider(Spider):
    name = "js_rendered"
    custom_settings = {
        
    }
    # allowed_domains = ["realestatedatabase.net"]
    # start_urls = [
    #     "https://realestatedatabase.net/FindAHouse/houses-for-rent-in-kampala-uganda.aspx?Title=Houses+for+rent+in+kampala"
    # ]
    # start_urls = [f"file://{url}"]
    # start_urls = ["https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/grodzisk-mazowiecki?distanceRadius=0&market=ALL&priceMin=20&priceMax=400000&viewType=listing&lang=pl&searchingCriteria=sprzedaz,mieszkanie,cala-polska"]
    # rules = (
    #     Rule(
    #         LinkExtractor(allow=("/pl/oferta/")),
    #         callback="parse_property",
    #         follow=True,
    #     ),
    # )

    def start_requests(self):
        url = 'https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/grodzisk-mazowiecki?distanceRadius=0&market=ALL&priceMin=20&priceMax=400000&viewType=listing&lang=pl&searchingCriteria=sprzedaz,mieszkanie,cala-polska'
        # url = "https://realestatedatabase.net/FindAHouse/houses-for-rent-in-kampala-uganda.aspx?Title=Houses+for+rent+in+kampala"
        yield SplashRequest(url, callback=self.parse, args={'wait': 0.5, 'url':url})

    def parse(self, response):
        with open("otodom-search2.html", "w") as file:
            file.write(response.text)
        search_results = otodom_search_parser(response)
        
        for result in search_results:
            print('******************', result.title, '//////////////////', result.offer_url)
            item = ScraperItem()
            item["price"] = result.title
            item["location"] = result.offer_url
            yield item


    # def parse_property(self, response):
    #     result = otodom_get_parser(response)
    #     item = ScraperItem()
    #     item["price"] = result["price"]
    #     item["location"] = result["title"]
    #     yield item
        # property_loader = ItemLoader(item=ScraperItem(), response=response)
        # property_loader.default_output_processor = TakeFirst()

        # property_loader.add_css(
        #     "price", "span#ContentPlaceHolder1_DetailsFormView_Shillings::text"
        # )
        # property_loader.add_css(
        #     "location", "span#ContentPlaceHolder1_DetailsFormView_LocationLabel::text"
        # )

        # yield property_loader.load_item()