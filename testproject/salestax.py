from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\\Users\\temad\\Desktop\\Driver\\chromedriver.exe"
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/salestax.html"
browser = webdriver.Chrome(PATH)
browser.maximize_window()  # az oldal méretét maximalizálja.
browser.get(URL)

subtotal_btn = browser.find_element_by_id("subtotalBtn")
subtotal_btn.click()
subtotal = browser.find_element_by_id("subtotal")
assert subtotal.get_attribute("value") == "0.00"

gtotal_btn = browser.find_element_by_id("gtotalBtn")
gtotal_btn.click()
salestax = browser.find_element_by_id("salestax")
assert salestax.get_attribute("value") == "0.00"
gtotal = browser.find_element_by_id("gtotal")
assert gtotal.get_attribute("value") == "4.95"

prod = browser.find_element_by_xpath('//select[@id="Proditem"]/option[@value="4.95"]')
prod.click()

quantity = browser.find_element_by_id("quantity")
quantity.send_keys("1")
subtotal_btn.click()
assert subtotal.get_attribute("value") == "4.95"  # itt a subtotal mező értéke lesz 4.95, nem a salestax azonosítójú mező értéke
gtotal_btn.click()
assert gtotal.get_attribute("value") == "9.90"

