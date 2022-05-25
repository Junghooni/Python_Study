from optparse import Option
from ssl import Options
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)
driver.maximize_window()    #창 최대화
url = 'https://google.com'
driver.get(url)

driver.find_element(By.CSS_SELECTOR, 'input').send_keys('네이버 부동산')
driver.find_element(By.CSS_SELECTOR, 'input').send_keys(Keys.ENTER)
driver.find_element(By.CSS_SELECTOR, '.LC20lb.MBeuO.DKV0Md').click()
driver.find_elements(By.CSS_SELECTOR, '.selectbox-box')[1].click()
driver.find_elements(By.CSS_SELECTOR, '.selectbox-item')[3].click()
driver.find_elements(By.CSS_SELECTOR, '.icon.icon_step')[2].click()
driver.find_elements(By.CSS_SELECTOR, '.radio_label_district')[3].click()
driver.find_element(By.CSS_SELECTOR, '.complex_item_inner').click()