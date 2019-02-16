from bs4 import BeautifulSoup
import json
import requests


def get_valuation(valuation_table, program_name):
	"""
	Retrieves the value of a loyalty program's point in cents.

	:param valuation_table: a bs4 object pointing to TPG's valuation table
	:param program_name: the string name of the loyalty program
	:return: the value of the one point in cents
	"""
	row = valuation_table.find(text=program_name).parent.parent
	valuation = row.findChildren('td', recursive=False)[3].text
	return float(valuation)

def get_valuations():
	"""
	Creates and returns a dictionary mapping of loyalty program abbreviations to
	the current value of each point, in cents.

	:return: dictionary containing loyalty program valuations
	"""
	tpg_valuation_url = 'https://thepointsguy.com/guide/monthly-valuations/'
	tpg_response = requests.get(tpg_valuation_url, verify=True)
	soup = BeautifulSoup(tpg_response.text, 'lxml')
	table = soup.find('section', { 'class': 'table' })

	result = {}
	result['ihg']       = get_valuation(table, 'IHG Rewards Club')
	result['delta']     = get_valuation(table, 'Delta SkyMiles')
	result['american']  = get_valuation(table, 'American AAdvantage')
	result['frontier']  = get_valuation(table, 'Frontier Miles')
	result['hilton']    = get_valuation(table, 'Hilton Honors')
	result['hyatt']     = get_valuation(table, 'World of Hyatt Loyalty Program')
	result['jetblue']   = get_valuation(table, 'JetBlue TrueBlue Rewards Program')
	result['marriott']  = get_valuation(table, 'Marriott Rewards')
	result['southwest'] = get_valuation(table, 'Southwest Rapid Rewards')
	result['spirit']    = get_valuation(table, 'Spirit Airlines Free Spirit')
	result['united']    = get_valuation(table, 'United MileagePlus')
	return result

if __name__ == '__main__':
	"""
	Prints a dictionary mapping of loyalty program abbreviations to the
	current value of each point in cents, according to thepointsguy.com.
	"""
	print(get_valuations())
