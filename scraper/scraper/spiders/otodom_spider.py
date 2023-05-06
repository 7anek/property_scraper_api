import os
from scraper.utils import *
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
from properties.models import Property
from properties import otodom
from scrapy_playwright.page import PageMethod
from playwright.sync_api import Page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# current_dir = os.path.dirname(__file__)
# url = os.path.join(current_dir, 'otodom-results.html')


class OtodomSpider(Spider):
# class PropertiesSpider(Spider):
    name = "otodom"
    service_name = "otodom"
    domain = "www.otodom.pl"
    scheme = "http"
    results_per_page = 24
    first_offer_detail=True

    
    def __init__(self, *args, **kwargs):
        super(OtodomSpider, self).__init__(*args, **kwargs)
        search_form_json = kwargs.get('search_form', False)
        self.scrapyd_job_id = kwargs.get('_job')
        search_form = json.loads(search_form_json) if search_form_json else {}

        search_form = dict_filter_none(search_form)
        # do testowania z konsoli
        # if not search_form:
        #     search_form={'formatted_address': 'Elektoralna, Warszawa, Polska', 'province': 'Mazowieckie', 'city': 'Warszawa', 'district': 'Śródmieście','street':'Elektoralna', 'price_min': 300000, 'price_max': 1000000, 'property_type': 'flat', 'offer_type': 'sell'}  

        if search_form:
            #add pagination params
            search_form["limit"]=self.results_per_page
            search_form["page"] = 1
            self.use_playwright = 'street' in search_form
            self.search_form = search_form
            self.current_url = self.url_from_params()
            self.start_urls = [self.current_url]
        else:
            self.search_form = search_form
            self.query_params = ''
            self.current_url = ''
            self.use_playwright = False
            self.start_urls = []


    def start_requests(self):
        if self.use_playwright:
            for url in self.start_urls:
                selenium = selenium_browser()
                selenium.get(url)
                selenium.implicitly_wait(3)
                selenium.save_screenshot("../test_data/otodom/otodom1.png")
                selenium.find_element("id","onetrust-accept-btn-handler").click()
                selenium.find_element("id","location").click()
                selenium.find_element("css selector",'ul[data-testid="selected-locations"] > li:nth-child(2)').click()
                selenium.find_element("id",'location-picker-input').send_keys(self.search_form["formatted_address"])
                selenium.find_element("css selector",'ul.css-1tsmnl6 li:first-child').click()
                selenium.save_screenshot("../test_data/otodom/otodom2.png")
                selenium.find_element("id","search-form-submit").click()
                selenium.implicitly_wait(3)
                selenium.save_screenshot("../test_data/otodom/otodom3.png")
                print('selenium.current_url',selenium.current_url)
                new_url=selenium.current_url
                selenium.close()
                yield Request(url=new_url)
        #         yield Request(url=url,  meta={
        #     "playwright": True,
        #     "playwright_include_page": True,
        #     "playwright_page_methods": [
        #         PageMethod("screenshot", path="../test_data/otodom/otodom1.png"),
        #         PageMethod("wait_for_selector",'#onetrust-accept-btn-handler'),
        #         PageMethod("click",'#onetrust-accept-btn-handler'),
        #         PageMethod("screenshot", path="../test_data/otodom/otodom2.png"),
        #         PageMethod("fill",'#areaMin', value="50"),
        #         # PageMethod("click",'#location'),
        #         # PageMethod("wait_for_selector",'ul[data-testid="selected-locations"] > li:nth-child(2)'),
        #         # PageMethod("click",'ul[data-testid="selected-locations"] > li:nth-child(2)'),
        #         # PageMethod("fill",'#location-picker-input', value=self.search_form["formatted_address"]),
        #         # PageMethod("screenshot", path="../test_data/otodom/otodom3.png"),
        #         # PageMethod("click",'ul.css-1tsmnl6 li:first-child'),
        #         # PageMethod("wait_for_selector",'#search-form-submit'),
        #         PageMethod("wait_for_selector","#search-form-submit", timeout=5000),
        #         PageMethod("submit",'#search-form-submit', delay=5000),
        #         PageMethod("screenshot", path="../test_data/otodom/otodom4.png"),
        #         # PageMethod("_click_accept_cookies"),
        #         # PageMethod("_set_location"),
        #         # PageMethod("_submit_search_form"),
        #         # PageMethod("screenshot", path="../test_data/otodom/otodom.png"),
        #     ],
        # },)
        else:
            for url in self.start_urls:
                yield Request(url=url)

    def parse(self, response):
        # return True
        print('response.request.url',response.request.url)
        parsed_url_query = url_to_params_dict(response.request.url)
        print('parsed_url_query',parsed_url_query)
        if not 'page' in parsed_url_query:
            print('not page in parsed_url')
            return False
        
        current_page = parsed_url_query['page']
        if not current_page:
            print('not current_page')
            return False
        print('current_page',current_page)
        #tu chce wyszukać ulice

        num_results=self.get_results_num(response)
        if not num_results:
            return False
        print('num_results', num_results)
        results_per_page = 24
        num_pages = math.ceil(num_results/results_per_page)
        print('num_pages', num_pages)

        if 'locations' in parsed_url_query:
            self.search_form['locations'] = parsed_url_query['locations']
        # return True
        if num_pages and int(current_page) == 1:
            for i in range(2,num_pages+1):
                self.current_url = self.url_from_params(page=i, limit=results_per_page)
                yield response.follow(self.current_url)

        m = re.search(r"ad_impressions\":\[((\d+,)*\d+)\]", response.text)
        offers_ids = list(set((m.group(1).split(","))))
        domain = "http://www.otodom.pl/"
        offers_urls = list(map(lambda offer_id : domain+offer_id, set((m.group(1).split(",")))))
        for offer_url in offers_urls:
            yield response.follow(offer_url, callback=self.parse_offer)

        # offers_html = soup.find_all('a', {"data-cy": "listing-item-link"})
        # for offer in offers_html:
        #     print('******************', offer['href'], '//////////////////')
        #     yield response.follow("https://www.otodom.pl"+offer['href'], callback=self.parse_get)

    def parse_offer(self, response):
        # if self.first_offer_detail:
        #     with open("/home/janek/python/property_scraper/test_data/otodom-details.html", "w") as file:
        #         file.write(response.text)
        js = response.css("script#__NEXT_DATA__::text").get()
        data = chompjs.parse_js_object(js)
        offer_dict = data["props"]["pageProps"]["ad"]

        # item = ScraperItem()
        item = {}
        item=localization_fields_from_search_form(item, self.search_form)

        item["scrapyd_job_id"] = self.scrapyd_job_id
        item["service_id"] = parse_service_id(offer_dict["id"])
        item["service_name"] = self.service_name
        item["title"] = offer_dict["title"]
        item["price"] = float(offer_dict["target"]["Price"])
        
        item["description"] = offer_dict["description"]
        item["area"] = float(offer_dict["target"]["Area"])
        item["floor"] = parse_floor(offer_dict["target"]["Floor_no"]) if "Floor_no" in offer_dict["target"] else None
        item["number_of_rooms"] = int(offer_dict["target"]["Rooms_num"][0]) if "Rooms_num" in offer_dict["target"] else None
        item["type_of_property"] = parse_type_of_property(offer_dict["target"]["ProperType"])
        item["type_of_building"] = parse_type_of_building(offer_dict) if "Building_type" in offer_dict["target"] else None
        item["create_date"] = datetime.fromisoformat(offer_dict["createdAt"])
        item["modify_date"] = datetime.fromisoformat(offer_dict["modifiedAt"])

        # self.first_offer_detail=False

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
    def url_from_params(self, page=1, limit=24):
        path = otodom.get_url_path(self.search_form)
        query = otodom.url_query(self.search_form, page=page, limit=limit)
        return generate_url(scheme=self.scheme, netloc=self.domain, path=path, query=query)
    
    def get_results_num(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        print('soup.find("strong",{"data-cy":"search.listing-panel.label.ads-number"})',soup.find("strong",{"data-cy":"search.listing-panel.label.ads-number"}))
        # num_results = int(soup.find("strong",{"data-cy":"search.listing-panel.label.ads-number"}).span.next_sibling.next_sibling.text)
        num_results = int(soup.find("strong",{"data-cy":"search.listing-panel.label.ads-number"}).text.split()[-1])
        return num_results

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
    if offer_dict["target"]["ProperType"] != "mieszkanie":
        return None
    try:
        type_of_building = offer_dict["target"]["Building_type"]
        type_of_building=type_of_building[0]
    except KeyError:
        type_of_building = None
    if type_of_building == "block":
        return Property.TypesOfFlats.BLOCK_OF_FLATS.value
    elif type_of_building == "tenement":
        return Property.TypesOfFlats.TENEMENT.value
    elif type_of_building == "apartment":
        return Property.TypesOfFlats.APARTMENT.value
    return type_of_building


def parse_type_of_property(type):
    if type == "mieszkanie":
        return Property.TypesOfProperties.FLAT.value
    elif type == "dzialka":
        return Property.TypesOfProperties.PLOT.value
    else:
        return type

def parse_type_of_plot(offer_dict):
    if offer_dict["target"]["ProperType"] != "dzialka":
        return None
    try:
        type = offer_dict["target"]["Type"]
        type=type[0]
    except KeyError:
        type = None
    if type == "building":
        return Property.TypesOfPlots.BUILDING.value
    elif type == "agricultural":
        return Property.TypesOfPlots.AGRICULTURAL.value
    elif type == "recreational":
        return Property.TypesOfPlots.RECREATIONAL.value
    elif type == "woodland":
        return Property.TypesOfPlots.FOREST.value
    return type