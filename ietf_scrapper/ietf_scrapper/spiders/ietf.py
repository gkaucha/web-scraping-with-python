import scrapy
import w3lib.html

class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        
        return {
            'title': response.xpath('//meta[@name="creator"]/@content').get(),
            'description': response.xpath('//meta[@name="DC.Description.Abstract"]/@content').get(),
            'author': response.xpath('//meta[@name="DC.Creator"]/@content').get(),
            'date': response.xpath('//meta[@name="DC.Date.Issued"]/@content').get(),
            'rfc_number': response.xpath('//span[@class="rfc-no"]/text()').get(),
            'company':response.xpath('//span[@class="author-company"]/text()').get(),
            'address':response.xpath('//span[@class="address"]/text()').get(),
            'text': w3lib.html.remove_tags(response.xpath('//div[@class="text"]').get()),
            'headings':response.xpath('//span[@class="subheading"]/text()').getall(),
            # title = response.css('span.title::text').get()

        }
