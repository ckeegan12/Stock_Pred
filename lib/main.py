import requests
from bs4 import BeautifulSoup
import pandas as pd

# Initialize data frames
prev_close = []
open = []
bid =[]
ask = []
day_range = []
range_52 = []
volume = []
avg_vol = []
market_cap = []
beta = []
pe_ratio = []
eps = []


def scrape_date():
    url = 'https://finance.yahoo.com/quote/AAPL/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    a_tags = soup.find_all('a', class_='historical-link cmc-link')
    for tag in a_tags:
        href = tag.get('href')
        scrape_date_list.append(href)

scrape_date()
print('There are ' + str(len(scrape_date_list)) + ' dates(Sundays) available for scraping from CoinMarketCap historical data.')


