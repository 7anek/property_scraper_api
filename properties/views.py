from django.shortcuts import render
from properties.search_results import SearchResults
from scrapy.crawler import CrawlerProcess
# try:
#     from scraper.scraper.spiders.otodom_spider import PropertiesSpider
# except ModuleNotFoundError as e:
#     pass
#     # from scraper.spiders.otodom_spider import PropertiesSpider
import asyncio
from scrapy.utils.project import get_project_settings
import subprocess
from scrapyd_api import ScrapydAPI
from properties.models import Property
from properties.forms import SearchForm
import json
import uuid
import properties.search as search_api
from django.conf import settings


# Create your views here.
# connect scrapyd service
scrapyd = ScrapydAPI('http://localhost:6800')
# scrapyd = ScrapydAPI('http://localhost:9000')


def search(request):
    print('**********', request.GET)
    # print('**********', type(request.GET['priceMin']))
    if request.method == 'POST':
        print(request.POST)
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            data = search_form.cleaned_data
            print(data)
            results = SearchResults(data)
            # results = search_api.webpages_search(data)
            context = {"search_form": search_form, "search_results": results}
        else:
            print("Invalid Form")
            context = {"search_form": search_form, "error": "Invalid Form"}
    else:
        search_form = SearchForm()
        context = {"search_form": search_form}
    return render(request, "properties/search.html", context)

def scrape(request):
    # process = subprocess.run(["python", "manage.py", "crawl"], check=True)
    # data = process.stdout
    # data = process
    # process = CrawlerProcess(get_project_settings())
    # process.crawl(PropertiesSpider) # Assuming that you are passing the argumment of the car_model to scrape specific models
    # process.start()
    # data = "abc"
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        # settings = get_project_settings()
        # print('////////////',settings)
        if search_form.is_valid():  
            job_id = scrapyd.schedule('default', 'gratka', search_form = json.dumps(search_form.cleaned_data))
            # job_id = scrapyd.schedule('default', 'otodom', search_form = json.dumps(search_form.cleaned_data))
            # job_id = scrapyd.schedule('default', 'otodom', settings=settings)
            scrape_status =  scrapyd.job_status('default', job_id)
            scrape_job_id = uuid.UUID(hex=job_id)
            properties = Property.objects.filter(scrape_job_id=scrape_job_id)[:500]
            context = {"title": "search", "search_form": search_form, "properties":properties, 'scrape_status': scrape_status, 'scrape_job_id':scrape_job_id}
        else:
            search_form = SearchForm()
            context = {"title": "search", "search_form": search_form}
    elif request.method == 'GET':
        search_form = SearchForm()
        data = Property.objects.all()[:500]
        context = {"title": "search", "search_form": search_form}
    else:
        search_form = SearchForm()
        context = {"title": "search", "search_form": search_form}
        print('******* django view DATABASES', settings.DATABASES)
        print('******* django view PGSERVICEFILE', settings.PGSERVICEFILE)
        print('******* django view PGPASSFILE', settings.PGPASSFILE)
    return render(request, "properties/scrape.html", context)

def get_scrape(request, scrape_job_id):
    search_form = SearchForm()
    scrape_status = scrapyd.job_status('default', scrape_job_id.hex)
    properties = Property.objects.filter(scrape_job_id=scrape_job_id)[:500]
    context = {"title": "search", "search_form": search_form, "properties":properties, 'scrape_status': scrape_status, 'scrape_job_id':scrape_job_id}
    return render(request, "properties/scrape.html", context)