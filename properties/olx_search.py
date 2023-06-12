from properties import olx
from playwright.sync_api import sync_playwright
from properties.search import Search, SearchResult
from properties.utils import *


class OlxSearch(Search):
    service_label = 'olx'
    url_netloc = "www.olx.pl"
    # end_results_tekst="Sprawdź ogłoszenia w większej odległości:"
    last_page=False

    def get_url_path(self):
        return olx.get_url_path(self.search_params)


    def get_request_params(self, page):
        try:
            request_params=olx.get_request_params(self.search_params,page=page)
        except Exception as err:
            print(err)
            request_params=False
        print('request_params',request_params)
        return request_params
    

    def get_page_html(self):
        if self.first_page and "district" in self.search_params:
            print('*******olx request js rendered')
            with sync_playwright() as playwright:
                browser = playwright.chromium.launch()
                page = browser.new_page()
                page.goto(self.request_url)
                page.wait_for_selector('#onetrust-accept-btn-handler')
                page.click('#onetrust-accept-btn-handler')
                page.locator('button[data-testid="clear-btn"][class="css-4s5yc1"]').click()
                location_input=page.locator('input[data-testid="location-search-input"]')
                location_input.click()
                location_input.fill(self.search_params['city']+", "+self.search_params['district'])
                page.locator('div[data-testid="suggestion-list"]').locator("li:first-child").click()

                page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
                self.request_params=url_to_params_dict(page.url())
                return page.content()
        else:
            print('*******olx super().get_page_html()')
            return super().get_page_html()

    def search(self):
        """
        attrs - dict with filter criteria
        get page content using requests library and parse it using BeautifulSoup
        function requests search results
        """
        print('search')
        current_page=1
        ret=True
        self.first_page=True
        while not self.last_page: 
            print('in while loop, not self.last_page:',not self.last_page)
            result = self.search_single_page(current_page)
            if not result:
                ret=False
            current_page = current_page+1
            self.first_page=True
        return ret

    def parse_results(self, soup):
        """
        olx na początku daje ogłoszenia w szukanej lokalizacji, póżniej daje w coraz dalszych. 
        zeby pobrać wyniki tylko z szukanej lokalizacji trzeba pobierać kolejne strony aż trafi się na taką z tekstem:
        Sprawdź ogłoszenia w większej odległości:, dalej są już oferty tylko z innych lokalizacji i pobierać z każdej strony pierwszy <div data-testid="listing-grid, na stronach z ofertami z tylko naszą lokalizacją jest on jeden, a jak jest podany wyżej tekst to są dwa i trzeba pobrać ten pierwszy
        """
        # if not soup("div", class_="css-pband8"):
        #     return False
        # results_count=int(soup.find("div",{"data-testid":"total-count"}).text.split()[1])
        if(soup.find("div", {"class": "css-wsrviy"})):
            self.last_page=True

        # self.num_pages = math.ceil(self.results_count/self.results_per_page)
        search_results_soup = soup.find("div", {"data-testid":"listing-grid"}).find_all("a")

        print('len(search_results_soup)',len(search_results_soup))
        results_arr = []
        for search_result_soup in search_results_soup:
            search_result = SearchResult()
            offer_url = search_result_soup["href"]
            if offer_url.startswith(("https://www.otodom.pl","www.otodom.pl")):#niechcemy ofert z otodom bo pobieramy je w innym miejscu i będą się dublowały
                continue
            elif offer_url.startswith(("https","www")):#oferta z innego serwisu
                search_result.offer_url = offer_url
            else:
                search_result.offer_url = self.get_service_url(path=search_result_soup["href"])
                search_result.offer_url_path = offer_url
            image_url = search_result_soup.find("div", class_="css-gl6djm").find("img")["src"]
            if image_url.startswith(("https","www")):
                search_result.main_image_url = image_url
            elif image_url.startswith(("/app/static/media/")): 
                search_result.main_image_url = self.get_service_url(path=image_url)
            else:
                search_result.main_image_url = ''
            search_result.title = search_result_soup.find("h6").text
            search_result.price = search_result_soup.find(
                "h6").find_next("p").text
            area_soup=search_result_soup.find("span", class_="css-643j0o")
            if area_soup:
                area_text = area_soup.text
                if "-" in area_text:
                    search_result.area, search_result.price_per_square_meter = search_result_soup.find(
                    "span", class_="css-643j0o").text.split(" - ")
                else:
                    search_result.area = area_text
            else:
                search_result.area =0

            search_result.service =  self.service_label
            results_arr.append(search_result)

        return results_arr


    def parse_single_result(self):
        pass


    def get_request_single_result_url(self):
        pass
