import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\\Users\\temad\\Desktop\\Driver\\chromedriver.exe"
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/timesheet.html"
browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)

next_btn = browser.find_element_by_xpath('//input[@type="button"][@value="Next"]')
assert next_btn.get_attribute("disabled") == "true" # nem aktív gomb, a gomb disabled attribum értéke true
emai_input = browser.find_element_by_xpath('//input[@type="email"]')
emai_input.send_keys("test.test")
assert next_btn.get_attribute("disabled") == "true"

emai_input.send_keys("test@bela.hu")
hours = browser.find_element_by_xpath('//input[@ng-model="ele.time.hours"]')
hours.send_keys("2")
minutes = browser.find_element_by_xpath('//input[@ng-model="ele.time.mins"]')
minutes.send_keys("0")
message = browser.find_element_by_xpath('//textarea[@ng-model="ele.msg"]')
message.send_keys("working hard")
work = browser.find_element_by_xpath('//select[@id="dropDown"]/option[@value="Time working on visual effects for movie"]')
work.click()
next_btn.click()

WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "section-thankyou")))
check = browser.find_elements_by_xpath('//span[@class="green ng-binding"]')
assert check[1].text == "2"  # tömb első eleme az email, a 2. eleme az óra
assert check[2].text == "0"
