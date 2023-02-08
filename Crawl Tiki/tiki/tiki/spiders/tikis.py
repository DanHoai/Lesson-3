import scrapy


class TikisSpider(scrapy.Spider):
    name = "tikis"
    allowed_domains = ["tiki.vn"]
    start_urls = ["https://tiki.vn/dien-thoai-may-tinh-bang/c1789"]

    def parse(self, response):
        for product in response.css('.product-item'):
            yield {
                'title': product.css('.name h3::text').get(),
                'price': product.css('.price-discount__price::text').get(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
