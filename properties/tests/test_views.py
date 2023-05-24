from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from unittest.mock import patch, MagicMock
from properties.views import scrape
from properties.forms import SearchForm
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class MockScrapydHandler(BaseHTTPRequestHandler):
    job_id = '75d6b108cc9811edba0300155d7be260'  # Przykładowe poprawne ID pracy

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response_data = {
            'status': 'ok',
            'jobid': self.job_id
        }
        response = json.dumps(response_data).encode('utf-8')
        self.wfile.write(response)

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response_data = {
            'status': 'ok',
            'jobid': self.job_id
        }
        response = json.dumps(response_data).encode('utf-8')
        self.wfile.write(response)

class ScrapeTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.server_address = ('localhost', 6800)
        cls.server = HTTPServer(cls.server_address, MockScrapydHandler)
        cls.server_thread = threading.Thread(target=cls.server.serve_forever)
        cls.server_thread.daemon = True
        cls.server_thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.server_thread.join()
        super().tearDownClass()

    def setUp(self):
        super().setUp()
        self.form_data = {'formatted_address': 'Grodzisk Mazowiecki, Polska', 'province': 'Mazowieckie',
                          'city': 'Grodzisk Mazowiecki', 'price_min': 300000, 'price_max': 400000,
                          'property_type': 'flat', 'offer_type': 'sell'}
    #
    def tearDown(self):
        super().tearDown()
        # Tutaj wykonaj czynności po zakończeniu testu

    @patch('scraper.spiders.gratka_spider.GratkaSpider')
    @patch('scrapyd_api.ScrapydAPI')
    def test_scrape(self, mock_scrapyd, mock_spider):
        # Tworzenie żądania POST z danymi formularza
        # Inicjalizacja mockowanego obiektu GratchaSpider
        spider_instance = mock_spider.return_value
        client = Client()
        scrape_url = reverse('scrape')

        mock_scrapyd.return_value.job_status.side_effect = [
            {'status': 'pending', 'jobid': '75d6b108cc9811edba0300155d7be260'},
            {'status': 'running', 'jobid': '75d6b108cc9811edba0300155d7be260'},
            {'status': 'finished', 'jobid': '75d6b108cc9811edba0300155d7be260'}
        ]

        response = client.post(scrape_url, data=self.form_data)

        # Sprawdzenie statusu odpowiedzi
        self.assertEqual(response.status_code, 200)

        # Sprawdzenie, czy metoda start_requests została wywołana na mockowanym spiderze
        spider_instance.start_requests.assert_called_once()

        # Sprawdzenie, czy metoda job_status została wywołana na mockowanym Scrapyd API
        mock_scrapyd.return_value.job_status.assert_called()

        # Sprawdzenie, czy metoda job_status została wywołana z oczekiwanymi parametrami
        expected_calls = [
            call('default', '75d6b108cc9811edba0300155d7be260'),
            call('default', '75d6b108cc9811edba0300155d7be260'),
            call('default', '75d6b108cc9811edba0300155d7be260')
        ]
        mock_scrapyd.return_value.job_status.assert_has_calls(expected_calls)


