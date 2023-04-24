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
from datetime import datetime,date
from urllib.parse import urljoin, urlencode, urlparse, urlunparse, unquote, parse_qs
import chompjs
import json
from properties.otodom import *
from properties.utils import *
from properties.models import Property
from properties import olx
# current_dir = os.path.dirname(__file__)
# url = os.path.join(current_dir, 'otodom-results.html')


class OlxSpider(Spider):
# class PropertiesSpider(Spider):
    name = "olx"
    service_name = "olx"
    domain = "www.olx.pl"
    scheme = "https"
    first_offer_detail=True
    last_page=False

    
    def __init__(self, *args, **kwargs):
        super(OlxSpider, self).__init__(*args, **kwargs)
        search_form_json = kwargs.get('search_form', False)
        self.scrapyd_job_id = kwargs.get('_job')
        search_form = json.loads(search_form_json) if search_form_json else {}

        search_form = dict_filter_none(search_form)
        if search_form:
            #add pagination params
            # search_form["limit"]=self.results_per_page
            search_form["page"] = 1

            self.search_form = search_form
            self.current_url = self.url_from_params()
            self.start_urls = [self.current_url]
        else:
            self.search_form = search_form
            self.query_params = ''
            self.current_url = ''
            self.start_urls = []


    def parse(self, response):
        parsed_url = parse_qs(urlparse(response.request.url).query)

        if not 'page' in parsed_url:
            # print('not page in parsed_url')
            # return False
            current_page=1
        else:
            current_page = int(parsed_url['page'][0])
        # current_page = parsed_url['page']
        # if not current_page:
        #     print('not current_page')
        #     return False

        soup = BeautifulSoup(response.text, 'html.parser')

        num_results=self.get_results_num(soup)
        if not num_results:
            return False

        if(soup.find("div", {"class": "css-wsrviy"})):
            self.last_page=True

        # results_per_page = 24
        # num_pages = math.ceil(num_results/results_per_page)

        if int(current_page) == 1:
            i=2
            while not self.last_page: 
                self.search_form["page"] = i
                i=i+1
                self.current_url = self.url_from_params()
                yield response.follow(self.current_url)
                
        search_results_soup = soup.find("div", {"data-testid":"listing-grid"}).find_all("a")
        domain = generate_url(scheme=self.scheme,netloc=self.domain)
        offers_urls=list(map(lambda offer_soup: domain+offer_soup["href"],filter(lambda offer_soup: not offer_soup["href"].startswith(("https://www.otodom.pl","www.otodom.pl")),search_results_soup)))
        for offer_url in offers_urls:
            yield response.follow(offer_url, callback=self.parse_offer)


    def parse_offer(self, response):
        # if self.first_offer_detail:
        #     with open("/home/janek/python/property_scraper/test_data/olx-details.html", "w") as file:
        #         file.write(response.text)
        soup=BeautifulSoup(response.text,"html.parser")

        # item = ScraperItem()
        item = {}
        item["scrapyd_job_id"] = self.scrapyd_job_id
        item["service_id"] = parse_service_id(soup)
        item["service_name"] = self.service_name
        item["title"] = soup.find("h1").text
        item["price"] = parse_price(soup)
        item["location"] = self.search_form["localization"]
        item["description"] = soup.find("div",class_="css-bgzo2k").text
        item["area"] = float(soup.find(lambda s: s.name=="p" and "Powierzchnia:" in s.text).text.split()[1].replace(",","."))
        item["floor"] = parse_floor(soup)
        item["number_of_rooms"] = int(soup.find(lambda s: s.name=="p" and "Liczba pokoi:" in s.text).text.split()[2])
        item["type_of_property"] = self.search_form["property_type"]
        item["type_of_building"] = parse_type_of_building(soup)
        item["create_date"] = parse_create_date(soup)
        item["modify_date"] = item["create_date"]

        # self.first_offer_detail=False

        yield item

    
    
    def url_from_params(self):
        path = olx.get_url_path(self.search_form)
        query = olx.get_request_params(self.search_form)
        return generate_url(scheme=self.scheme, netloc=self.domain, path=path, query=query)
    
    def get_results_num(self, soup):
        num_results = int(soup.find("div",{"data-testid":"total-count"}).text.split()[1])
        return num_results

def parse_service_id(soup):
    try:
        service_id=int(soup.find("span",class_="css-12hdxwj").text.split()[1])
    except Exception as e:
        print(e)
        service_id=None
    return service_id

def parse_price(soup):
    try:
        price=float(''.join(filter(str.isdigit,soup.find("h3").text)))
    except Exception as e:
        print(e)
        price=None
    return price

def parse_floor(soup):
    try:
        floor_str=soup.find(lambda s: s.name=="p" and "Poziom:" in s.text).text.split()[1]
        if floor_str=="Parter":
            floor=0
        else:
            floor=int(floor_str)
    except Exception as e:
        print(e)
        floor=None
    return floor
    
        
def parse_type_of_building(soup):
    
    try:
        type_of_building=soup.find(lambda s: s.name=="p" and "Rodzaj zabudowy:" in s.text).text.split()[2]
    except Exception as e:
        print(e)
        type_of_building = None
    if type_of_building == "Blok":
        return Property.TypesOfFlats.BLOCK_OF_FLATS.value
    elif type_of_building == "Kamienica":
        return Property.TypesOfFlats.TENEMENT.value
    elif type_of_building == "Apartamentowiec":
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

def parse_create_date(soup):
    try:
        data_str=soup.find("span",{"data-cy":"ad-posted-at"}).text
        dzien, miesiac_str, rok = data_str.split()
        if(dzien=='Dzisiaj'):
            data = date.today()#można jeszcze godzine i minute dodać
        else:
            month_dict = {
                'stycznia': 1,
                'lutego': 2,
                'marca': 3,
                'kwietnia': 4,
                'maja': 5,
                'czerwca': 6,
                'lipca': 7,
                'sierpnia': 8,
                'września': 9,
                'października': 10,
                'listopada': 11,
                'grudnia': 12
            }
            miesiac = month_dict[miesiac_str]
            data = datetime(int(rok), miesiac, int(dzien))
    except Exception as e:
        print(e)
        data=date.today()
    return data