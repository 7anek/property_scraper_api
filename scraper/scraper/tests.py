# from django.test import TestCase
from unittest import TestCase

from scrapy.http import TextResponse, HtmlResponse, Response, Request
import json

try:
    from properties.models import Property
except ModuleNotFoundError:
    import os,sys
    from django.core.wsgi import get_wsgi_application
    sys.path.append(os.path.dirname(os.path.abspath('.')))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'properties_scrapping.settings'
    application = get_wsgi_application()
    from properties.models import Property
from scraper.spiders.otodom_spider import OtodomSpider
from scraper.spiders.domiporta_spider import DomiportaSpider
from scraper.spiders.gratka_spider import GratkaSpider
from scraper.spiders.morizon_spider import MorizonSpider
from scraper.spiders.olx_spider import OlxSpider
from scraper.pipelines import ScraperPipeline
from django.utils import timezone
from asgiref.sync import sync_to_async
from django.core.exceptions import ImproperlyConfigured
import unittest


def fake_response_from_file(file_name, url=None):
    """
    Create a Scrapy fake HTTP response from a HTML file
    @param file_name: The relative filename from the responses directory,
                    but absolute paths are also accepted.
    @param url: The URL of the response.
    returns: A scrapy HTTP response which can be used for unittesting.
    """
    if not url:
        url = 'http://www.example.com'

    request = Request(url=url)
    # if not file_name[0] == '/':
    #     responses_dir = os.path.dirname(os.path.realpath(__file__))
    #     file_path = os.path.join(responses_dir, file_name)
    # else:
    #     file_path = file_name
    file_path=f"/home/janek/python/property_scraper/{file_name}"
    file_content = open(file_path, 'r').read()

    # response = Response(url=url,
    response = TextResponse(url=url,
        request=request,
        body=file_content,
        encoding = 'utf-8'
        )
    # response.encoding = 'utf-8'
    return response


class ScraperParseTestCase(TestCase):

    # def setUp(self):
    #     self.otodom_spider = OtodomSpider()
    
    # def test_otodom_spider_from_file(self):
    #     search_form=json.dumps({'localization': 'Grodzisk Mazowiecki', 'price_min': 300000, 'price_max': 400000, 'area_min': None, 'area_max': None, 'property_type': 'flat', 'offer_type': 'sell', 'plot_type': '', 'house_type': '', 'flat_type': '', 'year_of_construction_from': None, 'year_of_construction_to': None})
    #     job_id='75d6b108cc9811edba0300155d7be260'
    #     params={'search_form':search_form,'_job':job_id}
    #     url="http://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/grodzisk-mazowiecki?distanceRadius=0&priceMin=300000&priceMax=400000&locations=%5Bcities_6-703%5D&viewType=listing&limit=24&page=1"
    #     results = self.spider.parse(fake_response_from_file('otodom-search4.html', url))

    #     print('results',results)
    #     print('list(results)',list(results))
    #     print('Property.objects.all()',Property.objects.all())
    #     print('Ala ma kota')

    def test_parse_otodom_offer(self):
        # return True
        search_form=json.dumps({'formatted_address': 'Jaktorów, Polska', 'province': 'Mazowieckie', 'city': 'Jaktorów', 'price_min': 30000, 'price_max': 400000, 'property_type': 'flat', 'offer_type': 'sell'})
        job_id='75d6b108cc9811edba0300155d7be260'
        spider=OtodomSpider(search_form=search_form,_job=job_id)
        print('test_parse_offer')
        path="test_data/otodom/otodom-details.html"
        # url='http://www.otodom.pl/64121978'
        url="nieważne"
        response = HtmlResponse(
            url=url,
            body=open(path, 'rb').read(),
            encoding='utf-8'
        )
        results = spider.parse_offer(response)
        # print('results',list(results))
        items = list(results)
        self.assertEqual(len(items), 1)
        item=items[0]
        # self.assertEqual(item['title'], 'Mieszkanie 48m²⭐Stan Deweloperski⭐3 pokoje⭐Centrum')
        # self.assertEqual(item['price'], 395000)
        self.assertEqual(item["service_id"], 62983737)
        self.assertEqual(item["service_name"],"otodom")
        self.assertEqual(item['title'], 'Mieszkanie, 44 m², Jaktorów')
        self.assertEqual(item['price'], 190000)
        # item["location"] = ", ".join([offer_dict["target"]["City"], offer_dict["target"]["Subregion"],offer_dict["target"]["Province"]])
        self.assertEqual(item["area"],44)
        # item["floor"] = parse_floor(offer_dict["target"]["Floor_no"]) if "Floor_no" in offer_dict["target"] else None
        self.assertEqual(item["number_of_rooms"],2)
        self.assertEqual(item["type_of_property"],"flat")
        # self.assertEqual(item["type_of_building"],"block")
        # item["create_date"] = datetime.fromisoformat(offer_dict["createdAt"])
        # item["modify_date"] = datetime.fromisoformat(offer_dict["modifiedAt"])
        # self.assertEqual(items[0]['location'], 'Wrocław, Krzyki, ul. Mickiewicza')
        # self.assertEqual(items[0]['description'], 'Kawalerka o powierzchni 50,17 m2 usytuowana na III piętrze w 6 piętrowym budynku na Krzykach')

    # # def test_otodom_spider_from_file(self):
    # #     search_form=json.dumps({'localization': 'Grodzisk Mazowiecki', 'price_min': 300000, 'price_max': 400000, 'area_min': None, 'area_max': None, 'property_type': 'flat', 'offer_type': 'sell', 'plot_type': '', 'house_type': '', 'flat_type': '', 'year_of_construction_from': None, 'year_of_construction_to': None})

    def test_parse_olx_offer(self):
        search_form=json.dumps({'formatted_address': 'Grodzisk Mazowiecki, Polska', 'province': 'Mazowieckie', 'city': 'Grodzisk Mazowiecki', 'price_min': 300000, 'price_max': 400000, 'property_type': 'flat', 'offer_type': 'sell'})
        job_id='75d6b108cc9811edba0300155d7be260'
        spider=OlxSpider(search_form=search_form,_job=job_id)
        print('test_parse_offer')
        path="test_data/olx/olx-details.html"
        # url='http://www.otodom.pl/64121978'
        url="nieważne"
        response = HtmlResponse(
            url=url,
            body=open(path, 'rb').read(),
            encoding='utf-8'
        )
        results = spider.parse_offer(response)
        # print('results',list(results))
        items = list(results)
        self.assertEqual(len(items), 1)
        item=items[0]
        self.assertEqual(item["service_id"], 710818583)
        self.assertEqual(item["service_name"],"olx")
        self.assertEqual(item['title'], 'Atrakcyjne mieszkania w centrum Grodziska Maz. ceny już od 8500/m2')
        self.assertEqual(item['price'], 380000.0)
        # item["location"] = ", ".join([offer_dict["target"]["City"], offer_dict["target"]["Subregion"],offer_dict["target"]["Province"]])
        self.assertEqual(item["area"],40.0)
        # item["floor"] = parse_floor(offer_dict["target"]["Floor_no"]) if "Floor_no" in offer_dict["target"] else None
        self.assertEqual(item["number_of_rooms"],2)
        self.assertEqual(item["type_of_property"],"flat")
        self.assertEqual(item["type_of_building"],"block_of_flats")
        # item["create_date"] = datetime.fromisoformat(offer_dict["createdAt"])
        # item["modify_date"] = datetime.fromisoformat(offer_dict["modifiedAt"])
        # self.assertEqual(items[0]['location'], 'Wrocław, Krzyki, ul. Mickiewicza')
        # self.assertEqual(items[0]['description'], 'Kawalerka o powierzchni 50,17 m2 usytuowana na III piętrze w 6 piętrowym budynku na Krzykach')

    def test_parse_domiporta_offer(self):
        search_form=json.dumps({'formatted_address': 'Chrzanów Mały, Polska', 'province': 'Mazowieckie', 'city': 'Chrzanów Mały', 'price_min': 300000, 'price_max': 400000, 'property_type': 'flat', 'offer_type': 'sell'})
        job_id='75d6b108cc9811edba0300155d7be260'
        spider=DomiportaSpider(search_form=search_form,_job=job_id)
        print('test_parse_offer')
        path="test_data/domiporta/domiporta-details.html"
        # url='http://www.otodom.pl/64121978'
        url="http://www.domiporta.pl/nieruchomosci/sprzedam-mieszkanie-dwupokojowe-chrzanow-maly-chrzanow-maly-41m2/154218398"
        request=Request(
            url=url
        )
        response = HtmlResponse(
            url=url,
            request=request,
            body=open(path, 'rb').read(),
            encoding='utf-8'
        )
        results = spider.parse_offer(response)
        # print('results',list(results))
        items = list(results)
        self.assertEqual(len(items), 1)
        item=items[0]
        # self.assertEqual(item["service_id"], 710818583)#wyciągane z requesta
        self.assertEqual(item["service_name"],"domiporta")
        self.assertEqual(item['title'], 'Mieszkanie dwupokojowe na sprzedaż')
        self.assertEqual(item['price'], 390000.0)
        # item["location"] = ", ".join([offer_dict["target"]["City"], offer_dict["target"]["Subregion"],offer_dict["target"]["Province"]])
        self.assertEqual(item["area"],41.0)
        # item["floor"] = parse_floor(offer_dict["target"]["Floor_no"]) if "Floor_no" in offer_dict["target"] else None
        self.assertEqual(item["floor"],2)
        self.assertEqual(item["number_of_rooms"],2)
        self.assertEqual(item["type_of_property"],"flat")
        self.assertEqual(item["type_of_building"],"block_of_flats")
        # item["create_date"] = datetime.fromisoformat(offer_dict["createdAt"])
        # item["modify_date"] = datetime.fromisoformat(offer_dict["modifiedAt"])
        # self.assertEqual(items[0]['location'], 'Wrocław, Krzyki, ul. Mickiewicza')
        # self.assertEqual(items[0]['description'], 'Kawalerka o powierzchni 50,17 m2 usytuowana na III piętrze w 6 piętrowym budynku na Krzykach')
    
    
    def test_parse_gratka_offer(self):
        search_form=json.dumps({'formatted_address': 'Grodzisk Mazowiecki, Polska', 'province': 'Mazowieckie', 'city': 'Grodzisk Mazowiecki', 'price_min': 300000, 'price_max': 400000, 'property_type': 'flat', 'offer_type': 'sell'})
        job_id='75d6b108cc9811edba0300155d7be260'
        spider=GratkaSpider(search_form=search_form,_job=job_id)
        print('test_parse_offer')
        path="test_data/gratka/gratka-details.html"
        url="nieważne"
        response = HtmlResponse(
            url=url,
            body=open(path, 'rb').read(),
            encoding='utf-8'
        )
        results = spider.parse_offer(response)
        # print('results',list(results))
        items = list(results)
        self.assertEqual(len(items), 1)
        item=items[0]
        self.assertEqual(item["service_id"], 30116547)
        self.assertEqual(item["service_name"],"gratka")
        self.assertEqual(item['title'], 'Mieszkanie Grodzisk Mazowiecki, ul. Grunwaldzka')
        self.assertEqual(item['price'], 348000.0)
        # item["location"] = ", ".join([offer_dict["target"]["City"], offer_dict["target"]["Subregion"],offer_dict["target"]["Province"]])
        self.assertEqual(item["area"],47.0)
        # item["floor"] = parse_floor(offer_dict["target"]["Floor_no"]) if "Floor_no" in offer_dict["target"] else None
        self.assertEqual(item["floor"],4)
        self.assertEqual(item["number_of_rooms"],3)
        self.assertEqual(item["type_of_property"],"flat")
        self.assertEqual(item["type_of_building"],"block_of_flats")
        # item["create_date"] = datetime.fromisoformat(offer_dict["createdAt"])
        # item["modify_date"] = datetime.fromisoformat(offer_dict["modifiedAt"])
        # self.assertEqual(items[0]['location'], 'Wrocław, Krzyki, ul. Mickiewicza')
        # self.assertEqual(items[0]['description'], 'Kawalerka o powierzchni 50,17 m2 usytuowana na III piętrze w 6 piętrowym budynku na Krzykach')

    def test_parse_morizon_offer(self):
        search_form=json.dumps({'formatted_address': 'Grodzisk Mazowiecki, Polska', 'province': 'Mazowieckie', 'city': 'Grodzisk Mazowiecki', 'price_min': 300000, 'price_max': 400000, 'property_type': 'flat', 'offer_type': 'sell'})
        job_id='75d6b108cc9811edba0300155d7be260'
        spider=MorizonSpider(search_form=search_form,_job=job_id)
        print('test_parse_offer')
        path="test_data/morizon/morizon-details.html"
        url="nieważne"
        response = HtmlResponse(
            url=url,
            body=open(path, 'rb').read(),
            encoding='utf-8'
        )
        results = spider.parse_offer(response)
        # print('results',list(results))
        # items = list(results)
        self.assertEqual(list(results), [])
        # item=items[0]
        # self.assertEqual(item["service_id"], 30116547)
        # self.assertEqual(item["service_name"],"morizon")
        # self.assertEqual(item['title'], 'DWA POKOJE W CENTRUM GRODZISKA MAZOWIECKIEGO (38 m2) - BEZPOŚREDNIO')
        # self.assertEqual(item['price'], 348000.0)
        # # item["location"] = ", ".join([offer_dict["target"]["City"], offer_dict["target"]["Subregion"],offer_dict["target"]["Province"]])
        # self.assertEqual(item["area"],47.0)
        # # item["floor"] = parse_floor(offer_dict["target"]["Floor_no"]) if "Floor_no" in offer_dict["target"] else None
        # self.assertEqual(item["floor"],4)
        # self.assertEqual(item["number_of_rooms"],3)
        # self.assertEqual(item["type_of_property"],"flat")
        # self.assertEqual(item["type_of_building"],"block_of_flats")
        # item["create_date"] = datetime.fromisoformat(offer_dict["createdAt"])
        # item["modify_date"] = datetime.fromisoformat(offer_dict["modifiedAt"])
        # self.assertEqual(items[0]['location'], 'Wrocław, Krzyki, ul. Mickiewicza')
        # self.assertEqual(items[0]['description'], 'Kawalerka o powierzchni 50,17 m2 usytuowana na III piętrze w 6 piętrowym budynku na Krzykach')


class ScraperPipelineTestCase(TestCase):

    def setUp(self):
        self.pipeline = ScraperPipeline()


    async def test_process_item(self):
        item = {}
        item["scrapyd_job_id"] = '75d6b108cc9811edba0300155d7be261'
        item["service_id"] = 64121979
        item["service_name"] = "otodom"
        item["title"] = "Fajny tytuł"
        item["price"] = 100.000
        item["location"] = "Grodzisk Mazowiecki, Grodziski, Mazowieckie"
        item["description"] = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce malesuada massa non euismod condimentum. Fusce et tincidunt lorem, a faucibus libero. Duis sed leo a massa tempus porta. Etiam consectetur eros nec metus volutpat tincidunt. Suspendisse imperdiet sit amet dui nec tempor. Curabitur id ligula cursus, pretium leo et, lobortis arcu. Suspendisse varius ante non enim dictum, eu molestie mi ultrices. Maecenas urna nisl, consectetur sit amet facilisis eget, vulputate et sapien. Maecenas at lorem faucibus, facilisis est et, ultrices ante. Donec condimentum condimentum urna, sit amet dignissim diam lobortis sollicitudin. Duis accumsan facilisis rhoncus."
        item["area"] = 100
        item["floor"] = 1
        item["number_of_rooms"] = 1
        item["type_of_property"] = "mieszkanie"
        item["type_of_building"] = "block"
        item["create_date"] = timezone.now()
        item["modify_date"] = timezone.now()
        processed_item = await self.pipeline.process_item(item, None)
        # processed_item = await sync_to_async(self.pipeline.process_item)(item, None)

        # existing_object = Property.objects.get(service_id=item["service_id"], service_name=item["service_name"])
        existing_objects = Property.objects.filter(service_id=item["service_id"], service_name=item["service_name"])
        # existing_object = await existing_objects.first()
        existing_object = await sync_to_async(existing_objects.first)()
        # obj = Model.objects.filter(id=1).first()

        self.assertNotEqual(existing_object, None)
        self.assertEqual(existing_object.service_id, 64121979)
        self.assertEqual(existing_object.service_name,"otodom")

    #TODO - dodać test na duplikaty

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
    #     item["type_of_property"] = "mieszkanie"
    #     item["type_of_building"] = "block"
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
        print('test_model_connection_is_working')
        try:
            Property.objects.create(title="adsad",price=12.32,area=23.43,service_name="sdfsdf")
            print('Property.objects.count()')
            c=Property.objects.count()
        except ImproperlyConfigured:
            print('ImproperlyConfigured')
            connected=False
        else:
            print('count',c)
            connected=True
        self.assertEqual(connected, True)

