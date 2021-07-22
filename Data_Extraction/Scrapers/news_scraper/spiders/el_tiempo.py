import scrapy


class ElTiempoSpider(scrapy.Spider):
    name = 'el_tiempo'
    allowed_domains = ['https://www.eltiempo.com/']
    start_urls = ['https://www.eltiempo.com//']

    def parse(self, response):
        pass
