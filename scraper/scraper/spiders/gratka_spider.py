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
from datetime import datetime,date, timedelta
from urllib.parse import urljoin, urlencode, urlparse, urlunparse, unquote, parse_qs
import chompjs
import json
from properties.otodom import *
from properties.utils import *
from properties.models import Property
from properties import gratka, otodom
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# current_dir = os.path.dirname(__file__)
# url = os.path.join(current_dir, 'otodom-results.html')


class GratkaSpider(Spider):
# class PropertiesSpider(Spider):
    name = "gratka"
    service_name = "gratka"
    domain = "gratka.pl"
    scheme = "http"
    results_per_page = 32
    first_offer_detail=True

    
    def __init__(self, *args, **kwargs):
        super(GratkaSpider, self).__init__(*args, **kwargs)
        search_form_json = kwargs.get('search_form', False)
        self.scrapyd_job_id = kwargs.get('_job')
        search_form = json.loads(search_form_json) if search_form_json else {}

        search_form = dict_filter_none(search_form)
        if search_form:
            #add pagination params
            search_form["limit"]=self.results_per_page
            search_form["page"] = 1
            self.use_playwright = 'district_neighbourhood' in search_form
            self.search_form = search_form
            self.current_url = self.url_from_params()
            self.start_urls = [self.current_url]
        else:
            self.search_form = search_form
            self.query_params = ''
            self.current_url = ''
            self.start_urls = []

    def start_requests(self):
        if self.use_playwright:
            for url in self.start_urls:
                selenium = selenium_browser()
                selenium.get(url)
                selenium.implicitly_wait(3)
                selenium.save_screenshot("../test_data/gratka/gratka1.png")
                selenium.find_element("css selector","button.cmp-intro_acceptAll").click()
                selenium.find_element("css selector",'i.locationSuggester__eraser').click()
                selenium.find_element("css selector",'input[name="lokalizacja_region"]').send_keys(self.search_form['formatted_address'])
                selenium.find_element("css selector",'ul.category__results li:first-child').click()
                selenium.find_element("css selector","body").click()
                # selenium.implicitly_wait(5)
                selenium.save_screenshot("../test_data/gratka/gratka2.png")
                selenium.find_element("css selector",'button[data-cy="submitSearch"]').click()
                selenium.save_screenshot("../test_data/gratka/gratka3.png")
                print('selenium.current_url',selenium.current_url)
                new_url=selenium.current_url+"&page=1"
                selenium.close()
                yield Request(url=new_url)
        else:
            for url in self.start_urls:
                yield Request(url=url)


    def parse(self, response):
        
        parsed_url_query = url_to_params_dict(response.request.url)

        if not 'page' in parsed_url_query:
            print('not page in parsed_url')
            return False
        
        current_page = parsed_url_query['page']
        if not current_page:
            print('not current_page')
            return False

        url_path=get_url_path(response.request.url)
        district_neighbourhood_cand=url_path.split("/")[-1]
        if re.search(r'[a-z]+\-\d+', district_neighbourhood_cand):
            self.search_form["district_neighbourhood_from_url"]=district_neighbourhood_cand

        soup = BeautifulSoup(response.text, 'html.parser')

        num_results=gratka.get_results_count(soup)
        if not num_results:
            return False

        # results_per_page = 24
        num_pages = math.ceil(num_results/self.results_per_page)

        if num_pages and int(current_page) == 1:
            for i in range(2,num_pages+1):
                self.current_url = self.url_from_params(page=i)
                yield response.follow(self.current_url)

        m = re.search(r"allOffersIds \= \[((\d+,)*\d+)\]", response.text)
        offers_ids = list(set((m.group(1).split(","))))
        property_type=gratka.property_type_mapping[self.search_form['property_type']]
        domain = generate_url(scheme=self.scheme,netloc=self.domain, path=f'/nieruchomosci/{property_type}/ob/')
        offers_urls = list(map(lambda offer_id : domain+offer_id, set((m.group(1).split(",")))))
        for offer_url in offers_urls:
            yield response.follow(offer_url, callback=self.parse_offer)

        # offers_html = soup.find_all('a', {"data-cy": "listing-item-link"})
        # for offer in offers_html:
        #     print('******************', offer['href'], '//////////////////')
        #     yield response.follow("https://www.otodom.pl"+offer['href'], callback=self.parse_get)

    def parse_offer(self, response):
        # if self.first_offer_detail:
        #     with open("/home/janek/python/property_scraper/test_data/gratka-details.html", "w") as file:
        #         file.write(response.text)
        soup = BeautifulSoup(response.text, 'html.parser')
        js=next(filter(lambda t: "PPDataLayer.push({" in t.text, soup.body.find_all("script", resursive=False))).text
        data = chompjs.parse_js_object(js)
        
        js2=next(filter(lambda t: "@graph" in t.text,soup.find_all("script", {"type":"application/ld+json"},resursive=False))).text
        data2 = chompjs.parse_js_object(js2)["@graph"][0]

        # item = ScraperItem()
        item = {}
        item=localization_fields_from_search_form(item, self.search_form)
        item["scrapyd_job_id"] = self.scrapyd_job_id
        item["service_id"] = data["id_oferty"]
        item["service_name"] = self.service_name
        item["service_url"] = response.request.url
        item["title"] = data2["name"]
        item["price"] = data["cena"]
        item["description"] = data2["description"]
        item["area"] = data["powierzchnia_m2"]
        item["floor"] = data2["floorLevel"] if "floorLevel" in data2 else None
        item["number_of_rooms"] = data2["numberOfRooms"] if "numberOfRooms" in data2 else None
        item["type_of_property"] = parse_type_of_property(data["podkategoria"]) if "podkategoria" in data else self.search_form["property_type"]
        item["type_of_building"] = parse_type_of_building(data2["@type"]) if "@type" in data2 and data["podkategoria"]=="mieszkania" else None
        item["type_of_plot"] = parse_type_of_plot(data2["@type"]) if "@type" in data2 and data["podkategoria"]=="dzialki-grunty" else None
        item["latitude"]=data2['geo']['latitude'] if 'geo' in data2 else None
        item["longitude"]=data2['geo']['longitude'] if 'geo' in data2 else None
        item["year_of_construction"]= data2["yearBuilt"] if "yearBuilt" in data2 else None
        item["create_date"] = parse_create_date(soup)
        item["modify_date"] = parse_modify_date(soup)

        # self.first_offer_detail=False

        yield item       
        

    def url_from_params(self,page=1):
        path = gratka.get_url_path(self.search_form)
        query = gratka.get_url_query(self.search_form,page=page)
        return generate_url(scheme=self.scheme, netloc=self.domain, path=path, query=query)
    




def parse_type_of_building(type_of_building):
    if type_of_building == "Apartment":
        return Property.TypesOfFlats.BLOCK_OF_FLATS.value
    elif type_of_building == "tenement":
        return Property.TypesOfFlats.TENEMENT.value
    elif type_of_building == "apartment":
        return Property.TypesOfFlats.APARTMENT.value
    return type_of_building


def parse_type_of_property(type):
    if type == "mieszkania":
        return Property.TypesOfProperties.FLAT.value
    elif type == "dzialki-grunty":
        return Property.TypesOfProperties.PLOT.value
    else:
        return type

def parse_type_of_plot(type):
    if type == "building":
        return Property.TypesOfPlots.BUILDING.value
    elif type == "Place":
        return Property.TypesOfPlots.AGRICULTURAL.value
    elif type == "recreational":
        return Property.TypesOfPlots.RECREATIONAL.value
    elif type == "woodland":
        return Property.TypesOfPlots.FOREST.value
    return type

def parse_create_date(soup):
    return parse_date(soup,"Dodane")

def parse_modify_date(soup):
    return parse_date(soup,"Zaktualizowane")

def parse_date(soup, str):
    date_str=next(filter(lambda t: str in t.text,soup.find_all("li"))).div.text
    if date_str=="dziś":
        return date.today()
    elif date_str=="wczoraj":
        return date.today()+timedelta(days=-1)
    else:
        return None