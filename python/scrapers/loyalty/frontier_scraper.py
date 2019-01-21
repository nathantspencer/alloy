from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import code


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

web_driver_timout_seconds = 10
driver.get('https://www.flyfrontier.com/')

# TODO

code.interact(local=locals())

driver.close()
driver.quit()
