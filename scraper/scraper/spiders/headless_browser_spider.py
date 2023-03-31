import os
from scrapy.spiders import CrawlSpider, Spider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from bs4 import BeautifulSoup
from properties.parser import otodom_get_parser
from scraper.items import ScraperItem
from scrapy_splash import SplashRequest
import scrapy
from scrapy_playwright.page import PageMethod

# current_dir = os.path.dirname(__file__)
# url = os.path.join(current_dir, 'otodom-results.html')

class SearchResult:
    offer_url = ''
    offer_url_path = ''
    main_image_url = ''
    title = ''
    price = ''
    price_per_square_meter = ''
    number_of_rooms = ''
    area = ''
    service=''

def otodom_search_parser(response):
    print('//////////////////','otodom_search_parser',',,,,,,,,,,,,,')
    # soup = BeautifulSoup(response.text, 'html.parser')
    soup = BeautifulSoup(response.text, 'lxml')
    offers_html = soup.find_all('a', {"data-cy": "listing-item-link"})
    results_arr = []
    for offer in offers_html:
        search_result = SearchResult()
        search_result.offer_url = "https://www.otodom.pl"+offer['href']
        search_result.main_image_url = offer.find("img")["src"]
        title_tag = offer.find("h3", {"data-cy": "listing-item-title"})
        search_result.title = title_tag.text
        # params_arr = title_tag.find_next("div").find_all("span")
        # search_result.price = params_arr[0].text
        # search_result.price_per_square_meter = params_arr[1].text
        # search_result.number_of_rooms = params_arr[2].text
        # search_result.area = params_arr[3].text
        search_result.service =  "otodom"

        results_arr.append(search_result)

        print('***** otodom url:', search_result.offer_url)
        print('***** otodom url path:', search_result.offer_url_path)

    return results_arr
# class PropertiesSpider(CrawlSpider):
class PropertiesSpider(Spider):
    name = "headless_browser_spider"


    def start_requests(self):
        url = 'https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/grodzisk-mazowiecki?distanceRadius=0&market=ALL&priceMin=20&priceMax=400000&viewType=listing&lang=pl&searchingCriteria=sprzedaz,mieszkanie,cala-polska'
        yield scrapy.Request(url, meta=dict(
            playwright= True,
            playwright_page_methods =[
        #   PageMethod("wait_for_selector", "div.quote"),
          PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)"),
          PageMethod("wait_for_selector", "div.quote:nth-child(11)"),  # 10 per page
          ],
        errback=self.errback,
            ))

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

    