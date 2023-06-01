from properties.domiporta_search import DomiportaSearch
from properties.morizon_search import MorizonSearch
from properties.olx_search import OlxSearch
from properties.otodom_search import OtodomSearch
from properties.gratka_search import GratkaSearch
from properties.nieruchomosci_online_search import NieruchomosciOnlineSearch
from properties.search import SearchResult, ServiceNames
from properties.utils import dict_filter_none




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
        
        self.add(otodom.result)
        self.results_total += otodom.results_count
        self.service[ServiceNames.otodom]=otodom

        if self.olx_localization_condition(search_params):
            print('olx conditions satisfied')
            olx =  OlxSearch(search_params)
            olx_result = olx.search()
            if olx_result != True:
                print('******* Error in searching olx')
            self.add(olx.result)
            self.results_total += olx.results_count
            self.service[ServiceNames.olx]=olx
        else:
            print('olx conditions not satisfied')


        if 'province' not in search_params and 'street' not in search_params:
            no =  NieruchomosciOnlineSearch(search_params)
            no_result = no.search()
            if no_result != True:
                print('******* Error in searching nieruchomosci-online')
            self.add(no.result)
            self.results_total += no.results_count
            self.service[ServiceNames.nieruchomosci_online]=no

        gratka = GratkaSearch(search_params)
        gratka_result = gratka.search()
        if gratka_result != True:
            print('******* Error in searching gratka')
        self.add(gratka.result)
        self.results_total += gratka.results_count
        self.service[ServiceNames.gratka]=gratka


        domiporta = DomiportaSearch(search_params)
        domiporta_result = domiporta.search()
        if domiporta_result != True:
            print('******* Error in searching domiporta')
        self.add(domiporta.result)
        self.results_total += domiporta.results_count
        self.service[ServiceNames.domiporta]=domiporta


        morizon = MorizonSearch(search_params)
        morizon_result = morizon.search()
        if morizon_result != True:
            print('******* Error in searching morizon')
        self.add(morizon.result)
        self.results_total += morizon.results_count
        self.service[ServiceNames.morizon]=morizon

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
    
    def olx_localization_condition(self, search_params):
        return not ('province' in search_params and 'city' not in search_params and 'district' not in search_params and 'district_neighbourhood' not in search_params and 'street' not in search_params ) and 'district_neighbourhood' not in search_params and 'street' not in search_params