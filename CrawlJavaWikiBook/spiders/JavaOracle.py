from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from CrawlJavaWikiBook.items import CrawljavawikibookItem


class JavaOracle(CrawlSpider):
    name = "JavaOracle"  # Spider name
    allowed_domains = ["docs.oracle.com"]  # Which (sub-)domains shall be scraped?
    start_urls = ["https://docs.oracle.com/javase/tutorial"]  # Start with this one
    global x
    x = 0

    # Follow any link scrapy finds (that is allowed and matches the patterns).
    rules = [Rule(LinkExtractor(allow=("https://docs.oracle.com/javase/tutorial")), callback='parse_item',
            follow=True)]

    def parse_item(self, response):
        items = CrawljavawikibookItem()
        selector = Selector(response)
        posttext_selector_str = '//div[@id="PageContent"]'
        post = ''.join(selector.xpath(posttext_selector_str).extract())

        global x
        x = x+1
        items['id'] = str(x)
        items['url'] = response.url
        items['content'] = post

        return items