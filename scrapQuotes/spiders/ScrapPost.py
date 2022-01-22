import scrapy

class ScrapeQuotes(scrapy.Spider):
    #class name
    name = 'quotes'    

    start_urls = [
        'https://www.goodreads.com/quotes/'
    ]
    
    def parse(self, response):
        #extracting details using css selector
        for item in response.css('.quote'):

            quote = item.css('.quoteText::text').get()
            author = item.css('.authorOrTitle::text').get()
        
            #yielding the extracted details creating a dict
            yield {
                'Quote': quote,
                'Author':author
            }

        #parsing next pages
        next_page = response.css('.next_page::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse)
