from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\\Users\\temad\\Desktop\\Driver\\chromedriver.exe"
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/landtransfertax.html"
browser = webdriver.Chrome(PATH)
browser.get(URL)

btn = browser.find_element_by_xpath('//button[@class="btn-go"][text()="Go"]')
btn.click()

tax = browser.find_element_by_id("tax")
assert  tax.get_attribute("value") == ""

hiba_uzenet = browser.find_element_by_xpath('//p[@id="disclaimer"]/strong')
assert hiba_uzenet.text == "Enter the property value before clicking Go button."

price = browser.find_element_by_id("price")
price.send_keys("33333")
btn.click()
tax = browser.find_element_by_id("tax")
assert  tax.get_attribute("value") == "166.665"  # NEM a feladatleírásban szereplő 16.665 érték jön
