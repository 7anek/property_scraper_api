from properties import nieruchomosci_online
from properties.search import Search, SearchResult


class NieruchomosciOnlineSearch(Search):
    service_label = 'nieruchomosci-online'
    url_netloc = "nieruchomosci-online.pl"
    # end_results_tekst="Sprawdź ogłoszenia w większej odległości:"
    last_page=False

    def get_url_path(self):
        return nieruchomosci_online.get_url_path(self.search_params)


    def get_request_params(self, page):
        # request_params = DictAutoVivification()
        try:
            request_params=nieruchomosci_online.get_request_params(self.search_params,page=page)
        except Exception as err:
            print(err)
            request_params=False
        print('request_params',request_params)
        return request_params
    

    # def get_page_html(self):
    #     with sync_playwright() as playwright:
    #         browser = playwright.chromium.launch()
    #         page = browser.new_page()
    #         page.goto(self.request_url)
    #         page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
    #         return page.content()
    def search(self):
        """
        attrs - dict with filter criteria
        get page content using requests library and parse it using BeautifulSoup
        function requests search results
        """
        current_page=1
        ret=True
        while not self.last_page: 
            result = self.search_single_page(current_page)
            if not result:
                ret=False
                break
            current_page = current_page+1
        return ret

    def parse_results(self, soup):

        # if not soup("div", class_="css-pband8"):
        #     return False
        results_count=int(soup.find("span",{"id":"boxOfCounter"}).text.split()[0])
        if(soup.find("h2", {"id": "pie_searchSupplement"})):
            self.last_page=True

        # self.num_pages = math.ceil(self.results_count/self.results_per_page)
        search_results_soup = soup.find("div",{"class":"column-container"}).find_all("div",{"class":"tile__top"})

        print('len(search_results_soup)',len(search_results_soup))
        results_arr = []
        for search_result_soup in search_results_soup:
            search_result = SearchResult()
            search_result.offer_url = search_result_soup.find("h2").find("a")["href"]
            search_result.main_image_url = search_result_soup.find("div",{"class":"tile-holder"}).find("a").find("img")["src"]
            search_result.title = search_result_soup.find("h2").find("a").text
            search_result.price = int(''.join(filter(str.isdigit,search_result_soup.find("p",{"class":"title-a"}).span.text.split())))
            search_result.area = float(search_result_soup.find("span",{"class":"area"}).text.split()[0].replace(",","."))
            search_result.service =  self.service_label
            results_arr.append(search_result)

        self.results_count=len(results_arr)
        return results_arr


    def parse_single_result(self):
        pass


    def get_request_single_result_url(self):
        pass
