from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


# TODO: remove this hardcoded secrets
content = []
with open('../secrets.pass') as f:
    content = f.readlines()
username = content[0]
password = content[1]

options = webdriver.ChromeOptions()
# TODO: run headless in production
#options.add_argument('headless')
options.add_argument('--incognito')
driver = webdriver.Chrome('../tools/chromedriver', chrome_options=options)
driver.get('https://www.ihg.com')

web_driver_timout_seconds = 10

sign_in_button = WebDriverWait(driver, web_driver_timout_seconds).until(
	EC.element_to_be_clickable((By.XPATH, '//*[@title="Sign In"]')));
sign_in_button.click()

username_field = WebDriverWait(driver, web_driver_timout_seconds).until(
	EC.element_to_be_clickable((By.ID, 'UHF_username')));
username_field.click()
username_field.send_keys(username)

password_field = WebDriverWait(driver, web_driver_timout_seconds).until(
	EC.element_to_be_clickable((By.ID, 'UHF_password')));
password_field.click()

# sometimes this password entry fails, so we'll try up to 10 times
# TODO: this still fails fairly often
attempts = 0
while len(password_field.get_attribute('value')) != 4 and attempts < 10:
	password_field.send_keys(password)
	attempts = attempts + 1
	sleep(0.1)
