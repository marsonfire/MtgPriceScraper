import scrapy
from csv import writer
from datetime import datetime
from scrapy.crawler import CrawlerProcess

ck = "Card Kingdom"
scg = "Star City Games"
tcg = "Tcg Player Market"
ch = "Cardhoarder"

# region Spiders

# Endurance Card Kingdom 
class EnduranceCardKingdomSpider(scrapy.Spider):
    name = "enduranceCardKingdomSpider"
    start_urls = ['https://www.cardkingdom.com/mtg/modern-horizons-2/endurance']

    def parse(self, response):
        endurance_ck_price = SpiderHelpers.create_list_of_values(ck, response.xpath("//span[@class='stylePrice']/text()").get().strip())
        SpiderHelpers.append_to_csv('endurance', endurance_ck_price)

# Endurance Star City Games
class EnduranceScgSpider(scrapy.Spider):
    name = "enduranceScgSpider"
    start_urls = ['https://starcitygames.com/endurance-sgl-mtg-mh2-157-enn/?sku=SGL-MTG-MH2-157-ENN1']

    def parse(self, response):
        endurance_scg_price = SpiderHelpers.create_list_of_values(scg, response.xpath("//span[@class='price price--withoutTax']/text()").get())
        SpiderHelpers.append_to_csv('endurance', endurance_scg_price)

#Endurance TCG Player and Cardhoarder
class EnduranceGoldfishSpider(scrapy.Spider):
    name = "enduranceGoldfishSpider"
    start_urls = ['https://www.mtggoldfish.com/price/Modern+Horizons+2/Endurance#paper']

    def parse(self, response):
        endurance_tcg_price = SpiderHelpers.create_list_of_values(tcg, str(response.xpath("//span[@class='btn-shop-price']/text()")[2].get()).strip())
        endurance_ch_price = SpiderHelpers.create_list_of_values(ch, str(response.xpath("//span[@class='btn-shop-price']/text()")[4].get()).strip())
        SpiderHelpers.append_to_csv('endurance', endurance_tcg_price)
        SpiderHelpers.append_to_csv('endurance', endurance_ch_price)

# Polluted Delta TCG Player
class PollutedDeltaGoldfishSpider(scrapy.Spider):
    name = "pdGoldfishSpider"
    start_urls = ['https://www.mtggoldfish.com/price/Khans+of+Tarkir/Polluted+Delta#online']

    def parse(self, response):
        pd_tcg_price = SpiderHelpers.create_list_of_values(tcg, str(response.xpath("//span[@class='btn-shop-price']/text()")[3].get()).strip())
        SpiderHelpers.append_to_csv('pollutedDelta', pd_tcg_price)

#Polluted Delta Card Kingom
class PollutedDeltaCardKingdomSpider(scrapy.Spider):
    name = "pdCkSpider"
    start_urls = ['https://www.cardkingdom.com/mtg/khans-of-tarkir/polluted-delta']

    def parse(self, response):
        pd_ck_price = SpiderHelpers.create_list_of_values(ck, response.xpath("//span[@class='stylePrice']/text()").get().strip())
        SpiderHelpers.append_to_csv('pollutedDelta', pd_ck_price)

# Force of Will TCG Player
class ForceOfWillGoldfishSpider(scrapy.Spider):
    name = "fowSpider"
    start_urls = ['https://www.mtggoldfish.com/price/Alliances/Force+of+Will#paper']

    def parse(self, response):
        fow_tcg_price = SpiderHelpers.create_list_of_values(tcg, str(response.xpath("//span[@class='btn-shop-price']/text()")[3].get()).strip())
        SpiderHelpers.append_to_csv('forceOfWill', fow_tcg_price)

# Force of Negation TCG Player
class ForceOfNegationGoldfishSpider(scrapy.Spider):
    name = "fonSpider"
    start_urls = ['https://www.mtggoldfish.com/price/Modern+Horizons/Force+of+Negation#online']

    def parse(self, response):
        fon_tcg_price = SpiderHelpers.create_list_of_values(tcg, str(response.xpath("//span[@class='btn-shop-price']/text()")[3].get()).strip())
        SpiderHelpers.append_to_csv('forceOfNegation', fon_tcg_price)

# Verdant Catacombs Goldfish Spider
class VerdantCatacombsGoldfishSpider(scrapy.Spider):
    name = "vcSpider"
    start_urls = ['https://www.mtggoldfish.com/price/Modern+Horizons+2/Verdant+Catacombs#online']

    def parse(self, response):
        vc_tcg_price = SpiderHelpers.create_list_of_values(tcg, str(response.xpath("//span[@class='btn-shop-price']/text()")[2].get()).strip())
        SpiderHelpers.append_to_csv('verdantCatacombs', vc_tcg_price)

# Sanctum Prelate Spider
class SanctumPrelateGoldfishSpider(scrapy.Spider):
    name = "spSpider"
    start_urls = ['https://www.mtggoldfish.com/price/Treasure+Chest/Sanctum+Prelate#online']

    def parse(self, response):
        sp_ch_price = SpiderHelpers.create_list_of_values(ch, str(response.xpath("//span[@class='btn-shop-price']/text()")[0].get()).strip())
        SpiderHelpers.append_to_csv('sanctumPrelate', sp_ch_price)

# endregion 

# Helper methods to run the spiders
class SpiderHelpers():
    
    # Function to format the new row we will append to the CSV file
    def create_list_of_values(site, xpath):
        return [datetime.now().strftime("%Y-%m-%d %H:%M"), site, xpath] 

    # Open the CSV and append the new row to it
    def append_to_csv(csv_name, new_row):
        # Open file in append mode
        with open("csvData/ " + csv_name + '.csv', 'a+', newline='') as write_obj:
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
        process.crawl(EnduranceGoldfishSpider)
        process.crawl(PollutedDeltaGoldfishSpider)
        process.crawl(PollutedDeltaCardKingdomSpider)
        process.crawl(ForceOfWillGoldfishSpider)
        process.crawl(ForceOfNegationGoldfishSpider)
        process.crawl(VerdantCatacombsGoldfishSpider)
        process.crawl(SanctumPrelateGoldfishSpider)
        process.start()