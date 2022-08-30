import scrapy
from wonderland.items import WonderlandItem

class WonderSpider(scrapy.Spider):
    name = 'wonder'
    #allowed_domains = ['www.baidu.com']
    start_urls = ['https://qiushibaike.lofter.com/']

    def parse(self, response):
        div_list = response.xpath('/html/body/div/div[2]/div[1]/div')
        for div in div_list:
            time = div.xpath('./div[2]/div[1]/a/text()').extract()
            content = div.xpath('./div[1]/div/div//text()').extract()
            content = ''.join(content)#将列表中的字符串拿出
            print(time,content)
            item = WonderlandItem()
            item['date'] = time
            item['content'] = content

            yield item
