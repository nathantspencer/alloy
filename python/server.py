import json
from scrapers.valuations import tpg_scraper

from flask import Flask
app = Flask(__name__)

# require master password here
@app.route('/scrape/valuations', methods=['POST'])
def hello_world():
    return json.dumps(tpg_scraper.get_valuations())
