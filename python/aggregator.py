from scrapers.valuations import tpg_scraper
from scrapers.loyalty import ihg_scraper

valuations = tpg_scraper.get_valuations()
geckodriver_path = '../tools/geckodriver 3'

# IHG
credentials = []
with open('../secrets.pass') as f:
    credentials = f.readlines()
username = credentials[0]
password = credentials[1]
ihg_results = ihg_scraper.get_account_info(username, password, geckodriver_path)
ihg_results['value'] = ihg_results['points'] * valuations['ihg'] / 100.0
print(ihg_results)

# this all might actually be done client-side instead to avoid having to scrape
# valuations over and over again...
