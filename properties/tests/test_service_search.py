from django.test import TestCase
from properties.nieruchomosci_online_search import NieruchomosciOnlineSearch
from properties.olx_search import OlxSearch
from properties.morizon_search import MorizonSearch
from properties.otodom_search import OtodomSearch
from properties.gratka_search import GratkaSearch
from properties.domiporta_search import DomiportaSearch
from properties.utils import *

class SearchOlxFromFileTestCase(TestCase):
    
    # @classmethod
    # def setUpTestData(cls):
    #     response_file_path="test_data/olx-search.html"
    #     with open(response_file_path,"r") as file:
    #         response_html=file.read()

    def test_parse_search(self):
        search_params={'formatted_address': 'Grodzisk Mazowiecki, Polska', 'province': 'Mazowieckie', 'city': 'Grodzisk Mazowiecki', 'price_min': 300000, 'price_max': 400000, 'property_type': 'flat', 'offer_type': 'sell'}
        olx =  OlxSearch(search_params,from_file="test_data/olx/olx-search.html")
        olx_result = olx.search()
        self.assertEqual(olx.request_url,'http://www.olx.pl/d/nieruchomosci/mieszkania/sprzedaz/grodzisk-mazowiecki?page=1&search%5Bfilter_float_price%3Afrom%5D=300000&search%5Bfilter_float_price%3Ato%5D=400000')
        self.assertEqual(len(olx.result),6)
        # self.assertEqual(olx.result[0].price,345000.0)
        self.assertEqual(olx.result[0].title,"Mieszkanie 34,8m2 Grodzisk Mazowiecki os. Bairda")
        # self.assertEqual(olx.result[0].area,34.5)

    # class SearchNieruchomosciOnlineFromFileTestCase(TestCase):
class SearchFromFileTestCase(TestCase):
    search_params={'formatted_address': 'Grodzisk Mazowiecki, Polska', 'province': 'Mazowieckie', 'city': 'Grodzisk Mazowiecki', 'price_min': 300000, 'price_max': 400000, 'property_type': 'flat', 'offer_type': 'sell'}

    # def test_nieruchomosci_online_parse_search(self):
    #     s = NieruchomosciOnlineSearch(self.search_params,from_file="test_data/nieruchomosci-online/nieruchomosci-online-search.html")
    #     s_result = s.search()
    #     self.assertEqual(s.request_url,'http://nieruchomosci-online.pl/szukaj.html?%2Cmieszkanie%2Csprzedaz%2C%2CGrodzisk+Mazowiecki%2C%2C%2C%2C300000-400000%2C%2C%2C%2C%2C%2C%2C%2C%2C%2C%2C%2C%2C%2C%2C%2C%2C%2C%2C%2C%2C%2C=&page=1')
    #     self.assertEqual(s_result,True)

    def test_morizon_parse_search(self):
        s = MorizonSearch(self.search_params,from_file="test_data/morizon/morizon-search.html")
        s_result = s.search()
        self.assertEqual(s.request_url,'http://www.morizon.pl/mieszkania/grodzisk-mazowiecki/?page=1&ps%5Bprice_from%5D=300000&ps%5Bprice_to%5D=400000')
        self.assertEqual(s_result,True)
        self.assertEqual(len(s.result), 29)

    def test_otodom_parse_search(self):
        s = OtodomSearch(self.search_params,from_file="test_data/otodom/otodom-search4.html")
        s_result = s.search()
        self.assertEqual(s.request_url,'http://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/grodzisk-mazowiecki?distanceRadius=0&market=ALL&viewType=listing&lang=pl&searchingCriteria=sprzedaz&page=2&limit=24&priceMin=300000&priceMax=400000')
        self.assertEqual(s_result,True)
        self.assertEqual(len(s.result), 48)

    def test_gratka_parse_search(self):
        s = GratkaSearch(self.search_params,from_file="test_data/gratka/gratka-search.html")
        s_result = s.search()
        self.assertEqual(s.request_url,'http://gratka.pl/nieruchomosci/mieszkania/grodzisk-mazowiecki?page=1&cena-calkowita%3Amin=300000&cena-calkowita%3Amax=400000')
        self.assertEqual(s_result,True)
        self.assertEqual(len(s.result), 31)

    def test_domiporta_parse_search(self):
        s = DomiportaSearch(self.search_params,from_file="test_data/domiporta/domiporta-search.html")
        s_result = s.search()
        self.assertEqual(s.request_url,'http://www.domiporta.pl/mieszkanie/sprzedam/mazowieckie/grodzisk-mazowiecki?PageNumber=1&Price.From=300000&Price.To=400000')
        self.assertEqual(s_result,True)
        self.assertEqual(len(s.result), 6)