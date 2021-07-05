import MtgSpiders

#https://towardsdatascience.com/tutorial-scrape-100-headlines-in-seconds-with-23-lines-of-python-14047deb1a98
#https://towardsdatascience.com/web-scraping-with-scrapy-8071fd627051
#scrapy runspider EnduranceTcgPlayerSpider.py -o test.csv
#0 */6 * * * /usr/bin/python3 /home/awmarsden/Desktop/MtgPriceScraper/SpiderRunner.py

#TCG Player and Card Hoarder seem to block bots
MtgSpiders.SpiderHelpers.run_spiders()

# MtgSpiders.SummaryFile.percent_change('sanctumPrelate')
# MtgSpiders.SummaryFile.percent_change('pollutedDelta')