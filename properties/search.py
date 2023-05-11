# import mechanicalsoup
import requests
# import pyppeteer
# from requests_html import HTMLSession, AsyncHTMLSession
from bs4 import BeautifulSoup
# modół abc - służy do tworzenia klas i metod abstarakcyjnych
from abc import ABC, abstractmethod
from properties.utils import *
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


class ServiceNames:
    otodom='otodom'
    olx='olx'
    nieruchomosci_online='nieruchomosci_online'
    gratka='gratka'
    morizon='morizon'
    domiporta='domiporta'

#nieruchomosci_online - blokada adresu ip
services = [ServiceNames.olx, ServiceNames.otodom, ServiceNames.gratka, ServiceNames.morizon, ServiceNames.domiporta]

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


class Search(ABC):
    request_url = None
    request_params = None
    from_file=False
    response = None
    result = []
    base_url = None
    lang = None
    url_scheme = 'http'
    url_netloc = None
    url_path = ''
    url_fragment = ''  # html id elementu
    service_label = ''
    results_count=0#całkowita liczba wyników  ze wszystkich stron z danego serwisu
    page_label="page"

    # @property
    @abstractmethod
    def get_url_path(self):
        pass

    def __init__(self, search_params, from_file=False):
        # search_params = dict_filter_none(search_params)
        # print('search_params', search_params)
        self.search_params = search_params
        self.from_file=from_file

    def add_search_params(self, search_params):
        self.search_params = search_params

    @abstractmethod
    def search(self):
        pass

    def search_single_page(self, page):
        print('search_single_page',page)
        if self.request_params:
            self.request_params[self.page_label]=page
        else:
            self.request_params = self.get_request_params(page)
            if self.request_params == False:
                print('********* error in generating request params', self.request_params)
                return False
        
        if not self.url_path:
            self.url_path=self.get_url_path()

        self.request_url = self.get_request_url()
        if not self.request_url:
            print('********* error in generating request url', self.request_url)
            return False

        print('*********', self.request_url)
        # return False
        if self.from_file:
            self.response = self.get_page_html_from_file()
        else:
            self.response = self.get_page_html()
        if not self.response:
            print('****** Something whent wrong')
            return False

        # self.save_to_file("test_data/olx-search.html")

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
        print("self.url_path",self.url_path)
        try:
            url=generate_url(
                    scheme=self.url_scheme,
                    netloc=self.url_netloc,
                    path=self.url_path,
                    url='',
                    query=self.request_params,
                    fragment=self.url_fragment
            )
        except Exception as err:
            print(err)
            url=False
        return url

    def get_page_html(self):
        if self.from_file:
            return self.get_page_html_from_file()
        response = requests.get(self.request_url)
        if not response.ok:
            print('****** Status code diffrent than 200')
            return False

        if not response.content:
            print('****** Search response content is empty')
            return False
        return response.content

    def get_page_html_from_file(self):
        with open(self.from_file,"r") as file:
            content = file.read()
        if content:
            return content
        else:
            print('****** No such file or file empty:',self.from_file)
            return False


    def save_to_file(self, path):
        with open(path, "w") as file:
            file.write(self.response)

    def get_service_url(self, path='', url='', query='', fragment=''):
        return generate_url(scheme=self.url_scheme, netloc=self.url_netloc, path=path, url=url, query=query, fragment=fragment)



  


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








