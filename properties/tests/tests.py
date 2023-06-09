from django.test import TestCase
# from properties.models import Property
from properties.forms import SearchForm
from django.db import connections
from django.db.utils import OperationalError
from properties.nieruchomosci_online_search import NieruchomosciOnlineSearch
from properties.olx_search import OlxSearch
import properties.search as search
from properties.utils import *
from properties import gratka, otodom,olx,nieruchomosci_online


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
class UtilsTestCase(TestCase): 

    def test_dict_filter_none(self):
        d={'localization': 'Grodzisk Mazowiecki', 'price_min': 300000, 'price_max': 400000, 'area_min': None, 'area_max': None, 'property_type': 'flat', 'offer_type': 'sell', 'plot_type': '', 'house_type': '', 'flat_type': '', 'year_of_construction_from': None, 'year_of_construction_to': None} 
        self.assertEqual(dict_filter_none(d),{'localization': 'Grodzisk Mazowiecki', 'price_min': 300000, 'price_max': 400000, 'property_type': 'flat', 'offer_type': 'sell'})
    


