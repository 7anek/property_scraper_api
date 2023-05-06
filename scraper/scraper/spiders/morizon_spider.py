import os
from scraper.utils import *
from scrapy.spiders import Spider
from bs4 import BeautifulSoup
import math
import re
from datetime import datetime,date, timedelta
from urllib.parse import urljoin, urlencode, urlparse, urlunparse, unquote, parse_qs
import chompjs
import json
from properties.otodom import *
from properties.utils import *
from properties.models import Property
from properties import morizon


class MorizonSpider(Spider):
    name = "morizon"
    service_name = "morizon"
    domain = "www.morizon.pl"
    scheme = "http"
    results_per_page = 35
    first_offer_detail=True

    
    def __init__(self, *args, **kwargs):
        super(MorizonSpider, self).__init__(*args, **kwargs)
        search_form_json = kwargs.get('search_form', False)
        self.scrapyd_job_id = kwargs.get('_job')
        search_form = json.loads(search_form_json) if search_form_json else {}

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


    def parse(self, response):
        
        parsed_url = url_to_params_dict(response.request.url)

        if not 'page' in parsed_url:
            print('not page in parsed_url')
            return False
        
        current_page = parsed_url['page']
        if not current_page:
            print('not current_page')
            return False

        soup = BeautifulSoup(response.text, 'html.parser')

        num_results=morizon.get_results_count(soup)
        if not num_results:
            return False

        num_pages = math.ceil(num_results/self.results_per_page)

        if num_pages and int(current_page) == 1:
            for i in range(2,num_pages+1):
                self.current_url = self.url_from_params(page=i)
                yield response.follow(self.current_url)

        js=next(filter(lambda t: '"@type":"OfferCatalog"' in t.text,soup.head.find_all("script",{"type":"application/ld+json","data-n-head":"ssr"}))).text
        data = chompjs.parse_js_object(js)
        for offer in data["itemListElement"]:
            yield response.follow(data["itemListElement"][offer]["url"], callback=self.parse_offer)


    def parse_offer(self, response):
        # if self.first_offer_detail:
        #     with open("/home/janek/python/property_scraper/test_data/morizon-details.html", "w") as file:
        #         file.write(response.text)
        soup = BeautifulSoup(response.text, 'html.parser')
        # js=next(filter(lambda t: "PPDataLayer.push({" in t.text, soup.body.find_all("script", resursive=False))).text
        # data = chompjs.parse_js_object(js)
        detailed_information_set=soup.find_all("div",{"class":"detailed-information__row"})
        service_id_str=get_detail_information_text(detailed_information_set,"Numer ogłoszenia")
        if re.search("gratka|otodom|olx", service_id_str):
            #oferta z innego serwisu
            return False
        # item = ScraperItem()
        details_row_set=soup.find("div",{"class":"details-row"}).find_all("span",{"class":"details-row__text"})

        item = {}
        item=localization_fields_from_search_form(item, self.search_form)
        item["scrapyd_job_id"] = self.scrapyd_job_id
        item["service_id"] = int(service_id_str.split("-")[-1])
        item["service_name"] = self.service_name
        item["service_url"] = response.request.url
        item["title"] = soup.find("h3",{"class":"description__title"}).get_text("",strip=True)
        item["price"] = float(re.sub(r"[^\d.,]","",soup.find("span",{"class":"price-row__price"}).text).replace(",","."))
        item["description"] = soup.find("div",{"class":"description"}).get_text("",strip=True)#wczytuje tylko nagłówek
        item["area"] = float(re.sub(r"[^\d.,]","",get_detail_information_text(detailed_information_set,"Pow. całkowita")).replace(",","."))
        item["floor"] = self.parse_floor(detailed_information_set, details_row_set)
        item["number_of_rooms"] = self.parse_number_of_rooms(detailed_information_set, details_row_set)
        item["type_of_property"] = self.search_form["property_type"]
        item["type_of_building"] = self.parse_type_of_building(detailed_information_set)
        item["type_of_plot"] = None
        item["create_date"] = parse_create_date(detailed_information_set)
        item["modify_date"] = parse_modify_date(detailed_information_set)

        # self.first_offer_detail=False

        yield item       
        

    def url_from_params(self,page=1):
        path = morizon.get_url_path(self.search_form)
        query = morizon.get_url_query(self.search_form,page=page)
        return generate_url(scheme=self.scheme, netloc=self.domain, path=path, query=query)
    
    def parse_floor(self, detailed_information_set, details_row_set):
        if self.search_form["property_type"] != "flat":
            return None
        try:
            floor_str=get_detail_information_text(detailed_information_set,"Piętro").split("/")[0]
            if floor_str in ['parter','Parter']:
                return 0
            else:
                return int(floor_str)
        except:
            f=next(filter(lambda t: re.search('[pP]iętro|[pP]arter]',t.text),details_row_set),None)
            if f:
                s=f.get_text("",strip=True)
                m=re.search("(\d+)/\d",s)
                if m:
                    return int(m.group(1))
                else:
                    m=re.search('[pP]arter]',s)
                    if m:
                        return 0
    
    def parse_number_of_rooms(self, detailed_information_set, details_row_set):
        if self.search_form["property_type"] != "flat":
            return None
        f=next(filter(lambda t: re.search('[pP]ok',t.text),details_row_set),None)
        if f:
            s=f.get_text("",strip=True)
            m=re.search("(\d+)",s)
            if m:
                return int(m.group(1))

    def parse_type_of_building(self,detailed_information_set):
        if self.search_form["property_type"] != "flat":
            return None
        type_of_building=get_detail_information_text(detailed_information_set,"Typ budynku")
        if not type_of_building:
            return None
        type_of_building=type_of_building.lower()
        if type_of_building == "blok":
            return Property.TypesOfFlats.BLOCK_OF_FLATS.value
        elif type_of_building == "kamienica":
            return Property.TypesOfFlats.TENEMENT.value
        elif type_of_building == "apartament":
            return Property.TypesOfFlats.APARTMENT.value
        return type_of_building


    def parse_type_of_plot(self,detailed_information_set):
        if self.search_form["property_type"] != "plot":
            return None
        if type == "building":
            return Property.TypesOfPlots.BUILDING.value
        elif type == "Place":
            return Property.TypesOfPlots.AGRICULTURAL.value
        elif type == "recreational":
            return Property.TypesOfPlots.RECREATIONAL.value
        elif type == "woodland":
            return Property.TypesOfPlots.FOREST.value
        return type

    
def get_detail_information_text(detailed_information_set,label):
    f=filter(lambda t: label in t.text,detailed_information_set)
    if f:
        return next(f).find("div",{"class":"detailed-information__cell detailed-information__cell--value"}).div.text

def get_details_row_text(details_row_set,label):
    f=next(filter(lambda t: re.search('[pP]iętro|[pP]arter]',t.text),details_row_set),None)
    if f:
        return
    return next(filter(lambda t: label in t.text,detailed_information_set),None).find("div",{"class":"detailed-information__cell detailed-information__cell--value"}).div.text


def parse_create_date(detailed_information_set):
    return parse_date(detailed_information_set,"Data dodania")

def parse_modify_date(detailed_information_set):
    return parse_date(detailed_information_set,"Aktualizacja")

def parse_date(detailed_information_set, label):
    d=get_detail_information_text(detailed_information_set,label)
    if d:
        return datetime.strptime(d,"%d.%m.%Y")
    