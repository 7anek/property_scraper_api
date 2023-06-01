from .scrapyd_singleton import ScrapydAPISingleton
from scrapy.utils.project import get_project_settings

class ScrapydSpiderFactory:
    def __init__(self, search_form_json):
        self.search_form = search_form_json
        scraper_settings = get_project_settings()
        self.project_name = "scraper"
        # self.project_name = scraper_settings.get('SCRAPYD_PROJECT')
        self.scrapyd = ScrapydAPISingleton("http://localhost:6800")
        # self.scrapyd = ScrapydAPISingleton(scraper_settings.get('SCRAPYD_URL'))
        print("self.project_name",self.project_name)
        self.job_ids = []

    def create_spiders(self):
        print('create_spiders')
        # spiders=['otodom','olx','domiporta','morizon','gratka']
        spider_names=['domiporta']
        for spider_name in spider_names:
            job_id=self.schedule_spider(spider_name)
            print('spider_name',spider_name, 'job_id', job_id)
            self.job_ids.append(job_id)

    def schedule_spider(self, spider_name):
        spider_args = {'search_form': self.search_form}
        print('schedule_spider spider_args',spider_args)
        return self.scrapyd.schedule(self.project_name, spider_name, **spider_args)

    def check_finished(self):
        return any(self.scrapyd.job_status(project='scraper', job_id=job_id) in ['running', 'pending'] for job_id in self.job_ids)