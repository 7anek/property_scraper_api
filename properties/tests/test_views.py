import requests_mock
from scrapy.http import HtmlResponse

from properties.models import Property
from django.test import TestCase, Client
from django.urls import reverse
from requests_mock import Mocker
from unittest.mock import patch
from properties.forms import SearchForm
import json
import re
from scraper.utils import *
from selenium.webdriver.common.by import By
from django.conf import settings
from selenium import webdriver
from scraper.spiders.gratka_spider import GratkaSpider
from django.test import LiveServerTestCase
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from django.test.client import RequestFactory


class ScrapeSeleniumTestCase(LiveServerTestCase):
    def setUp(self):
        self.old_debug = settings.DEBUG
        settings.DEBUG = True

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        webdriver_service = Service('chromedriver')
        self.driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
        self.driver.set_window_size(1280, 1024)
        # self.driver = webdriver.Chrome('chromedriver')



    def tearDown(self):
        self.driver.quit()
        settings.DEBUG = self.old_debug

    def test_search_with_google_maps_suggestion(self):
        self.driver.get(f"{self.live_server_url}/properties/search/")

        # Znajdź pole adresu i wpisz "Jaktorów"
        address_input = self.driver.find_element(By.ID,'id_address')
        address_input.clear()
        address_input.send_keys('Jaktorów')

        # Poczekaj na pojawienie się sugestii z Google Maps
        self.driver.implicitly_wait(1)

        # Wybierz pierwszą sugestię z Google Maps
        suggestions = self.driver.find_elements(By.CLASS_NAME, 'pac-item')
        suggestions[0].click()

        # Sprawdź, czy wartość pola adresu została ustawiona na wybraną sugestię
        self.assertEqual(address_input.get_attribute('value'), 'Jaktorów, Polska')

        # Znajdź przycisk submit i kliknij go
        # Ten kod spowoduje wyszukiwanie po tych serwisach, trzeba by najpierw dać mockowanie żeby zrobić to bezpiecznie
        # submit_button = self.driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        # submit_button.click()

    def handle_form(self):
        # Wypełnij pozostałe pola formularza
        self.driver.find_element(By.ID, 'id_address').clear()
        self.driver.find_element(By.ID, 'id_province').clear()
        self.driver.find_element(By.ID, 'id_city').clear()
        self.driver.find_element(By.ID, 'id_district').clear()
        self.driver.find_element(By.ID, 'id_district_neighbourhood').clear()
        self.driver.find_element(By.ID, 'id_street').clear()
        self.driver.find_element(By.ID, 'id_price_min').clear()
        self.driver.find_element(By.ID, 'id_price_max').clear()
        self.driver.find_element(By.ID, 'id_area_min').clear()
        self.driver.find_element(By.ID, 'id_area_max').clear()
        self.driver.find_element(By.ID, 'id_build_year_from').clear()
        self.driver.find_element(By.ID, 'id_build_year_to').clear()

        self.driver.find_element(By.ID, 'id_address').send_keys('Grodzisk Mazowiecki, Polska')
        self.driver.find_element(By.ID, 'id_province').send_keys('Mazowieckie')
        self.driver.find_element(By.ID, 'id_city').send_keys('Grodzisk Mazowiecki')
        self.driver.find_element(By.ID, 'id_price_min').send_keys('300000')
        self.driver.find_element(By.ID, 'id_price_max').send_keys('400000')
        # self.driver.find_element(By.ID, 'id_property_type').send_keys('flat')
        # self.driver.find_element(By.ID, 'id_offer_type').send_keys('sell')

        # Wyślij formularz
        # time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, 'form input[type="submit"]').click()

    @requests_mock.Mocker()
    def test_search(self, mocker):
        """morizon, otodom, gratka używają playwright - na tym nieda się tak łatwo mokować - można tylko tak:
        https://thompson-jonm.medium.com/intercepting-network-requests-with-python-and-playwright-7f621ad3935b
        browser = playwright.chromium.launch()
        page = browser.new_page()
        page.route('**', lambda route, request: route.fulfill(status=200, body=self.request_url))
        page.goto(self.request_url)
        co zwracało by to co jest w pliku nietylko podczas testowania ale i podczas normalnego działąnia więc zamieniam metodę get_page_html w tych serwisach żeby zwracała docelowy plik
        """
        # mocker.get(re.compile('.*otodom.pl/pl/oferty/sprzedaz/.+'), text=open("test_data/otodom/otodom-search.html", "r").read(), )
        mocker.get(re.compile('.*olx.pl/d/nieruchomosci/.+'), text=open("test_data/olx/olx-search.html", "r").read(), )
        # mocker.get(re.compile('.*morizon.pl/.+'), text=open("test_data/morizon/morizon-search.html", "r").read(), )
        mocker.get(re.compile('.*domiporta.pl/.+'),
                   text=open("test_data/domiporta/domiporta-search.html", "r").read(), )
        # mocker.get(re.compile('.*gratka.pl/nieruchomosci/.+'), text=open("test_data/gratka/gratka-search.html", "r").read(), )

        # Przygotowanie pliku HTML z odpowiedzią z serwisu Morizon
        morizon_mock_response_path = 'test_data/morizon/morizon-search.html'
        with open(morizon_mock_response_path, 'r') as file:
            morizon_mock_response_html = file.read()

        # Przygotowanie pliku HTML z odpowiedzią z serwisu Gratka
        gratka_mock_response_path = 'test_data/gratka/gratka-search.html'
        with open(gratka_mock_response_path, 'r') as file:
            gratka_mock_response_html = file.read()

        # Przygotowanie pliku HTML z odpowiedzią z serwisu Otodom
        otodom_mock_response_path = 'test_data/otodom/otodom-search5.html'
        with open(otodom_mock_response_path, 'r') as file:
            otodom_mock_response_html = file.read()

        with patch('properties.morizon_search.MorizonSearch.get_page_html') as mock_morizon_get_page_html, \
                patch('properties.gratka_search.GratkaSearch.get_page_html') as mock_gratka_get_page_html, \
                patch('properties.otodom_search.OtodomSearch.get_page_html') as mock_otodom_get_page_html:
            mock_morizon_get_page_html.return_value = morizon_mock_response_html
            mock_gratka_get_page_html.return_value = gratka_mock_response_html
            mock_otodom_get_page_html.return_value = otodom_mock_response_html

            self.driver.get(f"{self.live_server_url}/properties/search/")

            # address_input = self.driver.find_element(By.ID, 'id_address')
            # address_input.send_keys('Grodzisk Mazowiecki')
            # time.sleep(1)  # Poczekaj na pojawienie się sugestii

            # Wybierz pierwszą sugestię
            # try:
            #     autocomplete_suggestion = self.driver.find_element(By.CSS_SELECTOR, '.pac-container .pac-item:first-child')
            #     ActionChains(self.driver).move_to_element(autocomplete_suggestion).click().perform()
            # except NoSuchElementException:
            #
            #     self.fail("Nie znaleziono sugestii adresu.")

            self.handle_form()
            self.driver.save_screenshot('test_data/test_search3.png')
            # Poczekaj na załadowanie strony wynikowej
            # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.search-results')))

            # Sprawdź oczekiwany wynik

            # Przykład sprawdzenia wyniku: Sprawdź, czy na stronie wynikowej wyświetla się lista ofert
            search_results = self.driver.find_elements(By.CSS_SELECTOR, '.search-results .result-item')
            self.assertGreater(len(search_results), 0)
            self.assertEqual(len(search_results), 29 + 6 + 31 + 6 + 2 * 24)
            # morizon 29
            # domiporta 6
            # gratka 31
            # olx 6
            # otodom 2*24
            self.addCleanup(self.driver.quit)


    # def test_scrape_integration(self):
    #     """
    #     ten typ testu zmodyfikuje bazę normalną, nie testową przy przejściu przez niezmockowany scrapy pipeline
    #     musi być odpoalone scrapyd żeby test przeszedł
    #     """
    #     self.driver.get(f"{self.live_server_url}/properties/scrape/")
    #     print('test_scrape_integration start Property.objects.all().count()', Property.objects.all().count())
    #     self.handle_form()
    #     self.driver.save_screenshot('test_data/test_scrape_integration.png')
    #     # Poczekaj na załadowanie strony wynikowej
    #     # try:
    #     #     WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.scrapy-results')))
    #     # except:
    #     #     pass
    #     time.sleep(10)
    #     print('test_scrape_integration end Property.objects.all().count()', Property.objects.all().count())
    #     self.assertGreater(len(Property.objects.all()), 0)
    def test_scrape_view(self):
        # Test widoku scrape
        # Użyj biblioteki Selenium do wypełnienia formularza i wysłania żądania
        # Sprawdź oczekiwane rezultaty

        print(';;;;;;;;;;;;;;;;;;;; DEBUG',settings.DEBUG)
        # Zmockowanie metody create_spider w ScrapyFactory
        with patch('scraper.scrapy_factory.ScrapydSpiderFactory.__init__') as mock_init, \
             patch('scraper.scrapy_factory.ScrapydSpiderFactory.create_spiders') as mock_create_spider, \
             patch('scraper.scrapy_factory.ScrapydSpiderFactory.job_ids',["75d6b108cc9811edba0300155d7be260"]), \
             patch('scraper.scrapy_factory.ScrapydSpiderFactory.check_finished') as mock_check_finished:
            # Zmockowanie parse i parse_offer w scrapy spiderze
            # mock_spider = mock_create_spider.return_value
            # mock_spider.parse.return_value = None
            mock_init.return_value = None
            mock_create_spider.return_value = None
            mock_check_finished.return_value = True
            Property.objects.create(scrapyd_job_id="75d6b108cc9811edba0300155d7be260",service_name='test',service_url='www.test.pl',price=350000,area=50,province='Mazowieckie',city='Grodzisk Mazowiecki',property_type='flat', offer_type='sell')

            self.driver.get(f"{self.live_server_url}/properties/scrape/")
            self.handle_form()
            self.driver.save_screenshot('test_data/test_scrape_view.png')
            # time.sleep(10)
            self.assertIn("Finished", self.driver.page_source)
            elements = self.driver.find_elements(By.CLASS_NAME,"scrapy-item")
            self.assertTrue(len(elements) > 0)


#     @requests_mock.Mocker()
#     def test_scrape(self, mocker):
#         """morizon, otodom, gratka używają playwright - na tym nieda się tak łatwo mokować - można tylko tak:
#         https://thompson-jonm.medium.com/intercepting-network-requests-with-python-and-playwright-7f621ad3935b
#         browser = playwright.chromium.launch()
#         page = browser.new_page()
#         page.route('**', lambda route, request: route.fulfill(status=200, body=self.request_url))
#         page.goto(self.request_url)
#         co zwracało by to co jest w pliku nietylko podczas testowania ale i podczas normalnego działąnia więc zamieniam metodę get_page_html w tych serwisach żeby zwracała docelowy plik
#         """
#         mocker.get(re.compile('.*olx.pl/d/nieruchomosci/.+'), text=open("test_data/olx/olx-search.html", "r").read(), )
#         mocker.get(re.compile('.*domiporta.pl/mieszkanie/sprzedam.+'),
#                    text=open("test_data/domiporta/domiporta-search.html", "r").read(), )
#
#         mocker.get(re.compile('.*olx.pl/d/oferta.+'), text=open("test_data/olx/olx-details.html", "r").read(), )
#         mocker.get(re.compile('.*domiporta.pl/nieruchomosci.+'),
#                    text=open("test_data/domiporta/domiporta-details.html", "r").read(), )
#         mocker.get(re.compile('.*otodom.pl/\d.+'),
#                    text=open("test_data/otodom/otodom-details.html", "r").read(), )
#         mocker.get(re.compile('.*gratka.pl/nieruchomosci/mieszkanie.+'),
#                    text=open("test_data/gratka/gratka-details.html", "r").read(), )
#         mocker.get(re.compile('.*morizon.pl/oferta/.+'),
#                    text=open("test_data/morizon/morizon-details.html", "r").read(), )
#
#         # Przygotowanie pliku HTML z odpowiedzią z serwisu Morizon
#         morizon_mock_response_path = 'test_data/morizon/morizon-search.html'
#         with open(morizon_mock_response_path, 'r') as file:
#             morizon_mock_response_html = file.read()
#
#         # Przygotowanie pliku HTML z odpowiedzią z serwisu Gratka
#         gratka_mock_response_path = 'test_data/gratka/gratka-search.html'
#         with open(gratka_mock_response_path, 'r') as file:
#             gratka_mock_response_html = file.read()
#
#         # Przygotowanie pliku HTML z odpowiedzią z serwisu Otodom
#         otodom_mock_response_path = 'test_data/otodom/otodom-search5.html'
#         with open(otodom_mock_response_path, 'r') as file:
#             otodom_mock_response_html = file.read()
#
#         # Przygotowanie pliku HTML z odpowiedzią z serwisu Otodom
#         domiporta_mock_response_path = 'test_data/domiporta/domiporta-search.html'
#         with open(domiporta_mock_response_path, 'r') as file:
#             domiporta_mock_response_html = file.read()
#
#         # with patch('properties.morizon_search.MorizonSearch.get_page_html') as mock_morizon_get_page_html, \
#         #         patch('properties.gratka_search.GratkaSearch.get_page_html') as mock_gratka_get_page_html, \
#         #         patch('properties.otodom_search.OtodomSearch.get_page_html') as mock_otodom_get_page_html:
#         #     mock_morizon_get_page_html.return_value = morizon_mock_response_html
#         #     mock_gratka_get_page_html.return_value = gratka_mock_response_html
#         #     mock_otodom_get_page_html.return_value = otodom_mock_response_html
#
#         # patch('scraper.spiders.domiporta_spider.DomiportaSpider.current_url', f"file://{domiporta_mock_response_path}"), \
#         # patch('scraper.spiders.domiporta_spider.DomiportaSpider.start_urls',[f"file://{domiporta_mock_response_path}"]), \
#             # with patch('scrapyd_api.ScrapydAPI') as mock_scrapyd, \
#
#         with patch('scraper.scrapy_factory.ScrapydSpiderFactory.create_spiders') as mock_create_spider:
#             # Tworzenie instancji zmockowanego scrapy spidera
#             mock_spider = mock_create_spider.return_value
#
#             # Parsowanie pliku HTML i przekazanie go jako odpowiedź do metody parse
#             file_path = "test_data/domiporta/domiporta-search.html"
#             with open(file_path, "r", encoding="utf8") as file:
#                 response = HtmlResponse(url="http://www.domiporta.pl/mieszkanie/sprzedam/mazowieckie/grodzisk-mazowiecki?PageNumber=1&Price.From=300000&Price.To=400000", body=file.read(), encoding="utf-8")
#                 mock_spider.parse(response)
#
#             # Parsowanie pliku HTML i przekazanie go jako odpowiedź do metody parse_offer
#             file_path_offer = "test_data/domiporta/domiporta-details.html"
#             with open(file_path_offer, "r", encoding="utf8") as file_offer:
#                 response_offer = HtmlResponse(url="http://www.domiporta.pl/nieruchomosci/sprzedam-mieszkanie-dwupokojowe-chrzanow-maly-chrzanow-maly-41m2/154218398", body=file_offer.read(), encoding="utf-8")
#                 mock_spider.parse_offer(response_offer)
#
#         # with patch('scraper.spiders.morizon_spider.MorizonSpider.start_requests') as mock_morizon_start_requests, \
#         #         patch('scraper.spiders.domiporta_spider.DomiportaSpider.start_requests') as mock_domiporta_start_requests, \
#         #         patch('scraper.spiders.gratka_spider.GratkaSpider.start_requests') as mock_gratka_start_requests, \
#         #         patch('scraper.spiders.otodom_spider.OtodomSpider.start_requests') as mock_otodom_start_requests:
#             # mock_jobs = [{'id': '1', 'project': 'scraper', 'spider': 'domiporta', 'status': 'finished'},
#             #              {'id': '2', 'project': 'scraper', 'spider': 'domiporta', 'status': 'running'}]
#             # mock_scrapyd.return_value.list_jobs.return_value = mock_jobs  # Mockowanie wartości zwracanej przez ScrapydAPI
#             # mock_scrapyd.return_value.schedule.return_value = '1'
#             # mock_morizon_start_requests.return_value = morizon_mock_response_html
#             # mock_gratka_start_requests.return_value = gratka_mock_response_html
#             # mock_otodom_start_requests.return_value = otodom_mock_response_html
#             # mock_domiporta_start_requests.return_value = domiporta_mock_response_html
#             # mock_domiporta_current_url.return_value = f"file://{domiporta_mock_response_path}"
#             # mock_domiporta_start_urls.return_value = [f"file://{domiporta_mock_response_path}"]
#
#             self.driver.get(f"{self.live_server_url}/properties/scrape/")
#
#             # address_input = self.driver.find_element(By.ID, 'id_address')
#             # address_input.send_keys('Grodzisk Mazowiecki')
#             # time.sleep(1)  # Poczekaj na pojawienie się sugestii
#
#             # Wybierz pierwszą sugestię
#             # try:
#             #     autocomplete_suggestion = self.driver.find_element(By.CSS_SELECTOR, '.pac-container .pac-item:first-child')
#             #     ActionChains(self.driver).move_to_element(autocomplete_suggestion).click().perform()
#             # except NoSuchElementException:
#             #
#             #     self.fail("Nie znaleziono sugestii adresu.")
#
#             # Wypełnij pozostałe pola formularza
#             self.driver.find_element(By.ID, 'id_address').clear()
#             self.driver.find_element(By.ID, 'id_province').clear()
#             self.driver.find_element(By.ID, 'id_city').clear()
#             self.driver.find_element(By.ID, 'id_district').clear()
#             self.driver.find_element(By.ID, 'id_district_neighbourhood').clear()
#             self.driver.find_element(By.ID, 'id_street').clear()
#             self.driver.find_element(By.ID, 'id_price_min').clear()
#             self.driver.find_element(By.ID, 'id_price_max').clear()
#             self.driver.find_element(By.ID, 'id_area_min').clear()
#             self.driver.find_element(By.ID, 'id_area_max').clear()
#             self.driver.find_element(By.ID, 'id_build_year_from').clear()
#             self.driver.find_element(By.ID, 'id_build_year_to').clear()
#
#             self.driver.find_element(By.ID, 'id_address').send_keys('Grodzisk Mazowiecki, Polska')
#             self.driver.find_element(By.ID, 'id_province').send_keys('Mazowieckie')
#             self.driver.find_element(By.ID, 'id_city').send_keys('Grodzisk Mazowiecki')
#             self.driver.find_element(By.ID, 'id_price_min').send_keys('300000')
#             self.driver.find_element(By.ID, 'id_price_max').send_keys('400000')
#             # self.driver.find_element(By.ID, 'id_property_type').send_keys('flat')
#             # self.driver.find_element(By.ID, 'id_offer_type').send_keys('sell')
#
#             # Wyślij formularz
#             self.driver.find_element(By.CSS_SELECTOR, 'form input[type="submit"]').click()
#
#             # Poczekaj na załadowanie strony wynikowej
#             # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.search-results')))
#
#             # Sprawdź oczekiwany wynik
#
#             # Przykład sprawdzenia wyniku: Sprawdź, czy na stronie wynikowej wyświetla się lista ofert
#             # search_results = self.driver.find_elements(By.CSS_SELECTOR, '.search-results .result-item')
#             self.assertGreater(len(Property.objects.all()), 0)
#             # self.assertEqual(len(search_results), 29 + 6 + 31 + 6 + 2 * 24)
#             # morizon 29
#             # domiporta 6
#             # gratka 31
#             # olx 6
#             # otodom 2*24
#             self.addCleanup(self.driver.quit)
#
#     def test_scrape2(self):
#         # Utwórz fabrykę żądań Django
#         factory = RequestFactory()
#
#         # Utwórz żądanie do widoku `scrape`
#         request = factory.post("/scrape", data=SearchForm())
#         # Zastosuj dekorator PatchRequestMeta, aby podmienić metadane żądania
#         with PatchRequestMeta(request) as request_meta:
#             # Zdefiniuj ścieżki do lokalnych plików HTML
#             request_meta.add_url_mapping("www.domiporta.pl/offer/example", "test_data/domiporta/domiporta-details.html")
#
#             # Wywołaj widok `scrape`
#             response = scrape(request)
#
# class ScrapeTestCase(LiveServerTestCase):
#     pass
#
#     def setUp(self):
#         self.selenium = webdriver.Chrome('chromedriver')
#         # self.selenium = selenium_browser(headless=False)
#         # self.selenium_action=webdriver.ActionChains(self.selenium)
#
#     # def tearDown(self):
#     #     self.selenium.quit
#     @requests_mock.Mocker()
#     def test_search(self, mocker):
#         mocker.get(re.compile('.*otodom.pl/pl/oferty/sprzedaz/.+'),
#                    text=open("test_data/otodom/otodom-search.html", "r").read(), )
#         mocker.get(re.compile('.*olx.pl/d/nieruchomosci/.+'), text=open("test_data/olx/olx-search.html", "r").read(), )
#         mocker.get(re.compile('.*morizon.pl/mieszkania/.+'),
#                    text=open("test_data/morizon/morizon-search.html", "r").read(), )
#         mocker.get(re.compile('.*domiporta.pl/mieszkanie/sprzedam.+'),
#                    text=open("test_data/domiporta/domiporta-search.html", "r").read(), )
#         mocker.get(re.compile('.*gratka.pl/nieruchomosci/mieszkania/grodzisk-mazowiecki.+'),
#                    text=open("test_data/gratka/gratka-search.html", "r").read(), )
#
#         mocker.get(re.compile('.*otodom.pl/pl/oferta.+'),
#                    text=open("test_data/otodom/otodom-details.html", "r").read(), )
#         mocker.get(re.compile('.*olx.pl/d/oferta.+'), text=open("test_data/olx/olx-details.html", "r").read(), )
#         mocker.get(re.compile('.*domiporta.pl/nieruchomosci.+'),
#                    text=open("test_data/domiporta/domiporta-details.html", "r").read(), )
#         mocker.get(re.compile('.*gratka.pl/nieruchomosci/mieszkanie.+'),
#                    text=open("test_data/gratka/gratka-details.html", "r").read(), )
#         mocker.get(re.compile('.*morizon.pl/oferta/.+'),
#                    text=open("test_data/morizon/morizon-details.html", "r").read(), )
#
#         self.selenium.get(f"{self.live_server_url}/properties/scrape/")
#         # Wypełnij pozostałe pola formularza
#         self.selenium.find_element(By.ID, 'id_address').clear()
#         self.selenium.find_element(By.ID, 'id_province').clear()
#         self.selenium.find_element(By.ID, 'id_city').clear()
#         self.selenium.find_element(By.ID, 'id_district').clear()
#         self.selenium.find_element(By.ID, 'id_district_neighbourhood').clear()
#         self.selenium.find_element(By.ID, 'id_street').clear()
#         self.selenium.find_element(By.ID, 'id_price_min').clear()
#         self.selenium.find_element(By.ID, 'id_price_max').clear()
#         self.selenium.find_element(By.ID, 'id_area_min').clear()
#         self.selenium.find_element(By.ID, 'id_area_max').clear()
#         self.selenium.find_element(By.ID, 'id_build_year_from').clear()
#         self.selenium.find_element(By.ID, 'id_build_year_to').clear()
#
#         self.selenium.find_element(By.ID, 'id_address').send_keys('Grodzisk Mazowiecki, Polska')
#         self.selenium.find_element(By.ID, 'id_province').send_keys('Mazowieckie')
#         self.selenium.find_element(By.ID, 'id_city').send_keys('Grodzisk Mazowiecki')
#         self.selenium.find_element(By.ID, 'id_price_min').send_keys('300000')
#         self.selenium.find_element(By.ID, 'id_price_max').send_keys('350000')
#
#         # Wyślij formularz
#         self.selenium.find_element(By.CSS_SELECTOR, 'form input[type="submit"]').click()
