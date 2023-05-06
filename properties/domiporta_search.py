import math
from properties import domiporta
from properties.search import Search, SearchResult
from playwright.sync_api import sync_playwright
from properties.utils import generate_url



class DomiportaSearch(Search):
    service_label = 'domiporta'
    url_netloc = "www.domiporta.pl"
    results_per_page=36
    num_pages=1

    # @property
    def get_url_path(self):
        return domiporta.get_url_path(self.search_params)

    
    def search(self):
        """
        attrs - dict with filter criteria
        get page content using requests library and parse it using BeautifulSoup
        function requests search results
        """
        current_page=1
        ret=True
        self.first_page=True
        while current_page <= self.num_pages:
            result = self.search_single_page(current_page)
            if not result:
                ret=False
            current_page = current_page+1
            self.first_page=False
        return ret

    # def get_page_html(self):
    #     with sync_playwright() as playwright:
    #         browser = playwright.chromium.launch()
    #         page = browser.new_page()
    #         page.goto(self.request_url)
    #         page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
    #         return page.content()

    def get_request_single_result_url(self):
        return self.generate_url(scheme=self.url_scheme, netloc=self.url_netloc, path=self.url_path)

    def get_request_params(self, page):
        try:
            request_params=domiporta.get_url_query(self.search_params,page=page,limit=self.results_per_page)
        except Exception as err:
            print(err)
            request_params=False
        print('request_params', request_params)
        return request_params

    def parse_results(self, soup):
        if self.first_page:
            results_count=domiporta.get_results_count(soup)
            self.num_pages = math.ceil(results_count/self.results_per_page)#to da się wyciągnąć parsując stronę
        offers_html = domiporta.get_results_set(soup)
        results_arr = []
        for single_result_soup in offers_html:
            search_result = SearchResult()
            # search_result.offer_url_path = offer['href']
            search_result.offer_url = domiporta.get_single_search_result_url(single_result_soup)
            search_result.main_image_url = domiporta.get_single_search_result_image_url(single_result_soup)
            search_result.title = domiporta.get_single_search_result_title(single_result_soup)
            search_result.price = domiporta.get_single_search_result_price(single_result_soup)
            # search_result.price_per_square_meter = additional_features_set[1].text
            additional_features_set = domiporta.get_single_search_result_additional_features_set(single_result_soup)
            if additional_features_set:
                search_result.number_of_rooms = domiporta.get_single_search_result_number_of_rooms(additional_features_set)
                search_result.area = domiporta.get_single_search_result_area(additional_features_set)
            search_result.service =  self.service_label

            results_arr.append(search_result)
        
        self.results_count=len(results_arr)
        return results_arr
