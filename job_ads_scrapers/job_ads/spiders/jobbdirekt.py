# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class JobbdirektSpider(CrawlSpider):
    name = 'jobbdirekt'
    allowed_domains = ['jobbdirekt.se']
    start_urls = ['https://jobbdirekt.se/sok/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//li[contains(@class, 'position clear position')]/div/h2/span/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//div[@class='paging']/div/div/a[contains(text(), 'Nästa')]"))
    )

    def parse_item(self, response):
        yield {
            'job_headline': response.xpath("//div[@class='position']/h1/text()").get(),
            'application_details': response.xpath("normalize-space(//div[@class='meta']/p[1]/text())").get(),
            'work_category': response.xpath("//div[@class='meta']/p[2]/a/text()").getall()
        }

# 'duration':response.xpath("normalize-space(//div[@class='subtext']/time/text())").get(),
