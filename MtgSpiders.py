import scrapy
from csv import writer
from datetime import datetime
from scrapy.crawler import CrawlerProcess
import pandas as pd

TCG = "Tcg Player Market"
CH = "Cardhoarder"
GOLDFISH_XPATH = "//span[@class='btn-shop-price']/text()"
sig_changes = ""

# region Spiders

#Endurance TCG Player and Cardhoarder
class EnduranceGoldfishSpider(scrapy.Spider):
    name = "enduranceGoldfishSpider"
    start_urls = ['https://www.mtggoldfish.com/price/Modern+Horizons+2/Endurance#online']

    def parse(self, response):
        endurance_tcg_price = SpiderHelpers.create_list_of_values(TCG, str(response.xpath(GOLDFISH_XPATH)[1].get()).strip())
        endurance_ch_price = SpiderHelpers.create_list_of_values(CH, str(response.xpath(GOLDFISH_XPATH)[4].get()).strip())
        SpiderHelpers.append_to_csv('enduranceTcg', endurance_tcg_price)
        SummaryFile.get_percent_change('enduranceTcg')
        SpiderHelpers.append_to_csv('enduranceCh', endurance_ch_price)
        SummaryFile.get_percent_change('enduranceCh')

# Polluted Delta TCG Player
class PollutedDeltaGoldfishSpider(scrapy.Spider):
    name = "pdGoldfishSpider"
    start_urls = ['https://www.mtggoldfish.com/price/Khans+of+Tarkir/Polluted+Delta#online']

    def parse(self, response):
        pd_tcg_price = SpiderHelpers.create_list_of_values(TCG, str(response.xpath(GOLDFISH_XPATH)[2].get()).strip())
        SpiderHelpers.append_to_csv('pollutedDelta', pd_tcg_price)
        SummaryFile.get_percent_change('pollutedDelta')

# Force of Will TCG Player
class ForceOfWillGoldfishSpider(scrapy.Spider):
    name = "fowSpider"
    start_urls = ['https://www.mtggoldfish.com/price/Alliances/Force+of+Will#paper']

    def parse(self, response):
        fow_tcg_price = SpiderHelpers.create_list_of_values(TCG, str(response.xpath(GOLDFISH_XPATH)[2].get()).strip())
        SpiderHelpers.append_to_csv('forceOfWillTcg', fow_tcg_price)
        SummaryFile.get_percent_change('forceOfWillTcg')

#Force of will Cardhoarder
class ForceOfWillChGoldfishSpider(scrapy.Spider):
    name = "fowChSpider"
    start_urls = ['https://www.mtggoldfish.com/price/Vintage+Masters/Force+of+Will#online']

    def parse(self, response):
        ch_price = SpiderHelpers.create_list_of_values(CH, str(response.xpath(GOLDFISH_XPATH)[0].get()).strip())
        SpiderHelpers.append_to_csv('forceOfWillCh', ch_price)
        SummaryFile.get_percent_change('forceOfWillCh')

# Force of Negation TCG Player
class ForceOfNegationGoldfishSpider(scrapy.Spider):
    name = "fonSpider"
    start_urls = ['https://www.mtggoldfish.com/price/Modern+Horizons/Force+of+Negation#online']

    def parse(self, response):
        fon_tcg_price = SpiderHelpers.create_list_of_values(TCG, str(response.xpath(GOLDFISH_XPATH)[2].get()).strip())
        SpiderHelpers.append_to_csv('forceOfNegation', fon_tcg_price)
        SummaryFile.get_percent_change('forceOfNegation')

# Verdant Catacombs Goldfish Spider
class VerdantCatacombsGoldfishSpider(scrapy.Spider):
    name = "vcSpider"
    start_urls = ['https://www.mtggoldfish.com/price/Modern+Horizons+2/Verdant+Catacombs#online']

    def parse(self, response):
        vc_tcg_price = SpiderHelpers.create_list_of_values(TCG, str(response.xpath(GOLDFISH_XPATH)[1].get()).strip())
        SpiderHelpers.append_to_csv('verdantCatacombs', vc_tcg_price)
        SummaryFile.get_percent_change('verdantCatacombs')

# Sanctum Prelate Spider
class SanctumPrelateGoldfishSpider(scrapy.Spider):
    name = "spSpider"
    start_urls = ['https://www.mtggoldfish.com/price/Treasure+Chest/Sanctum+Prelate#online']

    def parse(self, response):
        sp_ch_price = SpiderHelpers.create_list_of_values(CH, str(response.xpath(GOLDFISH_XPATH)[0].get()).strip())
        SpiderHelpers.append_to_csv('sanctumPrelate', sp_ch_price)
        SummaryFile.get_percent_change('sanctumPrelate')

#Prismatic Ending Spider
class PrismaticEndingGoldfishSpider(scrapy.Spider):
    name = "peSpider"
    start_urls = ['https://www.mtggoldfish.com/price/Modern+Horizons+2/Prismatic+Ending#online']

    def parse(self, response):
        pe_tcg_price = SpiderHelpers.create_list_of_values(TCG, str(response.xpath(GOLDFISH_XPATH)[2].get()).strip()) 
        pe_ch_price = SpiderHelpers.create_list_of_values(CH, str(response.xpath(GOLDFISH_XPATH)[4].get()).strip())
        SpiderHelpers.append_to_csv('prismaticEnding', pe_tcg_price)
        SpiderHelpers.append_to_csv('prismaticEnding', pe_ch_price)

#Grist the hunger tide spider
class GristGoldfishSpider(scrapy.Spider):
    name = "gristSpider"
    start_urls = ['https://www.mtggoldfish.com/price/Modern+Horizons+2/Grist+the+Hunger+Tide#online']

    def parse(self, response):
        grist_tcg_price = SpiderHelpers.create_list_of_values(TCG, str(response.xpath(GOLDFISH_XPATH)[1].get()).strip()) 
        grist_ch_price = SpiderHelpers.create_list_of_values(CH, str(response.xpath(GOLDFISH_XPATH)[3].get()).strip())
        SpiderHelpers.append_to_csv('gristTcg', grist_tcg_price)
        SummaryFile.get_percent_change('gristTcg')
        SpiderHelpers.append_to_csv('gristCh', grist_ch_price)
        SummaryFile.get_percent_change('gristCh')

#brazen borrower
class BrazenGoldfishSpider(scrapy.Spider):
    name = "brazenSpider"
    start_urls = ['https://www.mtggoldfish.com/price/Throne+of+Eldraine/Brazen+Borrower#online']

    def parse(self, response):
        ch_price = SpiderHelpers.create_list_of_values(CH, str(response.xpath(GOLDFISH_XPATH)[5].get()).strip())
        SpiderHelpers.append_to_csv('brazenBorrower', ch_price)
        SummaryFile.get_percent_change('brazenBorrower')

#fiery islet
class FieryIsletGoldfishSpider(scrapy.Spider):
    name = "fieryIsletSpider"
    start_urls = ['https://www.mtggoldfish.com/price/Modern+Horizons/Fiery+Islet#online']

    def parse(self, response):
        ch_price = SpiderHelpers.create_list_of_values(CH, str(response.xpath(GOLDFISH_XPATH)[5].get()).strip())
        SpiderHelpers.append_to_csv('fieryIslet', ch_price)
        SummaryFile.get_percent_change('fieryIslet')

#blackcleave cliffs
class BlackcleaveGoldfishSpider(scrapy.Spider):
    name = "blackcleaveSpider"
    start_urls = ['https://www.mtggoldfish.com/price/Scars+of+Mirrodin/Blackcleave+Cliffs#online']

    def parse(self, response):
        ch_price = SpiderHelpers.create_list_of_values(CH, str(response.xpath(GOLDFISH_XPATH)[3].get()).strip())
        SpiderHelpers.append_to_csv('blackcleaveCliffs', ch_price)
        SummaryFile.get_percent_change('blackcleaveCliffs')

#klothys
class KlothysGoldfishSpider(scrapy.Spider):
    name = "klothysSpider"
    start_urls = ['https://www.mtggoldfish.com/price/Theros+Beyond+Death/Klothys+God+of+Destiny#online']

    def parse(self, response):
        ch_price = SpiderHelpers.create_list_of_values(CH, str(response.xpath(GOLDFISH_XPATH)[5].get()).strip())
        SpiderHelpers.append_to_csv('klothys', ch_price)

#murktide regent
class MurktideGoldfishSpider(scrapy.Spider):
    name = "murkSpider"
    start_urls = ['https://www.mtggoldfish.com/price/Modern+Horizons+2/Murktide+Regent#online']

    def parse(self, response):
        ch_price = SpiderHelpers.create_list_of_values(CH, str(response.xpath(GOLDFISH_XPATH)[3].get()).strip())
        SpiderHelpers.append_to_csv('murktide', ch_price)
        SummaryFile.get_percent_change('murktide')

#spirebluff canal
class SpirebluffCanalGoldfishSpider(scrapy.Spider):
    name = "spirebluffSpider"
    start_urls = ['https://www.mtggoldfish.com/price/Kaladesh/Spirebluff+Canal#online']

    def parse(self, response):
        ch_price = SpiderHelpers.create_list_of_values(CH, str(response.xpath(GOLDFISH_XPATH)[4].get()).strip())
        SpiderHelpers.append_to_csv('spirebluffCanal', ch_price)
        SummaryFile.get_percent_change('spirebluffCanal')

#dauthi voidwalker
class DauthiGoldfishSpider(scrapy.Spider):
    name = "dauthiSpider"
    start_urls = ['https://www.mtggoldfish.com/price/Modern+Horizons+2/Dauthi+Voidwalker#online']

    def parse(self, response):
        ch_price = SpiderHelpers.create_list_of_values(CH, str(response.xpath(GOLDFISH_XPATH)[4].get()).strip())
        SpiderHelpers.append_to_csv('dauthi', ch_price)
        SummaryFile.get_percent_change('dauthi')

#misty rainforest
class MistyRainforestGoldfishSpider(scrapy.Spider):
    name = "mistySpider"
    start_urls = ['https://www.mtggoldfish.com/price/Modern+Horizons+2/Misty+Rainforest#online']

    def parse(self, response):
        tcg_price = SpiderHelpers.create_list_of_values(TCG, str(response.xpath(GOLDFISH_XPATH)[1].get()).strip())
        ch_price = SpiderHelpers.create_list_of_values(CH, str(response.xpath(GOLDFISH_XPATH)[3].get()).strip())
        SpiderHelpers.append_to_csv('mistyRainforestTcg', tcg_price)
        SummaryFile.get_percent_change('mistyRainforestTcg')
        SpiderHelpers.append_to_csv('mistyRainforestCh', ch_price)
        SummaryFile.get_percent_change('mistyRainforestCh')

class AlurenGoldfishSpider(scrapy.Spider):
    name = "alurenSpider"
    start_urls = ['https://www.mtggoldfish.com/price/Tempest/Aluren#online']

    def parse(self, response):
        ch_price = SpiderHelpers.create_list_of_values(CH, str(response.xpath(GOLDFISH_XPATH)[4].get()).strip())
        SpiderHelpers.append_to_csv('aluren', ch_price)
        SummaryFile.get_percent_change('aluren')

class TashaGoldfishSpider(scrapy.Spider):
    name = "tashaSpider"
    start_urls = ['https://www.mtggoldfish.com/price/Adventures+in+the+Forgotten+Realms/Tashas+Hideous+Laughter#online']

    def parse(self, response):
        ch_price = SpiderHelpers.create_list_of_values(CH, str(response.xpath(GOLDFISH_XPATH)[3].get()).strip())
        SpiderHelpers.append_to_csv('tasha', ch_price)
        SummaryFile.get_percent_change('tasha')

class TreasureGoldfishSpider(scrapy.Spider):
    name = "treasureSpider"
    start_urls = ['https://www.mtggoldfish.com/price/Adventures+in+the+Forgotten+Realms/Treasure+Vault#online']

    def parse(self, response):
        ch_price = SpiderHelpers.create_list_of_values(CH, str(response.xpath(GOLDFISH_XPATH)[3].get()).strip())
        SpiderHelpers.append_to_csv('treasureVault', ch_price)
        SummaryFile.get_percent_change('treasureVault')

class MentorGoldfishSpider(scrapy.Spider):
    name = "mentorSpider"
    start_urls = ['https://www.mtggoldfish.com/price/Fate+Reforged/Monastery+Mentor#online']

    def parse(self, response):
        ch_price = SpiderHelpers.create_list_of_values(CH, str(response.xpath(GOLDFISH_XPATH)[4].get()).strip())
        SpiderHelpers.append_to_csv('mentor', ch_price)
        SummaryFile.get_percent_change('mentor')
# endregion 

#Create Summary File
class SummaryFile():
    def get_percent_change(csv):

        #read in the csv and get the 2 most recent values
        list_values = pd.read_csv("/home/awmarsden/Desktop/MtgPriceScraper/csvData/" + csv + '.csv').values.tolist()
        last_value = list_values[-1][2]
        second_to_last = list_values[-2][2]

        #get the values for Cardhoarder
        if("tix" in last_value and "tix" in second_to_last):
            tix_index = last_value.index('tix')
            last_value = float(last_value[:tix_index].strip())
            tix_index = second_to_last.index('tix')
            second_to_last = float(second_to_last[:tix_index].strip())
        elif("$" in last_value and "$" in second_to_last):
            index = last_value.index('$')
            last_value = float(last_value[index + 1:].strip())
            index = second_to_last.index('$')
            second_to_last = float(second_to_last[index + 1:].strip())
        #get the percent change between the 2 most recent values
        percent_change = ((last_value - second_to_last)/second_to_last) * 100

        if(percent_change >= 5 or percent_change <= -5):
            global sig_changes
            sig_changes = sig_changes + csv + " percent change " + str(percent_change) + ". Was " + str(second_to_last) + ", now " + str(last_value) + "\n"

# Helper methods to run the spiders
class SpiderHelpers():
    
    # Function to format the new row we will append to the CSV file
    def create_list_of_values(site, xpath):
        return [datetime.now().strftime("%Y-%m-%d %H:%M"), site, xpath] 

    # Open the CSV and append the new row to it
    def append_to_csv(csv_name, new_row):
        # Open file in append mode
        with open("/home/awmarsden/Desktop/MtgPriceScraper/csvData/" + csv_name + '.csv', 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow(new_row)

    # Function to run the spiders 
    def run_spiders():
        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })
        process.crawl(EnduranceGoldfishSpider)
        process.crawl(PollutedDeltaGoldfishSpider)
        process.crawl(ForceOfWillGoldfishSpider)
        #process.crawl(ForceOfWillChGoldfishSpider) no money to be made really
        process.crawl(ForceOfNegationGoldfishSpider)
        process.crawl(VerdantCatacombsGoldfishSpider)
        # process.crawl(SanctumPrelateGoldfishSpider)
        #process.crawl(PrismaticEndingGoldfishSpider)  Already bought paper and online
        process.crawl(GristGoldfishSpider)
        # process.crawl(BrazenGoldfishSpider)
        # process.crawl(FieryIsletGoldfishSpider)
        process.crawl(BlackcleaveGoldfishSpider)
        # process.crawl(KlothysGoldfishSpider) # Just stable around 5.5 tix, dropped to 2.5, bought at about 3
        # process.crawl(MurktideGoldfishSpider)
        # process.crawl(SpirebluffCanalGoldfishSpider)
        #process.crawl(DauthiGoldfishSpider) just bounces from 8-10
        # process.crawl(MistyRainforestGoldfishSpider)
        # process.crawl(AlurenGoldfishSpider)
        # process.crawl(TashaGoldfishSpider)
        process.crawl(TreasureGoldfishSpider)
        process.start()

        with open('/home/awmarsden/Desktop/MtgPriceScraper/percentChanges.txt', 'w') as f:
            f.write(sig_changes)