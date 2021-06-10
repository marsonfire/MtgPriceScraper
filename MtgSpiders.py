import scrapy
from csv import writer
from datetime import datetime
from scrapy.crawler import CrawlerProcess

# region Endurance Spiders

# Endurance Card Kingdom 
class EnduranceCardKingdomSpider(scrapy.Spider):
    name = "enduranceCardKingdomSpider"
    start_urls = ['https://www.cardkingdom.com/mtg/modern-horizons-2/endurance']

    def parse(self, response):
        endurance_ck_price = SpiderHelpers.create_list_of_values('Card Kingdom', response.xpath("//span[@class='stylePrice']/text()").get().strip())
        SpiderHelpers.append_to_csv(endurance_ck_price)

# Endurance Star City Games
class EnduranceScgSpider(scrapy.Spider):
    name = "enduranceScgSpider"
    start_urls = ['https://starcitygames.com/endurance-sgl-mtg-mh2-157-enn/?sku=SGL-MTG-MH2-157-ENN1']

    def parse(self, response):
        endurance_scg_price = SpiderHelpers.create_list_of_values('Star City Games', response.xpath("//span[@class='price price--withoutTax']/text()").get())
        SpiderHelpers.append_to_csv(endurance_scg_price)

# endregion 

# Helper methods to run the spiders
class SpiderHelpers():
    
    # Function to format the new row we will append to the CSV file
    def create_list_of_values(site, xpath):
        return [datetime.now().strftime("%Y-%m-%d %H:%M"), site, xpath] 

    # Open the CSV and append the new row to it
    def append_to_csv(new_row):
        # Open file in append mode
        with open('test.csv', 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow(new_row)

    # Function to run the spiders 
    def run_spiders():
        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })
        process.crawl(EnduranceCardKingdomSpider)
        process.crawl(EnduranceScgSpider)
        process.start()