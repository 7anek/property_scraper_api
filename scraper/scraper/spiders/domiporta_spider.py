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
from properties import domiporta


class DomiportaSpider(Spider):
    name = "domiporta"
    service_name = "domiporta"
    domain = "www.domiporta.pl"
    scheme = "http"
    results_per_page = 35
    first_offer_detail=True

    
    def __init__(self, *args, **kwargs):
        super(DomiportaSpider, self).__init__(*args, **kwargs)
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

        num_results=domiporta.get_results_count(soup)
        if not num_results:
            return False

        num_pages = math.ceil(num_results/self.results_per_page)

        if num_pages and int(current_page) == 1:
            for i in range(2,num_pages+1):
                self.current_url = self.url_from_params(page=i)
                yield response.follow(self.current_url)

        js=re.findall(r"WynikiOdslonaOgloszeniaOrganic'\, ((?:'a\d+'\,?)+)",js,re.MULTILINE)
        ids = re.findall("\d+",js[0])
        property_type=domiporta.property_type_mapping[self.search_form['property_type']]
        url=generate_url(scheme=self.scheme,netloc=self.domain, path=f'/nieruchomosci/{property_type}/')
        for offer in ids:
            yield response.follow(url+offer, callback=self.parse_offer)


    def parse_offer(self, response):
        # if self.first_offer_detail:
        #     with open("/home/janek/python/property_scraper/test_data/domiporta-details.html", "w") as file:
        #         file.write(response.text)
        soup = BeautifulSoup(response.text, 'html.parser')
        features_list=soup.find("ul",{"class":"features__list-2"}).find_all("li")

        item = {}
        item=localization_fields_from_search_form(item, self.search_form)
        item["scrapyd_job_id"] = self.scrapyd_job_id
        item["service_id"] = int(response.request.url.split("/")[-1])
        item["service_name"] = self.service_name
        item["service_url"] = response.request.url
        item["title"] = soup.find("span",{"class":"summary__subtitle-2"}).get_text("",strip=True)
        item["price"] = float(soup.find("span",{"itemprop":"price"})["content"])
        # item["location"] = soup.find("div",{"class":"detials__map__location"}).get_text("",strip=True)
        item["description"] = soup.find("div",{"class":"description__panel"}).get_text("",strip=True)
        item["area"] = float(re.sub(r"[^\d.,]","",list(next(filter(lambda _: "Powierzchnia całkowita" in _.text,features_list)).strings)[1]).replace(",","."))
        item["floor"] = self.parse_floor(features_list)
        item["number_of_rooms"] = self.parse_number_of_rooms(features_list)
        item["type_of_property"] = self.search_form["property_type"]
        item["type_of_building"] = self.parse_type_of_building(features_list)
        item["type_of_plot"] = self.parse_type_of_plot(features_list)
        item["create_date"] = None
        item["modify_date"] = None

        # self.first_offer_detail=False

        yield item       
        

    def url_from_params(self,page=1):
        path = domiporta.get_url_path(self.search_form)
        query = domiporta.get_url_query(self.search_form,page=page)
        return generate_url(scheme=self.scheme, netloc=self.domain, path=path, query=query)
    
    def parse_floor(self, features_list):
        if self.search_form["property_type"] != "flat":
            return None
        try:
            floor_str=next(filter(lambda _: "Piętro" in _.text,features_list),None).find("span",{"class":"features__item_value"}).text
            if floor_str in ['parter','Parter']:
                return 0
            else:
                return int(floor_str)
        except:
            return None
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
    
    def parse_number_of_rooms(self, features_list):
        if self.search_form["property_type"] != "flat":
            return None
        try:
            f=int(next(filter(lambda _: "Liczba pokoi" in _.text,features_list),None).find("span",{"class":"features__item_value"}).text)
        except:
            f=None
        return f
 

    def parse_type_of_building(self,features_list):
        if self.search_form["property_type"] != "flat":
            return None
        type_of_building=next(filter(lambda _: "Typ budynku" in _.text,features_list),None).find("span",{"class":"features__item_value"}).text
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


    def parse_type_of_plot(self,features_list):
        if self.search_form["property_type"] != "plot":
            return None
        type=next(filter(lambda _: "Rodzaj działki" in _.text,features_list),None).find("span",{"class":"features__item_value"}).text
        if type == "budowlana":
            return Property.TypesOfPlots.BUILDING.value
        elif type == "rolna":
            return Property.TypesOfPlots.AGRICULTURAL.value
        elif type == "rekreacyjna":
            return Property.TypesOfPlots.RECREATIONAL.value
        elif type == "leśna":
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
    