from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

sign_in_button = WebDriverWait(driver, 10).until(
	EC.element_to_be_clickable((By.XPATH, '//*[@title="Sign In"]')));
sign_in_button.click()

username_field = WebDriverWait(driver, 10).until(
	EC.element_to_be_clickable((By.ID, 'UHF_username')));
username_field.click()
username_field.send_keys(username)

password_field = WebDriverWait(driver, 10).until(
	EC.element_to_be_clickable((By.ID, 'UHF_password')));
password_field.click()

# sometimes this password entry fails, so we'll try up to 10 times
password_attempts = 0
while password_field.get_attribute('value') == '' and password_attempts < 10:
	password_field.send_keys(password)
	password_attempts = password_attempts + 1
