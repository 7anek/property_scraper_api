from django.shortcuts import render
from django.contrib.auth.models import User
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

# Create your views here.
class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class PropertiesSearch(APIView):

    def perform_search(self, data):
        return search_api.webpages_search(data)

    def get(self, request, format='json'):
        search_params = request.GET
        # search_params['priceMin']
        search_form = SearchForm(request.GET)
        print('**********', request.query_params)
        if search_form.is_valid():
            search_results = self.perform_search(search_form.cleaned_data)
            print('********** len(search_results.objects)', len(search_results.objects))
            serializer = SearchResultsSerializer(search_results)
            print('********** len(serializer.data)', len(serializer.data['objects']))
            return Response(serializer.data)
        return Response("a")


class PropertiesScrape(APIView):
    scrapyd = ScrapydAPI('http://localhost:6800')
    serializer_class = PropertySerializer
    permission_classes = [AllowAny]

    def post(self, request):
        search_form = SearchForm(request.POST)
        # settings = get_project_settings()
        # print('////////////',request.POST)
        # print('////////////',search_form)
        
        if search_form.is_valid():  
            print('//////////// form is ok',search_form.cleaned_data)
            try:
                job_id = self.scrapyd.schedule('default', 'otodom', search_form = json.dumps(search_form.cleaned_data))
            except Exception as e:
                return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            # job_id = scrapyd.schedule('default', 'otodom', settings=settings)
            scrape_status =  self.scrapyd.job_status('default', job_id)
            scrape_job_id = uuid.UUID(hex=job_id)
            properties = Property.objects.filter(scrape_job_id=scrape_job_id)[:500]
            return Response(scrape_job_id)
        print('//////////// error - invalid form',search_form.cleaned_data)
        return Response("invalid form", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get(self, request, scrape_job_id, format="json"):
        print('scrape_job_id:',scrape_job_id)
        print('scrape_job_id.hex:',scrape_job_id.hex)
        scrape_status = self.scrapyd.job_status('default', scrape_job_id.hex)
        if scrape_status == 'finished':
            properties = Property.objects.filter(scrape_job_id=scrape_job_id)[:500]
            serializer = PropertySerializer(properties, many=True)
            print('serializer.data:',serializer.data)
            return Response(serializer.data)
            # return Response(properties)
        elif scrape_status in ['running', 'pending']:
            return Response(scrape_status, status=status.HTTP_202_ACCEPTED)
        return Response("unknown scrapyd status", status=status.HTTP_500_INTERNAL_SERVER_ERROR)



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
            raise APIException(str(e))
            # return Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        try:
            user.save()
        except Exception as e:
            raise APIException(str(e))
            # return Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response("User created")

class SignIn(TokenObtainPairView):
    permission_classes = [AllowAny]

class SignOut(APIView):
    def post(self, request):
        token = request.data["refresh"]
        if not token:
            return Response("refresh token is empty", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        try:
            refresh_token = RefreshToken(token)
        except Exception as e:
            raise APIException(str(e))
            # return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        refresh_token.blacklist()
        return Response("OK")