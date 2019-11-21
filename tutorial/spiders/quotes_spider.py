import scrapy
from tutorial.items import TutorialItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/',
    ]
            
    def parse(self, response):

        items = TutorialItem()

        for quote in response.css('div.quote'):

            items['title'] = quote.css('span.text::text').get()
            items['author'] = quote.css('small.author::text').get()
            items['tags'] = quote.css('div.tags a.tag::text').getall()

            yield items
            # yield {
            #     'Title': quote.css('span.text::text').get()[1:-1],
            #     'author': quote.css('small.author::text').get(),
            #     'tags': quote.css('div.tags a.tag::text').getall(),
            # }

        # next_page = response.css('li.next a::attr(href)').get()
        # print(next_page,"===================================================================================")
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)
        