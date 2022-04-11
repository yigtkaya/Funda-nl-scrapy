import scrapy
from scrapy.loader import ItemLoader
from ..items import FundanlItem


class Funl(scrapy.Spider):
    name = "demo"
    start_urls = [
        'https://www.funda.nl/en/koop/heel-nederland/p1/',
    ]
    allowed_url = "https://www.funda.nl"

    def parse(self, response):

        #data scrape and parsing
        full_search_result = response.css("ol.search-results li.search-result")

        for listed in full_search_result:
            il = ItemLoader(item=FundanlItem(), selector=listed)

            il.add_css("urls", "div.search-result__header-title-col a::attr(href)")
            il.add_css("price", "div.search-result-info-price span::text")
            il.add_css("m2", "ul.search-result-kenmerken span::text")
            il.add_css("address", "h4.search-result__header-subtitle.fd-m-none::text")
            il.add_css("roomNumber", "ul.search-result-kenmerken li::text")

            yield il.load_item()

        #pagination
        next_page = response.css('[rel=next]::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


