from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scrape(username, password):
	"""
	Creates and returns a JSON object containing user's total points, point
	expiration date, and loyalty level.

	:param username: account username as a string
	:param password: account password as a string
	:return: JSON object containing account information
	"""
	options = Options()
	options.headless = False
	driver = webdriver.Firefox(options=options,
		executable_path='../../../tools/geckodriver 3')

	web_driver_timout_seconds = 10
	driver.get('https://www.ihg.com/rewardsclub/us/en/sign-in/')

	username_field = WebDriverWait(driver, web_driver_timout_seconds).until(
		EC.element_to_be_clickable((By.NAME, 'emailOrPcrNumber')))
	username_field.send_keys(username)

	pin_field = WebDriverWait(driver, web_driver_timout_seconds).until(
		EC.element_to_be_clickable((By.XPATH, '//input[contains(@pattern, "[0-9]*")]')))
	pin_field.send_keys(password)

	submit_button = WebDriverWait(driver, web_driver_timout_seconds).until(
		EC.element_to_be_clickable((By.ID, 'tpiSubmitButton')))
	submit_button.click()

	profile_button = WebDriverWait(driver, web_driver_timout_seconds).until(
		EC.element_to_be_clickable((By.XPATH, '//a[@href="/rewardsclub/us/en/account-mgmt/home"]')))
	profile_button.click()

	WebDriverWait(driver, web_driver_timout_seconds).until(
		EC.element_to_be_clickable((By.XPATH, '//span[contains(@class, "t3 ng-binding")]')))
	soup = BeautifulSoup(driver.page_source, 'lxml')
	result = {}

	points_span = soup.find('span', { 'class' : 't3 ng-binding' })
	result['points'] = int(points_span.text.split()[0].replace(',', ''))

	level_span = soup.find('span', { 'data-slnm-ihg' : "memberLevelNameSID" })
	result['level'] = level_span.text.encode('ascii','ignore')

	if result['level'] == 'club':
		expiration_ng = "pointsTracker.pointsExpirationDate && pointsTracker.isClubLevel"
		expiration_span = soup.find('span', { 'ng-if' : expiration_ng })
		result['expiration'] = expiration_span.text.split()[2].encode('ascii','ignore')
	else:
		# for levels above club, points don't expire
		result['expiration'] = 'N/A'

	driver.close()
	driver.quit()
	return result

if __name__ == '__main__':
	"""
	Prints a JSON object containing information scraped from IHG account:
	total points, expiration date, and loyalty level. Uses a hardcoded file
	secrets.pass in the root directory of alloy for user credentials.
	"""
	content = []
	with open('../../../secrets.pass') as f:
	    credentials = f.readlines()
	username = credentials[0]
	password = credentials[1]
	print(scrape(username, password))
