import scrapy


class LinkedinSpider(scrapy.Spider):
    name = "linkedin"
    allowed_domains = ["linkedin.com"]
    start_urls = [
        "https://www.linkedin.com/company/imagine-careers",
    ]

    def parse(self, response):
        description = response.xpath("//*[@id='content']/div[2]/div[1]/p").extract()
        title = response.xpath("//*[@id='body']/div[2]/div[1]/div[1]/div/h1/span").extract()
        print(title, description)


def start_reqests():
    yield Request('http://checkip.dyndns.org/', callback=self.check_ip)
    # yield other requests from start_urls here if needed


def check_ip(self, response):
    pub_ip = response.xpath('//body/text()').re('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')[0]
    print "My public IP is: " + pub_ip
