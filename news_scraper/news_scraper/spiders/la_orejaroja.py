import scrapy
#import w3lib.html


class LaOrejarojaSpider(scrapy.Spider):
    name = 'la_orejaroja'
    allowed_domains = ['www.laorejaroja.com/']
    start_urls = ['http://www.laorejaroja.com//']

    def parse(self, response):
        return {
            "title": response.xpath('//div[@class="title"]/h3/text()').get(),
            #"content": w3lib.html.remove_tags(response.xpath('//div[@class="excerpt"]/p/text()').getall())
            "content": response.xpath('//div[@class="excerpt"]/p/text()').getall()
        }

    

