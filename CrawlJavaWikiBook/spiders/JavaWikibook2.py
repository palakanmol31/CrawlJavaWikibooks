from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from CrawlJavaWikiBook.items import CrawljavawikibookItem

class JavaWikibook2(CrawlSpider):
    name = "JavaWikibook2"
    allowed_domains = ["wikibooks.org"]
    start_urls = ["https://en.wikibooks.org/wiki/Java_Programming"]
    global x
    x = 0

    rules = [Rule(LinkExtractor(allow=("https://en.wikibooks.org/wiki/Java_Programming/"), deny=("https://en.wikibooks.org/wiki/Java_Programming/Print_version")), callback='parse_item',
            follow=True)]

    def parse_item(self, response):

        selector = Selector(response)

        headingSelector = '//h2/span[@class="mw-headline"]//text()'
        heading = selector.xpath(headingSelector).extract()

        if len(heading) > 0 :
            for i in range(0,len(heading)-1):
                items = CrawljavawikibookItem()
                contentSelector ="//*[preceding-sibling::h2[span='"+ heading[i] + "'] and following-sibling::h2[span='"+ heading[i+1]+ "']]//text()"
                content = ''.join(selector.xpath(contentSelector).extract())

                htmlSelector = "//*[preceding-sibling::h2[span='" + heading[i] + "'] and following-sibling::h2[span='" + heading[i + 1] + "']]"
                html = ''.join(selector.xpath(htmlSelector).extract())

                codeSelector = "//table[preceding-sibling::h2[span='" + heading[i] + "'] and following-sibling::h2[span='" + heading[i + 1] + "']]"
                code  = ''.join(selector.xpath(codeSelector).extract())

                withoutTableSelector = "//*[preceding-sibling::h2[span='"+ heading[i]+ "'] and following-sibling::h2[span='"+ heading[i+1] +"'] and not(self::table)]"
                withoutTable = ''.join(selector.xpath(withoutTableSelector).extract())

                global x
                x = x + 1
                items['id'] = str(x)
                items['url'] = response.url
                items['heading'] = heading[i]
                items['html'] = html
                items['content'] = content
                items['code'] = code
                items['removeCode'] = withoutTable
                print response.url + "    " + heading[i]
                yield items
       # else :



