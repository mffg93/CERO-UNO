import scrapy
from ..items import PalacioItem

class PalacioSpider(scrapy.Spider):
    name='Palace'
    

    def start_requests(self):
        for i in range(1,4):
            url='https://www.elpalaciodehierro.com/lujo/mujer/accesorios/bolsos.html?p='+str(i)
            yield scrapy.Request(url=url, callback=self.parse,dont_filter=True,priority=i)

    
    def parse(self,response):
        items=PalacioItem()
        all_products=response.css('div.jbb-list-item')
        
        for product in all_products:
            Marca= product.css('p.ls-grid-title::text').extract()
            Marca=[palabra.strip() for palabra in Marca]
            Producto= product.css('p.jbb-list-item-description span::attr(title)').extract()
            Precio= product.css('span.price::text').extract()
            Precio=[word.replace(u'\xa0', '') for word in Precio]

            items['Marca']=Marca
            items['Producto']=Producto
            items['Precio']=Precio      
            yield items
