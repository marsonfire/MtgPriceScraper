import scrapy
from csv import writer
from datetime import datetime
from scrapy.crawler import CrawlerProcess

class EnduranceCardKingdomSpider(scrapy.Spider):
    name = "enduranceCardKingdomSpider"
    start_urls = ['https://www.cardkingdom.com/mtg/modern-horizons-2/endurance']

    def parse(self, response):
        endurance_ck_price = [datetime.now().strftime("%Y-%m-%d %H:%M"), response.xpath("//span[@class='stylePrice']/text()").get().strip()]
        # Open file in append mode
        with open('test.csv', 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow(endurance_ck_price)

class EnduranceCardKingdomRunner():
    def run_spider():
        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })
        process.crawl(EnduranceCardKingdomSpider)



    

     