import time

from django.shortcuts import render
from django.contrib.auth.models import User
from properties.search_results import SearchResults
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)
from rest_framework.exceptions import APIException, ValidationError
from django.db.utils import IntegrityError
from properties.models import Property
from properties_api.serializers import PropertySerializer, SearchResultsSerializer
import properties.search as search_api
from properties.forms import SearchForm
from scrapyd_api import ScrapydAPI
import json, uuid

from scraper.scrapy_factory import ScrapydSpiderFactory

from scraper.scrapyd_singleton import ScrapydAPISingleton
from scraper.utils import is_scrapyd_running
from scraper.scrapyd_api import scrapyd

# Create your views here.
class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class PropertiesSearch(APIView):

    # def perform_search(self, data):
    #     return search_api.webpages_search(data)

    def get(self, request, format='json'):
        search_params = request.GET
        # search_params['priceMin']
        print(';;;;;;;request.GET', request.GET)
        search_form = SearchForm(request.GET)
        print('**********request.query_params', request.query_params)
        if search_form.is_valid():
            search_results = SearchResults(search_form.cleaned_data)
            print('----------------search_results',search_results)
            print('----------------search_results.objects',search_results.objects)
            # search_results = self.perform_search(search_form.cleaned_data)
            print('********** len(search_results.objects)', len(search_results.objects))
            serializer = SearchResultsSerializer(search_results)
            print('********** len(serializer.data)', len(serializer.data['objects']))
            return Response(serializer.data)
        print('-------invalid form')
        return Response("invalid form", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PropertiesScrape(APIView):
    # scrapyd = ScrapydAPI('http://localhost:6800')
    serializer_class = PropertySerializer
    permission_classes = [AllowAny]

    def post(self, request):
        search_form = SearchForm(request.POST)


        # settings = get_project_settings()
        print('////////////',request.POST)
        # print('////////////',search_form)
        
        if search_form.is_valid():  
            print('//////////// form is ok',search_form.cleaned_data)
            if not is_scrapyd_running():
                return Response("Scrapyd unavailable", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            try:
                scrapy_factory = ScrapydSpiderFactory(json.dumps(search_form.cleaned_data))
                print('++++++++++++++++++scrapy_factory created')
                scrapy_factory.create_spiders()
                print('++++++++++++++++++scrapy_factory spiders created', scrapy_factory.job_ids)
            except Exception as e:
                return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            # while scrapy_factory.check_finished():
            #     print('++++++++++++++++++time.sleep(10)')
            #     time.sleep(10)


            # scrape_job_id = uuid.UUID(hex=job_id)
            properties = Property.objects.filter(scrape_job_id__in=scrapy_factory.job_ids)
            serializer = PropertySerializer(properties, many=True)
            return Response({'job_ids':scrapy_factory.job_ids,'properties':serializer.data,'finished':scrapy_factory.check_finished()})
        print('//////////// error - invalid form',search_form.cleaned_data)
        return Response("invalid form", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # def get(self, request, scrape_job_id, format="json"):
    def get(self, request, job_ids, format="json"):

        # uuids_list = uuids.replace('-','').split(',')
        uuids_list = job_ids.split(',')
        uuids_list=list(map(lambda job_id: uuid.UUID(hex=job_id), uuids_list))
        print(uuids_list)

        if is_scrapyd_running():
            if self.check_finished(uuids_list):
                properties = Property.objects.filter(scrape_job_id__in=uuids_list)
                serializer = PropertySerializer(properties, many=True)
                print('serializer.data:', serializer.data)
                return Response(serializer.data)
            else:
                return Response("Spiders are processing", status=status.HTTP_202_ACCEPTED)
        else:
            print("niepodłączono scrapyd")
            return Response("Scrapyd is not running", status=status.HTTP_500_INTERNAL_SERVER_ERROR)



    def check_finished(self, uuids):
        """
        czy któryś ze spiderów ma status running albo pending
        uuids - lista uuids
        return False - jeśli jest jakiś spider który jeszcze się nieskończył wykonywać"""
        return not any(scrapyd.job_status(project='scraper', job_id=job_id) in ['running', 'pending'] for job_id in uuids)


class SignUp(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        
        first_name = request.data["first_name"] if "first_name" in request.data else ""
        last_name = request.data["last_name"] if "last_name" in request.data else ""
        email = request.data["email"] if "email" in request.data else ""
        if "username" in request.data:
            username = request.data["username"] 
        else: 
            raise ValidationError("The given username must be set")
        password = request.data["password"] if "password" in request.data else ""
        try:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password, is_staff=False, is_superuser=False, is_active=True)
        except Exception as e:
            # raise APIException(str(e))
            return Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        try:
            user.save()
        except Exception as e:
            # raise APIException(str(e))
            return Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response("User created")

class SignIn(TokenObtainPairView):
    permission_classes = [AllowAny]

class SignOut(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        print('SignOut view')
        token = request.data["refresh"]
        if not token:
            print('not token')
            return Response("refresh token is empty", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        try:
            refresh_token = RefreshToken(token)
        except Exception as e:
            print(str(e))
            # raise APIException(str(e))
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        print('adding token to blacklist')
        refresh_token.blacklist()
        return Response("OK")