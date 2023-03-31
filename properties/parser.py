from bs4 import BeautifulSoup
from properties.utils import *

class SearchResult:
    offer_url = ''
    offer_url_path = ''
    main_image_url = ''
    title = ''
    price = ''
    price_per_square_meter = ''
    number_of_rooms = ''
    area = ''
    service=''

def otodom_search_parser(response):
    print('//////////////////','otodom_search_parser',',,,,,,,,,,,,,')
    # soup = BeautifulSoup(response.text, 'html.parser')
    soup = BeautifulSoup(response.text, 'lxml')
    offers_html = soup.find_all('a', {"data-cy": "listing-item-link"})
    results_arr = []
    for offer in offers_html:
        search_result = SearchResult()
        search_result.offer_url_path = offer['href']
        search_result.offer_url = get_custom_url(
            scheme="https", netloc="www.otodom.pl", path=offer['href'])
        search_result.main_image_url = offer.find("img")["src"]
        title_tag = offer.find("h3", {"data-cy": "listing-item-title"})
        search_result.title = title_tag.text
        params_arr = title_tag.find_next("div").find_all("span")
        search_result.price = params_arr[0].text
        search_result.price_per_square_meter = params_arr[1].text
        search_result.number_of_rooms = params_arr[2].text
        search_result.area = params_arr[3].text
        search_result.service =  "otodom"

        results_arr.append(search_result)

        print('***** otodom url:', search_result.offer_url)
        print('***** otodom url path:', search_result.offer_url_path)

    return results_arr

def otodom_get_parser(response):
        print('...........','otodom_get_parser',',,,,,,,,,,,,,')
        soup = BeautifulSoup(response.text, 'lxml')
        offer = {}
        header = soup.find("header")
        offer["title"] = header.h1.text
        offer["price"] = header.find("strong",{'aria-label':'Cena'}).text
        offer["price_per_square_meter"] = header.find("div",{'aria-label':'Cena za metr kwadratowy'}).text
        offer["localization"] = header.find("a").text
        # Szczegóły ogłoszenia
        
        return offer