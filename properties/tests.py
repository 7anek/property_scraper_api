from django.test import TestCase
# from properties.models import Property
from properties.forms import SearchForm
from django.db import connections
from django.db.utils import OperationalError
import properties.search as search
from properties import otodom,olx


# Create your tests here.
# class SearchTestCase(TestCase):

#     @classmethod
#     def setUpTestData(cls):
#         #the testing framework will automatically call once for this class
#         #setUpTestData - jest elementem django i robi rollback w przypadku niepowodzenia
#         cls.search_criteria = {'localization': 'Grodzisk Mazowiecki', 'price_min': 300000, 'price_max': 400000, 'area_min': None, 'area_max': None, 'property_type': 'flat', 'offer_type': 'sell', 'plot_type': '', 'house_type': '', 'flat_type': '', 'year_of_construction_from': None, 'year_of_construction_to': None}#zakładam że na takie kryteria wyszukiwania będe dostawał wyniki
#         cls.search_results = search.webpages_search(cls.search_criteria)
#         print("setUpClass")

#     def setUp(self):
#         #the testing framework will automatically call for every single test we run
#         pass

#     def test_not_empty_results_list(self):
#         self.assertEqual(bool(self.search_results), True, "Results List is empty")
# #otodom tests
#     def test_otodom_correct_results_count(self):
#         otodom = self.search_results.service[search.ServiceNames.otodom]
#         self.assertEqual(otodom.results_count, len(otodom.results), "Otodom Results List count differs from source results count")
# #czy url_path,get_request_params się dobże ustawia
# #end otodom tests    
#     def test_correct_results_count(self):
#         self.assertEqual(self.search_results.results_total, len(self.search_results.objects), "Results List count differs from source results count")

#     def test_attributes_empty(self):
#         self.assertEqual(bool(self.search_results.objects[0].price), True, "Offer attributes are empty")

class OtodomTestCase(TestCase): 

    @classmethod
    def setUpTestData(cls):
        search_params={'localization': 'Grodzisk Mazowiecki', 'price_min': 300000, 'price_max': 400000, 'area_min': None, 'area_max': None, 'property_type': 'flat', 'offer_type': 'sell', 'plot_type': '', 'house_type': '', 'flat_type': '', 'year_of_construction_from': None, 'year_of_construction_to': None}    
        cls.search_params=search.dict_filter_none(search_params)

    def test_url_path(self):
        self.assertEqual(otodom.get_url_path(self.search_params),'pl/oferty/sprzedaz/mieszkanie/grodzisk-mazowiecki')
    
    def test_request_params(self):
        self.assertEqual(otodom.url_query(self.search_params),{'distanceRadius': 0, 'market': 'ALL', 'viewType': 'listing', 'lang': 'pl', 'searchingCriteria': 'sprzedaz', 'priceMin': 300000, 'priceMax': 400000})

class OlxTestCase(TestCase): 

    @classmethod
    def setUpTestData(cls):
        search_params={'localization': 'Grodzisk Mazowiecki', 'price_min': 300000, 'price_max': 400000, 'area_min': None, 'area_max': None, 'property_type': 'flat', 'offer_type': 'sell', 'plot_type': '', 'house_type': '', 'flat_type': '', 'year_of_construction_from': None, 'year_of_construction_to': None}    
        cls.search_params=search.dict_filter_none(search_params)

    def test_url_path(self):
        self.assertEqual(olx.get_url_path(self.search_params),'/d/nieruchomosci/mieszkania/sprzedaz/grodzisk-mazowiecki')
    
    def test_request_params(self):
        self.assertEqual(olx.get_request_params(self.search_params),{'page': 1, 'search[filter_float_price:from]': 300000, 'search[filter_float_price:to]': 400000})

class SearchOlxFromFileTestCase(TestCase):
    
    # @classmethod
    # def setUpTestData(cls):
    #     response_file_path="test_data/olx-search.html"
    #     with open(response_file_path,"r") as file:
    #         response_html=file.read()

    def test_parse_search(self):
        search_params={'localization': 'Grodzisk Mazowiecki', 'price_min': 300000, 'price_max': 400000, 'area_min': None, 'area_max': None, 'property_type': 'flat', 'offer_type': 'sell', 'plot_type': '', 'house_type': '', 'flat_type': '', 'year_of_construction_from': None, 'year_of_construction_to': None}
        search_params=search.dict_filter_none(search_params)
        olx =  search.OlxSearch(search_params,from_file="test_data/olx-search.html")
        olx_result = olx.search()
        self.assertEqual(olx.request_url,'https://www.olx.pl/d/nieruchomosci/mieszkania/sprzedaz/grodzisk-mazowiecki?page=1&search%5Bfilter_float_price%3Afrom%5D=300000&search%5Bfilter_float_price%3Ato%5D=400000')
        self.assertEqual(olx_result,True)


#wyszukiwanie bez np lokalizacji - powinno błąd żucić

# #testy modelu
class ModelTestCase(TestCase):
    def test_database_connection_is_working(self):
        db_conn=connections['default']
        try:
            c=db_conn.cursor()
        except OperationalError:
            connected=False
        else:
            connected=True
        self.assertEqual(connected, True)
