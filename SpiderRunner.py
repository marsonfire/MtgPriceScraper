import EnduranceTcgPlayerSpider, EnduranceCardKingdomSpider, EnduranceScgSpider,TestSpiders


#https://towardsdatascience.com/tutorial-scrape-100-headlines-in-seconds-with-23-lines-of-python-14047deb1a98
#https://towardsdatascience.com/web-scraping-with-scrapy-8071fd627051
#scrapy runspider EnduranceTcgPlayerSpider.py -o test.csv

#broken cuz tcgplayer changed thier site
#EnduranceTcgPlayerSpider.EnduranceTcgPlayerRunner.run_spider()

# EnduranceCardKingdomSpider.EnduranceCardKingdomRunner.run_spider()
# EnduranceScgSpider.EnduranceScgRunner.run_spider()

TestSpiders.Runner.run_spider()
