import scrapy


class QuotesSpider(scrapy.Spider):
    name = "get_links"
    start_urls = [
        'http://www.gallito.com.uy/inmuebles/casas'
    ]

    def parse(self, response):
        for next_page in response.css('img.img-seva::attr(alt)'):
            if next_page is not None:
                yield response.follow(href, self.parse_house)
                
    def parse_house(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        yield {
            
            'price': extract_with_css('p.precio::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        }
        
