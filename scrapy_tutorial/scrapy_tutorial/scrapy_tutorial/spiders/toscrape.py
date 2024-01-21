import scrapy


class ToscrapeSpider(scrapy.Spider):
    name = "toscrape"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        pass
