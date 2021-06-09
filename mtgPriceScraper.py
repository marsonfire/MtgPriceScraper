import scrapy
from pandas import read_csv
from readability.readability import Document

PATH_TO_DATA = 'testUrls.csv'
#https://towardsdatascience.com/web-scraping-with-scrapy-8071fd627051


class EnduranceSpider(scrapy.Spider):
    name = "enduranceSpider"
    start_urls = ['https://shop.tcgplayer.com/magic/modern-horizons-2/endurance?xid=a5beae949-191c-4d02-9309-692dc57d1b5a', 
                    'https://www.cardkingdom.com/mtg/modern-horizons-2/endurance',
                    'https://starcitygames.com/endurance-sgl-mtg-mh2-157-enn/?sku=SGL-MTG-MH2-157-ENN1',
                    'https://www.cardhoarder.com/cards/90691']

    def parse(self, response):
        doc = Document(response.text)
        yield {
            'short_title': doc.short_title(),
            'full_title': doc.title(),
            'url': response.url
        }

    