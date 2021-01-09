# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BlocketJobbSpider(CrawlSpider):
    name = 'blocket_jobb'
    allowed_domains = ['jobb.blocket.se']
    start_urls = ['https://jobb.blocket.se/lediga-jobb-i-hela-sverige/?sp=0']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='item job-item']/div[@class='content']/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//div[@class='ui buttons fluid']/a[last()]"))
    )

    def parse_item(self, response):
        yield {
            'job_headline': response.xpath("//h2[@class='ui header title h1 even-less-padding-bottom']/text()").get(),
            'job_location':response.xpath("normalize-space(//table[@class='ui job-info very compact borderless fixed table']/tbody/tr/td/b[contains(text(), 'Område')]/parent::node()/following-sibling::node()[2]/a/text())").get(),
            'work_catagory': response.xpath("//table[@class='ui job-info very compact borderless fixed table']/tbody/tr/td/b[contains(text(), 'Yrkesroll')]/parent::node()/following-sibling::node()[2]/a/text()").getall(),
            'application_deadline': response.xpath("//table[@class='ui job-info very compact borderless fixed table']/tbody/tr/td/b[contains(text(), 'Sista ansökningsdag')]/parent::node()/following-sibling::node()[2]/text()").get()
        }
