import scrapy
from csv import writer
from datetime import datetime

#https://towardsdatascience.com/tutorial-scrape-100-headlines-in-seconds-with-23-lines-of-python-14047deb1a98
#https://towardsdatascience.com/web-scraping-with-scrapy-8071fd627051

enduranceTcgPlayerPrice = "$0"

class EnduranceTcgPlayer(scrapy.Spider):
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

     