from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import requests
from django.conf import settings


def localization_fields_from_search_form(item, search_form):
    item["address"] = search_form["formatted_address"] if "formatted_address" in search_form else None
    item["province"] = search_form["province"] if "province" in search_form else None
    item["county"] = search_form["county"] if "county" in search_form else None
    item["city"] = search_form["city"] if "city" in search_form else None
    item["district"] = search_form["district"] if "district" in search_form else None
    item["district_neighbourhood"] = search_form["district_neighbourhood"] if "district_neighbourhood" in search_form else None
    item["street"] = search_form["street"] if "street" in search_form else None
    return item


def selenium_browser(headless=True):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    # return webdriver.Chrome("/home/janek/python/property_scraper/chromedriver", options=chrome_options)
    return webdriver.Chrome("chromedriver", options=chrome_options)

def is_scrapyd_running():
    """scrapyd: obiekt scrapyd_api.ScrapydAPI('host:port')"""
    scrapyd_url = settings.SCRAPYD_URL
    try:
        response = requests.get(f'{scrapyd_url}/daemonstatus.json')
        if response.status_code == 200:
            print('Scrapyd is running.')
            is_scrapyd_running=True
        else:
            print('Scrapyd is not running.')
            is_scrapyd_running=False
    except requests.exceptions.ConnectionError:
        print('Unable to connect to Scrapyd.')
        is_scrapyd_running=False
    return is_scrapyd_running