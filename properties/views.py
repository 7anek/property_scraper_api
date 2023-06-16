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
from scraper.utils import is_scrapyd_running

from scraper.scrapy_factory import ScrapydSpiderFactory
import time

# from scraper.scrapyd_singleton import ScrapydAPISingleton
from scraper.scrapyd_api import scrapyd
from django.contrib.auth.decorators import login_required


# Create your views here.
# connect scrapyd service
# scrapyd = ScrapydAPI('http://localhost:6800')


# scrapyd = ScrapydAPI('http://localhost:9000')

def home(request):
    return render(request, "properties/home.html")
@login_required
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

@login_required
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
        if is_scrapyd_running():
            # settings = get_project_settings()
            # print('////////////',settings)
            if search_form.is_valid():
                print('///////////search_form.cleaned_data', search_form.cleaned_data)
                # job_id = scrapyd.schedule('scraper', 'gratka', search_form=json.dumps(search_form.cleaned_data))
                # job_id = scrapyd.schedule('default', 'gratka', search_form=json.dumps(search_form.cleaned_data))
                # job_id = scrapyd.schedule('default', 'otodom', search_form = json.dumps(search_form.cleaned_data))
                # job_id = scrapyd.schedule('default', 'otodom', settings=settings)
                try:
                    scrapy_factory = ScrapydSpiderFactory(json.dumps(search_form.cleaned_data))
                except Exception as e:
                    print(str(e))
                print('++++++++++++++++++scrapy_factory created')
                scrapy_factory.create_spiders()
                print('++++++++++++++++++scrapy_factory spiders created', scrapy_factory.job_ids)
                # while scrapy_factory.check_finished():
                #     print('++++++++++++++++++time.sleep(10)')
                #     time.sleep(10)

                # print('++++++++++++++++++job_id',job_id)
                # scrape_status = scrapyd.job_status('scraper', job_id)
                # scrape_job_id = uuid.UUID(hex=job_id)

                if not settings.TESTING:
                # if not settings.get('TESTING'):
                    time.sleep(5)


                properties = Property.objects.filter(scrapyd_job_id__in=scrapy_factory.job_ids)
                print("$$$$$$$$$$$$$$ properties",properties)
                context = {"title": "search", "search_form": search_form, "properties": properties,
                           "scrape_status": "Running", "scrapyd_job_id": ",".join(scrapy_factory.job_ids)}
                print("$$$$$$$$$$$$$$ context", context)
                if scrapy_factory.check_finished():
                    context["scrape_status"] = "Finished"
                else:
                    context["scrape_status"] = "Running"
            else:
                search_form = SearchForm()
                context = {"title": "search", "search_form": search_form, 'error': 'Invalid form data'}
        else:
            context = {"title": "search", "search_form": search_form, 'error': 'Scrapyd unavailable'}
    else:
        search_form = SearchForm()
        if is_scrapyd_running():
            context = {"title": "search", "search_form": search_form}
        else:
            context = {"title": "search", "search_form": search_form, 'error': 'Scrapyd unavailable'}

    return render(request, "properties/scrape.html", context)

@login_required
def get_scrape(request, uuids):
    search_form = SearchForm()
    uuids_list = uuids.split(',')
    try:
        uuids_list = list(map(lambda job_id: uuid.UUID(hex=job_id), uuids_list))
    except:
        context = {"title": "scrape", "search_form": search_form, "error": f"Wrong job ids: {uuids}"}
        return render(request, "properties/scrape.html", context)
    print(uuids_list)
    properties = Property.objects.filter(scrapyd_job_id__in=uuids_list)
    context = {"title": "scrape", "search_form": search_form, "properties": properties, 'scrape_job_id': uuids}
    if is_scrapyd_running():
        if check_finished(uuids_list):
            context["scrape_status"]="Finished"
        else:
            context["scrape_status"]="Running"
    else:
        context['error']='Scrapyd unavailable'
    return render(request, "properties/scrape.html", context)


def check_finished(uuids):
    """uuids - lista uuids
    return False - jeśli jest jakiś spider który jeszcze się nieskończył wykonywać"""
    return not any(scrapyd.job_status(project='scraper', job_id=job_id) in ['running', 'pending'] for job_id in uuids)