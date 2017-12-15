from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.item import Item, Field


class MyItem(Item):
    url = Field()


class QuotesSpider(CrawlSpider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    rules = (Rule(LxmlLinkExtractor(allow_domains=allowed_domains), callback='parse_obj', follow=True),)

    def parse_obj(self, response):
        item = MyItem()
        item['url'] = []

        for link in LxmlLinkExtractor(allow_domains=self.allowed_domains, deny=()).extract_links(response):
            item['url'].append(link.url.rstrip('/'))

        yield {
            'url': response.url.rstrip('/'),
            'items': item['url']
        }