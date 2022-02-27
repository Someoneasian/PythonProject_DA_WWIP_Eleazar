import scrapy

# Create a spider to process the response and return scraped item
class NewSpider(scrapy.Spider):
    name="new_spider"
    start_urls = ["http://192.168.1.3/spicyx/"]
    def parse(self, response):
        for every_response in response.css("img"):
            yield{
                "Image Link is": every_response.xpath('@src').extract_first(),
            }

#To Recurse next page
        Page_selector = '.next a ::attr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )