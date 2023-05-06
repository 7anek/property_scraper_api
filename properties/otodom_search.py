import math
from properties import otodom
from properties.search import Search
from properties.search import SearchResult
from playwright.sync_api import sync_playwright
from properties.utils import generate_url
from properties.utils import *


class OtodomSearch(Search):
    service_label = 'otodom'
    url_netloc = "www.otodom.pl"
    lang = 'pl'
    results_per_page=24
    num_pages=1

    # @property
    def get_url_path(self):
        return otodom.get_url_path(self.search_params)

    
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

    def get_page_html(self):
        
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            page = browser.new_page()
            if self.first_page and "street" in self.search_params:
                print('**********wyklikuje wyszukiwanie')
                page.goto(self.request_url)
                page.wait_for_selector('#onetrust-accept-btn-handler')
                page.click('#onetrust-accept-btn-handler')

                btn_id_location=page.locator("#location")
                btn_id_location.click()
                page.wait_for_selector('ul[data-testid="selected-locations"]')
                selected_locations_list=page.locator('ul[data-testid="selected-locations"]')
                if selected_locations_list.is_visible():
                    selected_locations_list.locator('li').all()[1].click()

                location_input=page.locator("#location-picker-input")
                location_input.fill(self.search_params["formatted_address"])
                page.locator("ul.css-1tsmnl6").locator("li:first-child").click()
                page.locator("#search-form-submit").click()
                #musze dodać id ulicy do request paramsów
                # if "street" in self.search_params:
                self.request_params=url_to_params_dict(page.url())
            else:
                print('**********robie wyszukiwanie z url')
                page.goto(self.request_url)

            page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
            return page.content()

    def get_request_single_result_url(self):
        return self.generate_url(scheme=self.url_scheme, netloc=self.url_netloc, path=self.url_path)

    def get_request_params(self, page):
        # if self.request_params:
        #     self.request_params
        try:
            request_params=otodom.url_query(self.search_params,page=page,limit=self.results_per_page)
        except Exception as err:
            print(err)
            request_params=False
        print('request_params', request_params)
        return request_params

    def parse_results(self, soup):
        if self.first_page: 
            results_count=int(soup.find("span", {"class": "e17mqyjp2"}).text)
            print('***********results_count:',results_count)
            self.num_pages = math.ceil(results_count/self.results_per_page)
            print('***********self.num_pages:',self.num_pages)
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
        self.results_count=len(results_arr)
        return results_arr
        # return ''.join(soup.find_all('a', {"data-cy": "listing-item-link"}))
        # browser = mechanicalsoup.Browser()
        # url = "http://olympus.realpython.org/login"
        # page = browser.get(url)
        # return page.content