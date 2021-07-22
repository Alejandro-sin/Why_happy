import scrapy
#import w3lib.html


class LaOrejarojaSpider(scrapy.Spider):
    name = 'la_orejaroja'
    allowed_domains = ['www.laorejaroja.com/']
    start_urls = ['http://www.laorejaroja.com//']

    def parse(self, response):
        for news in response.xpath('//div[@class="main-content"]'):
            yield {"title": news.xpath('//div[@class="title"]/h3/text()').get(),
                #"content": w3lib.html.remove_tags(response.xpath('//div[@class="excerpt"]/p/text()').getall())
                "content": news.xpath('//div[@class="excerpt"]/p/text()').get(),
                #"url": news.xpath('//a').getall(),
            }
            


        
