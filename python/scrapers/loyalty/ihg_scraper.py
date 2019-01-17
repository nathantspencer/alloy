from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


# TODO: remove this hardcoded secrets
content = []
with open('../../../secrets.pass') as f:
    content = f.readlines()
username = content[0]
password = content[1]

options = Options()
options.headless = False
driver = webdriver.Firefox(options=options,
	executable_path='../../../tools/geckodriver 3')
driver.get('https://www.ihg.com')

web_driver_timout_seconds = 10

sign_in_button = WebDriverWait(driver, web_driver_timout_seconds).until(
	EC.element_to_be_clickable((By.XPATH, '//*[@title="Sign In"]')))
sign_in_button.click()

username_field = WebDriverWait(driver, web_driver_timout_seconds).until(
	EC.element_to_be_clickable((By.ID, 'UHF_username')))
username_field.click()
username_field.send_keys(username)

password_field = WebDriverWait(driver, web_driver_timout_seconds).until(
	EC.element_to_be_clickable((By.ID, 'UHF_password')))
password_field.click()
password_field.send_keys(password)

submit_button = WebDriverWait(driver, web_driver_timout_seconds).until(
	EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'signIn')]")))
submit_button.click()

# TODO: more here

driver.close()
driver.quit()
