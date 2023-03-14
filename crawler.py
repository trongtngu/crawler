from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import time
import json

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.google.com/search?q=restaurants+in+sydney&oq=restaurants+in+sydney&aqs=chrome.0.69i59j0i10i433i457i512j0i402j0i10i402i433i512j0i10i512j69i60l3.4986j0j7&sourceid=chrome&ie=UTF-8")

x_more_places = '//span[@class="Z4Cazf OSrXXb"]'
mp = driver.find_element("xpath", x_more_places)
mp.click()

restaurant_dict = {}

x_restaurants = '//span[@class="OSrXXb"]'
x_price_button = '//span[@class="WaZi0e OSrXXb"]'
x_filter_prices = '//span[@jsname="NNJLud"]'
x_apply_button = '//span[@class="kpmBG"]'
x_price_button = '//span[@class="WaZi0e OSrXXb"]'

# Clicking the Price filter
# pb opens up the dropdown
pb = driver.find_elements('xpath', x_price_button)
pb[2].click()

# Cheap Restaurants - $
# click price $ -> click apply -> click prices dropdown
prices = driver.find_elements('xpath', x_filter_prices)
prices[0].click()

ab = driver.find_element('xpath', x_apply_button)
ab.click()

restaurants = driver.find_elements("xpath", x_restaurants)
for r in restaurants:
    restaurant_dict[r.get_attribute("innerHTML")] = {"price": "$"}

pb = driver.find_elements('xpath', x_price_button)
pb[2].click()

# Moderately expensive - $$
prices = driver.find_elements('xpath', x_filter_prices)
prices[0].click()

prices = driver.find_elements('xpath', x_filter_prices)
prices[1].click()

ab = driver.find_element('xpath', x_apply_button)
ab.click()

restaurants = driver.find_elements("xpath", x_restaurants)
for r in restaurants:
    restaurant_dict[r.get_attribute("innerHTML")] = {"price": "$$"}

pb = driver.find_elements('xpath', x_price_button)
pb[2].click()

# Expensive - $$$
prices = driver.find_elements('xpath', x_filter_prices)
prices[1].click()

prices = driver.find_elements('xpath', x_filter_prices)
prices[2].click()

ab = driver.find_element('xpath', x_apply_button)
ab.click()

restaurants = driver.find_elements("xpath", x_restaurants)
for r in restaurants:
    restaurant_dict[r.get_attribute("innerHTML")] = {"price": "$$$"}

pb = driver.find_elements('xpath', x_price_button)
pb[2].click()

# Very expensive - $$$$ 
prices = driver.find_elements('xpath', x_filter_prices)
prices[2].click()

prices = driver.find_elements('xpath', x_filter_prices)
prices[3].click()

ab = driver.find_element('xpath', x_apply_button)
ab.click()

restaurants = driver.find_elements("xpath", x_restaurants)
for r in restaurants:
    restaurant_dict[r.get_attribute("innerHTML")] = {"price": "$$$$"}

with open("database.json", "w") as outfile:
    json.dump(restaurant_dict, outfile, indent=4)

#with open("database.json", "w") as outfile:
    #json.dump(restaurant_dict, outfile, indent=4)

#restaurants = driver.find_elements("xpath", x_restaurants)
#for r in restaurants:
    #restaurant_dict[r.get_attribute("innerHTML")] = {"price": "$$"}

#driver.close()
#driver.quit()