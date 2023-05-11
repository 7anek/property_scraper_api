from selenium.webdriver.chrome.options import Options
from selenium import webdriver

def localization_fields_from_search_form(item, search_form):
    item["formatted_address"]=search_form["formatted_address"] if "formatted_address" in search_form else None
    item["province"]=search_form["province"] if "province" in search_form else None
    item["county"]=search_form["county"] if "county" in search_form else None
    item["city"]=search_form["city"] if "city" in search_form else None
    item["district"]=search_form["district"] if "district" in search_form else None
    item["district_neighbourhood"]=search_form["district_neighbourhood"] if "district_neighbourhood" in search_form else None
    item["street"]=search_form["street"] if "street" in search_form else None
    return item

def selenium_browser(headless=True):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome("/home/janek/python/property_scraper/chromedriver", options=chrome_options)