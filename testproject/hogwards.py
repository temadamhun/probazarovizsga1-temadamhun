
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\\Users\\temad\\Desktop\\Driver\\chromedriver.exe"
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/hogwards.html"
browser = webdriver.Chrome(PATH)
browser.maximize_window()  # az oldal méretét maximalizálja.
browser.get(URL)

passanger_input = browser.find_element_by_id("passenger")
pass_input_value = "adam"
passanger_input.send_keys(pass_input_value)
departure_date = browser.find_element_by_id("departure-date")
departure_date.send_keys("2021")
departure_date.send_keys(Keys.TAB)
departure_date.send_keys("1010")

departure_time = browser.find_element_by_id("departure-time")
departure_time.send_keys("10:10")


button = browser.find_element_by_id("issue-ticket")
button.click()

passanger_text = browser.find_element_by_id("passenger-name").text
assert passanger_text == pass_input_value.upper()
departure_text = browser.find_element_by_id("departure-date-text").text
assert departure_text == "2021-10-10"
side_departure_text = browser.find_element_by_id("side-detparture-date").text
assert side_departure_text == "2021-10-10"
departure_time_text = browser.find_element_by_id("departure-time-text").text
assert departure_time_text == "10:10AM"
side_departure_time_text = browser.find_element_by_id("side-departure-time").text
assert side_departure_time_text == "10:10AM"

