import scrapy
from csv import writer
from datetime import datetime
from scrapy.crawler import CrawlerProcess

class EnduranceTcgPlayerSpider(scrapy.Spider):
    name = "enduranceTcgPlayerSpider"
    start_urls = ['https://shop.tcgplayer.com/magic/modern-horizons-2/endurance?xid=a5beae949-191c-4d02-9309-692dc57d1b5a']

    def parse(self, response):
        enduranceTcgPlayerPrice = [datetime.now().strftime("%Y-%m-%d %H:%M"), response.css('.price-point__data::text').get()]
        # Open file in append mode
        with open('test.csv', 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow(enduranceTcgPlayerPrice)

class EnduranceTcgPlayerRunner():
    def run_spider():
        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })
        process.crawl(EnduranceTcgPlayerSpider)
        process.start() # the script will block here until the crawling is finished



    

     