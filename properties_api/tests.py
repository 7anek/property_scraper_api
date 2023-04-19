from django.test import TestCase
from rest_framework.test import APIRequestFactory
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from properties.models import Property
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

# Create your tests here.

class RestApiTestCase(APITestCase):
    # def setUp(self):
    #     # self.obj = MyModel.objects.create(name="John")
    #     pass

    @classmethod
    def setUpTestData(cls):

        cls.user = User.objects.create_user("testuser", password="password")
        cls.access_token = str(AccessToken.for_user(cls.user))
        Property.objects.create(title="aaa",price=234,area=245, service_name="blabla")
        Property.objects.create(title="bbb",price=643,area=234, service_name="uuuuu")

    #     #the testing framework will automatically call once for this class
    #     #setUpTestData - jest elementem django i robi rollback w przypadku niepowodzenia
    #     cls.search_criteria = {'localization': 'Grodzisk Mazowiecki', 'price_min': 300000, 'price_max': 400000, 'area_min': None, 'area_max': None, 'property_type': 'flat', 'offer_type': 'sell', 'plot_type': '', 'house_type': '', 'flat_type': '', 'year_of_construction_from': None, 'year_of_construction_to': None}#zakładam że na takie kryteria wyszukiwania będe dostawał wyniki
    #     cls.search_results = search.webpages_search(cls.search_criteria)
    #     print("setUpClass")
    # def setUp(self):
        

    def test_objects_list_unauthenticated(self):
        url = reverse("properties_api:property-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_objects_list_authenticated(self):
        url = reverse("properties_api:property-list")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        self.assertEqual(len(response.data), 2)
