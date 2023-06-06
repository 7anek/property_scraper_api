from unittest import TestCase
from unittest.mock import patch

import requests
import requests_mock
from asgiref.sync import sync_to_async
from django.core.exceptions import ImproperlyConfigured
from requests import Response

from properties.models import Property
from django.utils import timezone
from scraper.pipelines import ScraperPipeline
from scraper.items import ScraperItem
from scraper.utils import *
from django.conf import settings

class ScraperPipelineTestCase(TestCase):
    def setUp(self):
        self.pipeline = ScraperPipeline()

    async def test_process_item(self):
        # item = {}
        item = ScraperItem()
        item["scrapyd_job_id"] = "75d6b108cc9811edba0300155d7be261"
        item["service_id"] = 64121979
        item["service_name"] = "otodom"
        item[
            "service_url"
        ] = "https://www.otodom.pl/pl/oferta/piekne-mieszkanie-32-5m2-bielany-garaz-podziemny-ID4l33t.html"
        item["title"] = "Fajny tytuł"
        item["price"] = 100.000
        item["location"] = "Grodzisk Mazowiecki, Grodziski, Mazowieckie"
        item[
            "description"
        ] = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce malesuada massa non euismod condimentum. Fusce et tincidunt lorem, a faucibus libero. Duis sed leo a massa tempus porta. Etiam consectetur eros nec metus volutpat tincidunt. Suspendisse imperdiet sit amet dui nec tempor. Curabitur id ligula cursus, pretium leo et, lobortis arcu. Suspendisse varius ante non enim dictum, eu molestie mi ultrices. Maecenas urna nisl, consectetur sit amet facilisis eget, vulputate et sapien. Maecenas at lorem faucibus, facilisis est et, ultrices ante. Donec condimentum condimentum urna, sit amet dignissim diam lobortis sollicitudin. Duis accumsan facilisis rhoncus."
        item["area"] = 100
        item["floor"] = 1
        item["number_of_rooms"] = 1
        item["property_type"] = "mieszkanie"
        item["house_type"] = "block"
        item["create_date"] = timezone.now()
        item["modify_date"] = timezone.now()
        processed_item = await self.pipeline.process_item(item, None)
        # processed_item = await sync_to_async(self.pipeline.process_item)(item, None)

        # existing_object = Property.objects.get(service_id=item["service_id"], service_name=item["service_name"])
        existing_objects = Property.objects.filter(
            service_id=item["service_id"], service_name=item["service_name"]
        )
        # existing_object = await existing_objects.first()
        existing_object = await sync_to_async(existing_objects.first)()
        # obj = Model.objects.filter(id=1).first()

        self.assertNotEqual(existing_object, None)
        self.assertEqual(existing_object.service_id, 64121979)
        self.assertEqual(existing_object.service_name, "otodom")

    # TODO - dodać test na duplikaty

    # async def test_process_item_wrong_type_of_field(self):
    #     item = {}
    #     item["scrapyd_job_id"] = '75d6b108cc9811edba0300155d7be261'
    #     item["service_id"] = 64121979
    #     item["service_name"] = "otodom"
    #     item["title"] = "Fajny tytuł"
    #     item["price"] = '100.000'
    #     item["location"] = "Grodzisk Mazowiecki, Grodziski, Mazowieckie"
    #     item["description"] = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce malesuada massa non euismod condimentum. Fusce et tincidunt lorem, a faucibus libero. Duis sed leo a massa tempus porta. Etiam consectetur eros nec metus volutpat tincidunt. Suspendisse imperdiet sit amet dui nec tempor. Curabitur id ligula cursus, pretium leo et, lobortis arcu. Suspendisse varius ante non enim dictum, eu molestie mi ultrices. Maecenas urna nisl, consectetur sit amet facilisis eget, vulputate et sapien. Maecenas at lorem faucibus, facilisis est et, ultrices ante. Donec condimentum condimentum urna, sit amet dignissim diam lobortis sollicitudin. Duis accumsan facilisis rhoncus."
    #     item["area"] = '100'
    #     item["floor"] = [1]
    #     item["number_of_rooms"] = ['1']
    #     item["property_type"] = "mieszkanie"
    #     item["house_type"] = "block"
    #     item["create_date"] = timezone.now()
    #     item["modify_date"] = timezone.now()
    #     processed_item = await self.pipeline.process_item(item, None)
    #     # processed_item = await sync_to_async(self.pipeline.process_item)(item, None)

    #     # existing_object = Property.objects.get(service_id=item["service_id"], service_name=item["service_name"])
    #     existing_objects = Property.objects.filter(service_id=item["service_id"], service_name=item["service_name"])
    #     # existing_object = await existing_objects.first()
    #     existing_object = await sync_to_async(existing_objects.first)()
    #     # obj = Model.objects.filter(id=1).first()

    #     self.assertNotEqual(existing_object, None)
    #     self.assertEqual(existing_object.service_id, 64121979)
    #     self.assertEqual(existing_object.service_name,"otodom")


class ScraperModelTestCase(TestCase):
    def test_model_connection_is_working(self):
        print("test_model_connection_is_working")
        try:
            Property.objects.create(
                title="adsad",
                price=12.32,
                area=23.43,
                service_name="sdfsdf",
                service_url="jhbjh",
            )
            print("Property.objects.count()")
            c = Property.objects.count()
        except ImproperlyConfigured:
            print("ImproperlyConfigured")
            connected = False
        else:
            print("count", c)
            connected = True
        self.assertEqual(connected, True)

class UtilsTestCase(TestCase):

    @patch('requests.get')
    def test_is_scrapyd_running_false(self, get_mock):
        # scrapyd_url = f'{settings.SCRAPYD_URL}/daemonstatus.json'
        # mocker.get(scrapyd_url, text=open("test_data/olx/olx-search.html", "r").read(), )

        get_mock.side_effect=requests.exceptions.ConnectionError()
        self.assertEqual(is_scrapyd_running(),False)

    @patch('requests.get')
    def test_is_scrapyd_running_true(self, get_mock):
        # scrapyd_url = f'{settings.SCRAPYD_URL}/daemonstatus.json'
        # mocker.get(scrapyd_url, text=open("test_data/olx/olx-search.html", "r").read(), )
        r=Response()
        r.status_code=200
        get_mock.return_value = r
        self.assertEqual(is_scrapyd_running(), True)