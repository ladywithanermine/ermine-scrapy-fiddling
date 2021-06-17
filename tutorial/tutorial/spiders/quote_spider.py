import scrapy


class QuotesSpider(scrapy.Spider):
    """
    Sample spider from the Scrapy tutorial.
    In order to run it, execute scrapy crawl quotes
    """

    # The name of the spider must be unique within the project. All spiders go into the /spiders folder
    name = "quotes"

    # Either define a start_requests method or the following variable (commented as a reminder)
    # start_urls = [
    #     'http://quotes.toscrape.com/page/1/',
    #     'http://quotes.toscrape.com/page/2/',
    # ]

    def start_requests(self):
        """
        Generator that returns an iterable of Requests that the spider will crawl from
        """
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
        Scrapy's default callback method
        """
        for quote in response.css("div.quote"):
            yield {
                'text' : quote.css("span.text::text").get(),
                'author' : quote.css("small.author::text").get(),
                'tags' : quote.css("div.tags a.tag::text").getall()
            }

        yield from response.follow_all(css='ul.pager a', callback=self.parse)