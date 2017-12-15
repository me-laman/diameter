from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.item import Item, Field


class MyItem(Item):
    url = Field()


class QuotesSpider(CrawlSpider):
    name = "wiki"
    allowed_domains = ["en.wikipedia.org"]
    deny = [
        '#',
        'index.php',
        'Wikipedia:',
        'Portal:',
        'Special:',
        'Help:',
        'Talk:',
        'File:',
        'User:',
        'Template:',
        'Category:',
        '/Main_Page'
    ]
    start_urls = [
        'https://en.wikipedia.org',
    ]

    rules = (Rule(LxmlLinkExtractor(allow_domains=allowed_domains, deny=deny), callback='parse_obj', follow=True),)

    def parse_obj(self, response):
        item = MyItem()
        item['url'] = []

        for link in LxmlLinkExtractor(allow_domains=self.allowed_domains, deny=self.deny).extract_links(response):
            item['url'].append(link.url.rstrip('/'))

        yield {
            'url': response.url.rstrip('/'),
            'items': item['url']
        }