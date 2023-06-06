# Scrapy settings for scraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import sys
from django.core.wsgi import get_wsgi_application
import os
import socket
# from dotenv import load_dotenv
#
# load_dotenv('/home/janek/PycharmProjects/property_scraper_api/.env')

# sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".."))
# sys.path.append('../')

sys.path.append(os.path.dirname(os.path.abspath('.')))

# sys.path.append('/home/janek/python/property_scraper')
# sys.path.append(os.path.dirname(os.path.abspath('.')))

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(os.path.join(BASE_DIR, "properties_scrapping"))
ipaddress = socket.gethostbyname(socket.gethostname())
if ipaddress == '127.0.1.1' or ipaddress == '192.168.0.46':
    DJANGO_SETTINGS_MODULE = 'properties_scrapping.settings.local'
else:
    DJANGO_SETTINGS_MODULE = 'properties_scrapping.settings.production'
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'properties_scrapping.settings')
os.environ['DJANGO_SETTINGS_MODULE'] = DJANGO_SETTINGS_MODULE
application = get_wsgi_application()  # musi być po ustawieniu DJANGO_SETTINGS_MODULE

# import django
# django.setup()

# SCRAPYD_URL = os.environ.get('SCRAPYD_URL')
# print(';;;;;;;;;;;;;;;;;;;SCRAPYD_URL',SCRAPYD_URL)
# SCRAPYD_PROJECT = os.environ.get('SCRAPYD_PROJECT')

# LOG_ENABLED=True
# LOG_FILE="scraper/logs/scraper.log"

BOT_NAME = "scraper"

SPIDER_MODULES = ["scraper.spiders"]
NEWSPIDER_MODULE = "scraper.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "scraper (+http://www.yourdomain.com)"
# USER_AGENT='my-cool-project (http://example.com)'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'
# USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_3 like Mac OS X)'
ITEM_PIPELINES = {
    #    'scraper.scraper.pipelines.PropertyStatusPipeline': 100,
    #    'scraper.scraper.pipelines.PropertyPricePipeline': 200,
    #    'scraper.scraper.pipelines.ConvertNumPipeline': 300,
    # 'scraper.pipelines.FieldValidationPipeline': 400,
    'scraper.pipelines.ScraperPipeline': 300,
}
# Obey robots.txt rules
# ROBOTSTXT_OBEY = True
ROBOTSTXT_OBEY = False

# DOWNLOAD_HANDLERS = {
#     "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
#     "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
# }
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 6
DOWNLOAD_DELAY = 0.25
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# Splash Server Endpoint
# SPLASH_URL = 'http://localhost:8050'

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
# #    "scraper.middlewares.ScraperSpiderMiddleware": 543,
#     'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
# #    "scraper.middlewares.ScraperDownloaderMiddleware": 543,
#     'scrapy_splash.SplashCookiesMiddleware': 723,
#     'scrapy_splash.SplashMiddleware': 725,
#     'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
# }

# Define the Splash DupeFilter
# DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    "scraper.pipelines.ScraperPipeline": 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"
# HTTPCACHE_STORAGE = "scrapy_splash.splash_request_fingerprint"
# HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
# Set settings whose default value is deprecated to a future-proof value
# REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
# DOWNLOAD_HANDLERS = {
#     "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
#     "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
# }


TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
# PLAYWRIGHT_BROWSER_TYPE = "firefox"
