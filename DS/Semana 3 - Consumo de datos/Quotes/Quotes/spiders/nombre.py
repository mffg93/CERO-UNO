import scrapy
from ..items import LaItem

class QuoteSpider(scrapy.Spider):
    name = 'Quote'
    start_urls =  ["http://quotes.toscrape.com/page/"+str(i)+'/' for i in range(1,3)]

    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(u, callback=self.parse,
                                    dont_filter=True)

    def parse(self,response):
        items=LaItem()
        all_div_quotes=response.css('div.quote')
        for quotes in all_div_quotes:
            text= quotes.css('span.text::text').extract()
            author= quotes.css('.author::text').extract()
            tags= quotes.css('.tag::text').extract()

            items['text']=text
            items['author']=author
            items['tags']=tags            
            yield items