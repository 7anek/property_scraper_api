import os
from scrapy.spiders import CrawlSpider, Spider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from bs4 import BeautifulSoup
from properties.parser import otodom_search_parser, otodom_get_parser
# from scraper.items import ScraperItem
# from scraper.scraper.items import ScraperItem
from scrapy import Request
import math
import re
from datetime import datetime
from urllib.parse import urljoin, urlencode, urlparse, urlunparse, unquote, parse_qs
import chompjs
import json
from properties.otodom import *
from properties.utils import *

# current_dir = os.path.dirname(__file__)
# url = os.path.join(current_dir, 'otodom-results.html')


class PropertiesSpider(Spider):
# class PropertiesSpider(Spider):
    name = "otodom"
    service_name = "otodom"
    domain = "www.otodom.pl"
    scheme = "http"
    results_per_page = 24
    # allowed_domains = ["realestatedatabase.net"]
    # start_urls = [
    #     "https://realestatedatabase.net/FindAHouse/houses-for-rent-in-kampala-uganda.aspx?Title=Houses+for+rent+in+kampala"
    # ]
    # start_urls = [f"file://{url}"]
    # start_urls = ["http://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/grodzisk-mazowiecki?distanceRadius=0&market=ALL&priceMin=20&priceMax=400000&viewType=listing&lang=pl&searchingCriteria=sprzedaz,mieszkanie,cala-polska&limit=24&page=1"]
    # rules = (
    #     Rule(
    #         LinkExtractor(allow=("/pl/oferta/")),
    #         callback="parse_property",
    #         follow=True,
    #     ),
    # )
    # def __init__(self, search_form):
    #     super(__init__(self))
    #     print('+++++++++++++++++', search_form)
    def __init__(self, *args, **kwargs):
        super(PropertiesSpider, self).__init__(*args, **kwargs)
        print('00000000', 'args', args)
        print('00000000', 'kwargs', kwargs)
        search_form_json = kwargs.get('search_form', False)
        self.scrapyd_job_id = kwargs.get('_job')
        search_form = json.loads(search_form_json) if search_form_json else {}
        print('00000000', 'search_form disct', search_form)
        search_form = dict_filter_none(search_form)
        if search_form:

            #add pagination params
            search_form["limit"]=self.results_per_page
            search_form["page"] = 1

            self.search_form = search_form
            self.current_url = self.url_from_params()
            self.start_urls = [self.current_url]
        else:
            self.search_form = search_form
            self.query_params = ''
            self.current_url = ''
            self.start_urls = []
        # self.start_urls = []

    def parse(self, response):
    #     pass
    # def parse2(self, response):
        # with open("otodom-search2.html", "w") as file:
        #     file.write(response.text)
        
        print('1111111111111111', response.request.url)
        current_page = parse_qs(urlparse(response.request.url).query)['page']
        if not current_page:
            return False
        print('2222222222222222222', current_page)
        soup = BeautifulSoup(response.text, 'lxml')
        num_results = int(soup.find("strong",{"data-cy":"search.listing-panel.label.ads-number"}).span.next_sibling.next_sibling.text)
        if not num_results:
            return False
        print('3333333333333333333333', num_results)
        results_per_page = 24
        num_pages = math.ceil(num_results/results_per_page)

        if num_pages and int(current_page[0]) == 1:
            print('44444444444444444444', 'aaaaaaaaaaaaaaa')
            for i in range(2,num_pages+1):
                self.search_form["page"] = i
                self.current_url = self.url_from_params()
                yield response.follow(self.current_url)

        print('555555555555555555')
        m = re.search(r"ad_impressions\":\[((\d+,)*\d+)\]", response.text)
        offers_ids = list(set((m.group(1).split(","))))
        print('6666666666666666666', offers_ids)
        domain = "http://www.otodom.pl/"
        offers_urls = list(map(lambda offer_id : domain+offer_id, set((m.group(1).split(",")))))
        for offer_url in offers_urls:
            yield response.follow(offer_url, callback=self.parse_get)

        # offers_html = soup.find_all('a', {"data-cy": "listing-item-link"})
        # for offer in offers_html:
        #     print('******************', offer['href'], '//////////////////')
        #     yield response.follow("https://www.otodom.pl"+offer['href'], callback=self.parse_get)

    def parse_get(self, response):
        print('777777777777777777', 'parse_get', 'job id', self.scrapyd_job_id)
        js = response.css("script#__NEXT_DATA__::text").get()
        data = chompjs.parse_js_object(js)
        offer_dict = data["props"]["pageProps"]["ad"]

        # item = ScraperItem()
        item = {}
        item["scrapyd_job_id"] = self.scrapyd_job_id
        item["service_id"] = parse_service_id(offer_dict["id"])
        item["service_name"] = self.service_name
        item["title"] = offer_dict["title"]
        item["price"] = offer_dict["target"]["Price"]
        item["location"] = ", ".join([offer_dict["target"]["City"], offer_dict["target"]["Subregion"],offer_dict["target"]["Province"]])
        item["description"] = offer_dict["description"]
        item["area"] = offer_dict["target"]["Area"]
        item["floor"] = parse_floor(offer_dict["target"]["Floor_no"]) if "Floor_no" in offer_dict["target"] else None
        item["number_of_rooms"] = int(offer_dict["target"]["Rooms_num"][0]) if "Rooms_num" in offer_dict["target"] else None
        item["type_of_property"] = offer_dict["target"]["ProperType"] 
        item["type_of_building"] = parse_type_of_building(offer_dict) if "Building_type" in offer_dict["target"] else None
        item["create_date"] = datetime.fromisoformat(offer_dict["createdAt"])
        item["modify_date"] = datetime.fromisoformat(offer_dict["modifiedAt"])

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
    def url_from_params(self):
        path = url_path(self.search_form)
        query = url_query(self.search_form)
        return generate_url(scheme=self.scheme, netloc=self.domain, path=path, query=query)

def parse_service_id(service_id):
    if type(service_id) == int:
        return service_id
    else:
        print('uknown service id', service_id, type(service_id))
        return service_id


def parse_floor(floor_no):

    m = re.search(r"floor_(\d+)", floor_no[0])
    if m:
        num = m.group(1)
        if num:
            return int(num)
        
def parse_type_of_building(offer_dict):
    try:
        type_of_building = offer_dict["target"]["Building_type"]
    except KeyError:
        type_of_building = None
    return type_of_building


