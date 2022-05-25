from optparse import Option
from ssl import Options
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)
url = 'https://google.com'
driver.get(url)
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, 'input').send_keys('네이버 부동산')
driver.find_element(By.CSS_SELECTOR, 'input').send_keys(Keys.ENTER)