# import mechanicalsoup
import requests
import asyncio
# import pyppeteer
# from requests_html import HTMLSession, AsyncHTMLSession
from bs4 import BeautifulSoup
# modół abc - służy do tworzenia klas i metod abstarakcyjnych
from abc import ABC, abstractmethod
from urllib.parse import urljoin, urlencode, urlparse, urlunparse, unquote
from collections import namedtuple
from properties.utils import *
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import math
from playwright.sync_api import sync_playwright

class ServiceNames:
    otodom='otodom'
    olx='olx'

services = [ServiceNames.olx, ServiceNames.otodom]


def webpages_search(attrs):
    search_results = SearchResults(attrs)
    return search_results

def get_single_offer(attrs):
    result = None
    if attrs['service'] == ServiceNames.otodom:
        print('service otodom')
        otodom = SearchSingleOtodom(attrs)
        result = otodom.get_result()
    elif attrs['service'] == ServiceNames.olx:
        print('service otodom')
        olx = SearchSingleOlx(attrs)
        result = olx.get_result()
    else:
        print('Unknown service:', attrs['service'])
        return False
 
    return result


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

class Offer:
    title = ''
    price = ''
    price_per_square_meter = ''
    localization = ''
    description = ''
    service_id = None


class SearchResults:
    objects = []
    search_params = None
    results_total = 0#ile wyników znajduje się na stronach (nie ile faktycznie pobrano)
    service = {}

    def __init__(self, search_params):
        self.objects=[]
        self.results_total=0
        # print('*************** SearchResults __init__ count', len(self.objects))
        search_params = dict_filter_none(search_params)
        # print('search_params', search_params)
        self.search_params = search_params
        otodom = OtodomSearch(search_params)
        otodom_result = otodom.search()
        if otodom_result != True:
            print('******* Error in searching otodom')
        # print('*************** otodom first url', otodom.result[0].offer_url)
        # print('*************** otodom count', len(otodom.result))
        self.add(otodom.result)
        self.results_total += otodom.results_count
        self.service[ServiceNames.otodom]=otodom
        # olx =  OlxSearch(search_params)
        # olx_result = olx.search()
        # if olx_result != True:
        #     print('******* Error in searching olx')
        # self.add(olx.result)
        # print('*************** SearchResults first url', self.objects[0].offer_url)
        # print('*************** SearchResults last url', self.objects[-1].offer_url)
        # print('*************** SearchResults count', len(self.objects))

    def add(self, search_result):
        if type(search_result) is list:
            self.objects[len(self.objects):] = search_result
        elif type(search_result) is SearchResult:
            self.objects.append(search_result)
        else:
            return False
        return True


class Search(ABC):
    request_url = None
    request_params = None
    response = None
    result = []
    base_url = None
    lang = None
    url_scheme = 'https'
    url_netloc = None
    url_path = ''
    url_fragment = ''  # html id elementu
    service_label = ''
    results_count=0#całkowita liczba wyników  ze wszystkich stron z danego serwisu
    results_per_page=24
    num_pages=1

    @property
    @abstractmethod
    def url_path(self):
        pass

    def __init__(self, search_params):
        # search_params = dict_filter_none(search_params)
        # print('search_params', search_params)
        self.search_params = search_params

    def add_search_params(self, search_params):
        self.search_params = search_params

    def search(self):
        """
        attrs - dict with filter criteria
        get page content using requests library and parse it using BeautifulSoup
        function requests search results
        """
        current_page=1
        ret=True
        while current_page <= self.num_pages:
            result = self.search_single_page(current_page)
            if not result:
                ret=False
            current_page = current_page+1
        return ret

    def search_single_page(self, page):
        self.request_params = self.get_request_params(page)
        self.request_url = self.get_request_url()

        # print('*********', self.request_url)
        # return False
        self.response = self.get_page_html()
        if not self.response:
            print('****** Something whent wrong')
            return False

        soup = BeautifulSoup(self.response, 'html.parser')

        result = self.parse_results(soup)

        if not result:
            return False

        self.result = self.result + result
        return True

    

    # @abstractmethod
    # def get_request_url(self):
    #     pass

    @abstractmethod
    def get_request_params(self, page):
        pass

    @abstractmethod
    def parse_results(self):
        pass



    @abstractmethod
    def get_request_single_result_url(self):
        pass

    def get_request_url(self):
        return generate_url(
                scheme=self.url_scheme,
                netloc=self.url_netloc,
                path=self.url_path,
                url='',
                query=self.request_params,
                fragment=self.url_fragment
        )

    def get_page_html(self):
        response = requests.get(self.request_url)
        if not response.ok:
            print('****** Status code diffrent than 200')
            return False

        if not response.content:
            print('****** Search response content is empty')
            return False
        return response.content

    def lowercase_with_hyphen_str(self, str):
        return '-'.join(str.lower().split())

    def save_to_file(self, path):
        with open(path, "w") as file:
            file.write(self.response.text)

    def get_service_url(self, path='', url='', query='', fragment=''):
        return generate_url(scheme=self.url_scheme, netloc=self.url_netloc, path=path, url=url, query=query, fragment=fragment)


class OtodomSearch(Search):
    service_label = 'otodom'
    url_netloc = "www.otodom.pl"
    lang = 'pl'
    offer_type_mapping = {
        'sell': 'sprzedaz',
        'rent': 'wynajem',
        'any': 'wszystko'
    }
    property_type_mapping = {
        'flat': 'mieszkanie',
        'house': 'dom',
        'plot': 'dzialka',
        'garage': 'garaz'
    }

    @property
    def url_path(self):
        url_path = []
        if 'offer_type' in self.search_params:
            url_path.append(self.offer_type_mapping[self.search_params['offer_type']])
        if 'property_type' in self.search_params:
            url_path.append(self.property_type_mapping[self.search_params['property_type']])
        url_path.append(self.lowercase_with_hyphen_str(remove_accents(self.search_params['localization'])))
        return f"{self.lang}/oferty/{'/'.join(url_path)}"

    # def get_request_url(self):
    #     search_loc = self.lowercase_with_hyphen_str(self.search_params['localization'])
    #     return self.base_url+"/"+self.lang+"/oferty/sprzedaz/mieszkanie/"+search_loc
    
    def get_page_html(self):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            page = browser.new_page()
            page.goto(self.request_url)
            page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
            return page.content()

    def get_request_single_result_url(self):
        return self.generate_url(scheme=self.url_scheme, netloc=self.url_netloc, path=self.url_path)

    def get_request_params(self, page):
        request_params = {
            'distanceRadius': 0,
            'market': 'ALL',
            'viewType': 'listing',
            'lang': self.lang,
            'searchingCriteria': self.offer_type_mapping[self.search_params['offer_type']],
            'limit': self.results_per_page,
            'page': page
        }

        if 'price_min' in self.search_params:
            request_params['priceMin'] = self.search_params['price_min']
        if 'price_max' in self.search_params:
            request_params['priceMax'] = self.search_params['price_max']
        if 'area_min' in self.search_params:
            request_params['areaMin'] = self.search_params['area_min']
        if 'area_max' in self.search_params:
            request_params['areaMax'] = self.search_params['area_max']
        # print('request_params', request_params)
        return request_params

    def parse_results(self, soup):
        self.results_count=int(soup.find("span", {"class": "e17mqyjp2"}).text)
        self.num_pages = math.ceil(self.results_count/self.results_per_page)
        results_div = soup.find('div', {"data-cy": "search.listing.organic"})
        offers_html = results_div.find_all('a', {"data-cy": "listing-item-link"})
        results_arr = []
        for offer in offers_html:
            search_result = SearchResult()
            search_result.offer_url_path = offer['href']
            search_result.offer_url = generate_url(
                scheme=self.url_scheme, netloc=self.url_netloc, path=offer['href'])
            search_result.main_image_url = offer.find("img")["src"]
            title_tag = offer.find("h3", {"data-cy": "listing-item-title"})
            search_result.title = title_tag.text
            params_arr = offer.find_all("span", {"class":"css-1ntk0hg"})
            if params_arr:
                search_result.price = params_arr[0].text
                search_result.price_per_square_meter = params_arr[1].text
                search_result.number_of_rooms = params_arr[2].text
                search_result.area = params_arr[3].text
            search_result.service =  self.service_label

            results_arr.append(search_result)

            # print('***** otodom netloc:', self.url_netloc)
            # print('***** otodom url:', search_result.offer_url)
            # print('***** otodom url path:', search_result.offer_url_path)

        return results_arr
        # return ''.join(soup.find_all('a', {"data-cy": "listing-item-link"}))
        # browser = mechanicalsoup.Browser()
        # url = "http://olympus.realpython.org/login"
        # page = browser.get(url)
        # return page.content

  


class OlxSearch(Search):
    service_label = 'olx'
    url_netloc = "www.olx.pl"

    offer_type_mapping = {
        'sell': 'sprzedaz',
        'rent': 'wynajem'
    }
    property_type_mapping = {
        'flat': 'mieszkania',
        'house': 'domy',
        'plot': 'dzialki',
        'garage': 'garaze-parkingi'
    }

    @property
    def url_path(self):
        # search_loc = self.lowercase_with_hyphen_str(self.search_params['localization'])
        url_path = []
        if 'property_type' in self.search_params:
            url_path.append(self.property_type_mapping[self.search_params['property_type']])
        if 'offer_type' in self.search_params:
            url_path.append(self.offer_type_mapping[self.search_params['offer_type']])
        url_path.append(self.lowercase_with_hyphen_str(self.search_params['localization']))
        return f"/d/nieruchomosci/{'/'.join(url_path)}"
    # def get_request_url(self):
    #     search_loc = self.lowercase_with_hyphen_str(self.search_params['localization'])
    #     return self.base_url+"/d/nieruchomosci/mieszkania/sprzedaz/"+search_loc

    def get_request_params(self, page):
        # request_params = DictAutoVivification()
        request_params = {}

        if 'price_min' in self.search_params:
            request_params['search[filter_float_price:from]'] = self.search_params['price_min']
        if 'price_max' in self.search_params:
            request_params['search[filter_float_price:to]'] = self.search_params['price_max']
        if 'area_min' in self.search_params:
            request_params['search[filter_float_m:from]'] = self.search_params['area_min']
        if 'area_max' in self.search_params:
            request_params['search[filter_float_m:to]'] = self.search_params['area_max']

        return request_params

    def parse_results(self, soup):
        # if not soup("div", class_="css-pband8"):
        #     return False
        
        search_results_soup = soup.find("div", {"data-testid":"listing-grid"}).find_all("a")
        results_arr = []
        for search_result_soup in search_results_soup:
            search_result = SearchResult()
            offer_url = search_result_soup["href"]
            if offer_url.startswith(("https://www.otodom.pl","www.otodom.pl")):#niechcemy ofert z otodom bo pobieramy je w innym miejscu i będą się dublowały
                continue
            elif offer_url.startswith(("https","www")):#oferta z innego serwisu
                search_result.offer_url = offer_url
            else:
                search_result.offer_url = self.get_service_url(path=search_result_soup["href"])
                search_result.offer_url_path = offer_url
            image_url = search_result_soup.find("div", class_="css-gl6djm").find("img")["src"]
            if image_url.startswith(("https","www")):
                search_result.main_image_url = image_url
            elif image_url.startswith(("/app/static/media/")): 
                search_result.main_image_url = self.get_service_url(path=image_url)
            else:
                search_result.main_image_url = ''
            search_result.title = search_result_soup.find("h6").text
            search_result.price = search_result_soup.find(
                "h6").find_next("p").text
            area_text = search_result_soup.find("span", class_="css-643j0o").text
            if "-" in area_text:
                search_result.area, search_result.price_per_square_meter = search_result_soup.find(
                "span", class_="css-643j0o").text.split(" - ")
            else:
                search_result.area = area_text

            search_result.service =  self.service_label
            results_arr.append(search_result)

        return results_arr


    def parse_single_result(self):
        pass


    def get_request_single_result_url(self):
        pass

class SearchSingle:
    view_params = None
    request_url = ''
    service_label = ''
    host = ""
    soup = None

    def __init__(self, params):
        self.view_params = params
        self.request_url = self.get_request_url(params)
        print('request_url', self.request_url)

    def get_result(self):
 
        self.response = requests.get(self.request_url)
        if not self.response.ok:
            print('****** Request was not succesful')
            return False
        print('status code', self.response.status_code)
        # if not self.response.content:
        #     print('****** Search response content is empty')
        #     return False

        self.soup = BeautifulSoup(self.response.text, "html.parser")

        if self.page_404():
            print('--------- Error 404 - page does not exists')
            return False

        self.result = self.parse_result()

        if not self.result:
            return False

        return self.result
    
    def get_request_url(self, params):
        return generate_url(netloc=self.host, path=params['url_path'])

    @abstractmethod
    def page_404(self):
        pass

    @abstractmethod
    def parse_result(self):
        pass

class SearchSingleOtodom(SearchSingle):
    service_label = 'otodom'
    host = "www.otodom.pl"

    def page_404(self):
        return bool(self.soup.find("h4", text="Przepraszamy, ale nie możemy znaleźć takiej strony... Co powiesz na krótką grę w ramach rekompensaty?"))

    def parse_result(self):
        offer = Offer()
        header = self.soup.find("header")
        offer.title = header.h1.text
        offer.price = header.find("strong",{'aria-label':'Cena'}).text
        offer.price_per_square_meter = header.find("div",{'aria-label':'Cena za metr kwadratowy'}).text
        offer.localization = header.find("a").text
        # Szczegóły ogłoszenia
        
        return offer
    
class SearchSingleOlx(SearchSingle):
    service_label = 'olx'
    host = "www.olx.pl"

    def page_404(self):
        return bool(self.soup.find("h4", text="Przepraszamy, ale nie możemy znaleźć takiej strony... Co powiesz na krótką grę w ramach rekompensaty?"))
    
    def get_result(self):
        CHROME_PATH = '/usr/bin/google-chrome'
        CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
        WINDOW_SIZE = "1920,1080"

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        chrome_options.binary_location = CHROME_PATH

        selenium = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                                chrome_options=chrome_options
                                )
        # selenium = webdriver.Chrome()

        selenium.get(self.request_url)
        selenium.implicitly_wait(10)
        onetrust_button = selenium.find_element("id","onetrust-accept-btn-handler")
        onetrust_button.click()
        # ActionChains(selenium).click(onetrust_button).perform()
        self.soup = BeautifulSoup(selenium.page_source, 'html.parser')

        if self.page_404():
            print('--------- Error 404 - page does not exists')
            return False

        self.result = self.parse_result()

        if not self.result:
            return False

        return self.result

    def parse_result(self):
        offer = Offer()
        offer.title = self.soup.find('h1', {"data-cy":"ad_title"}).text
        offer.price = self.soup.find('div', {"data-testid":"ad-price-container"}).h3.text
         # Szczegóły ogłoszenia
        attributes_raw = self.soup.find("div", {"id":"baxter-above-parameters"}).next_element.next_element.next_element.find_all("p")
        attributes_raw = list(map(lambda x: x.text, attributes_raw))
        attributes_dict = dict(map(lambda x: map(str.strip, x.split(":")),filter(lambda y: ":" in y, attributes_raw)))
        # {'Cena za m²': '9972.22 zł/m²', 'Poziom': '3', 'Umeblowane': 'Tak', 'Rynek': 'Wtórny', 'Rodzaj zabudowy': 'Blok', 'Powierzchnia': '36 m²', 'Liczba pokoi': '2 pokoje'}
        offer.description = self.soup.find("div",{"data-cy":"ad_description"}).div.text
        offer.localization = self.soup.find("p", class_="css-1cju8pu").text
        # offer.price_per_square_meter = attributes_dict["'Cena za m²"]
        # offer.localization = "".join(self.soup.find("p",string="Lokalizacja").find_next("div").section.div.div.find_all("p"))
        offer.service_id = self.soup.find("div", {"data-cy":"ad-footer-bar-section"}).span.text
        
        return offer








