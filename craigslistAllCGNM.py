import scrapy

class QuotesSpider(scrapy.Spider):
    name = "craigslistAllCGNM"
    start_urls = [
        'https://losangeles.craigslist.org/search/lac/cpg?is_paid=all'
    ]

    print '---------------------- START --------------------'

    def parse(self, response):
        for resultrow in response.css('li.result-row'):
            yield {
                'title': resultrow.css('a.result-title::text').extract_first(),
                'date': resultrow.css('time.result-date::text').extract_first(),
                'location': resultrow.css('span.result-hood::text').extract_first(),
            }

        next_page = response.css('a.button::attr(href)').extract_first()
        print '---------------------- DONE --------------------'
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
