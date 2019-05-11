import scrapy
from ..items import MercadoItem

class MercadoSpider(scrapy.Spider):
    name='Wolf'
    
    def start_requests(self):
        for i in range(0,3):
            url='https://celulares.mercadolibre.com.mx/_Desde_'+str(i*50+1)
            yield scrapy.Request(url=url, callback=self.parse,dont_filter=True,priority=i)

    def parse(self,response):
        items=MercadoItem()
        all_products=response.css('li.results-item')
        for product in all_products:
            Nombre= product.css('span.main-title::text').extract()
            Ventas=product.css('div.item__condition::text').extract()
            Precio= product.css('span.price__fraction::text').extract()
            Precio_Original=product.css('span.price-old del::text').extract()
            #Filter Original Price
            Precio_Original=[word.replace(u'$\xa0', '') for word in Precio_Original]

            items['Nombre']=Nombre
            items['Ventas']=Ventas
            items['Precio']=Precio    
            items['Precio_Original']=Precio_Original
            yield items

    