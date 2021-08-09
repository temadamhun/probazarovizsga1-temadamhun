import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\\Users\\temad\\Desktop\\Driver\\chromedriver.exe"
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/lottery.html"
browser = webdriver.Chrome(PATH)
browser.get(URL)

szamok = browser.find_elements_by_xpath('//section[@id="container"]/div')
assert len(szamok) == 0

gen_btn = browser.find_element_by_id("draw-number")
for i in range(6):  #5 click megnyomása. A klikkek túl gyorsak, mindegyik után 2 sec várakozás a generált számok kiírására.
    gen_btn.click()
    time.sleep(2)
szamok = browser.find_elements_by_xpath('//section[@id="container"]/div') # container id-jú sectionben található div-ek keresése
assert len(szamok) == 6
for sz in szamok:   # végigmegyünk a div listán
    assert int(sz.text) > 0 and int(sz.text) < 60

gen_btn.click()                    #ez a 7. click
szamok = browser.find_elements_by_xpath('//section[@id="container"]/div')
assert len(szamok) == 6

reset_btn = browser.find_element_by_id("reset-numbers")
reset_btn.click()
szamok = browser.find_elements_by_xpath('//section[@id="container"]/div')
assert len(szamok) == 0