from _cffi_backend import callback

from scrapy.http import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from zhaoping.items import LiepingItem


class zhilianSpider(CrawlSpider):
    name="lieping"
    allowed_domains = ['www.liepin.com']
    start_urls = ['https://www.liepin.com/zhaopin/?d_sfrom=search_fp_nvbar&init=1']
    def parse(self, response):
        post_nodes = response.css(".job-info>h3>a")
        for post_node in post_nodes:
            post_url = post_node.css("::attr(href)").extract_first("")
            yield Request(url=post_url,  callback=self.parse_companyname)
            # 提取下一页并交给scrapy进行下载
            next_url = response.xpath('//div[@class="pagerbar"]/a').extract()[6]
            if next_url:
                yield Request(post_url, callback=self.parse)

    def parse_companyname(self,response):
        item = LiepingItem()
        next_url = response.css(".next.page-numbers::attr(href)").extract_first("")
        if next_url:
            yield Request(url=response.url, callback=self.parse_companyname)
        # job=response.xpath('//div[@class="title-info"]/text()').extract()
        salary = response.xpath('//p[@class="job-item-title"]/text()').extract()
        position = response.xpath('//p[@class="basic-infor"]/span/a/text()').extract()
        education = response.xpath('//div[@class="job-qualifications"]/span/text()').extract()[0]
        operatinghours = response.xpath('//div[@class="job-qualifications"]/span/text()').extract()[1]
        company = response.xpath('//div[@class="title-info"]/h3/a/text()').extract()
        # image_url = response.xpath("img::attr(src)").extract_first("")
        # article_item["front_image_url"] = [front_image_url]
        # item['job'] = job
        item['salary'] = salary
        item['position'] = position
        item['education'] = education
        item['operatinghours'] = operatinghours
        item['company'] = company
        yield item
