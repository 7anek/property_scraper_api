from django.test import TestCase
from properties.nieruchomosci_online_search import NieruchomosciOnlineSearch
from properties.olx_search import OlxSearch
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

class SearchNieruchomosciOnlineFromFileTestCase(TestCase):
    
    def test_parse_search(self):
        search_params={'formatted_address': 'Grodzisk Mazowiecki, Polska', 'province': 'Mazowieckie', 'city': 'Grodzisk Mazowiecki', 'price_min': 300000, 'price_max': 400000, 'property_type': 'flat', 'offer_type': 'sell'}
        s = NieruchomosciOnlineSearch(search_params,from_file="test_data/nieruchomosci-online/nieruchomosci-online-search.html")
        s_result = s.search()
        self.assertEqual(s.request_url,'http://nieruchomosci-online.pl/szukaj.html?%2Cmieszkanie%2Csprzedaz%2C%2CGrodzisk+Mazowiecki%2C%2C%2C%2C300000-400000%2C%2C%2C%2C%2C%2C%2C%2C%2C%2C%2C%2C%2C%2C%2C%2C%2C%2C%2C%2C%2C%2C=&page=1')
        self.assertEqual(s_result,True)
