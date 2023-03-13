# TIP: use 'py' to run file in terminal

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.google.com/search?q=restaurants+in+sydney&oq=restaurants+in+sydney&aqs=chrome.0.69i59j0i10i433i457i512j0i402j0i10i402i433i512j0i10i512j69i60l3.4986j0j7&sourceid=chrome&ie=UTF-8")
driver.maximize_window()

#target = '//span[@class="OSrXXb"]'
#links = driver.find_elements("xpath", target)
#for link in links:
#    print(link.get_attribute("innerHTML"))

x_more_places = '//span[@class="Z4Cazf OSrXXb"]'
links = driver.find_elements("xpath", x_more_places)
links[0].click()

x_restaurants = '//span[@class="OSrXXb"]'
restaurants = driver.find_elements("xpath", x_restaurants)
for r in restaurants:
    print(r.get_attribute("innerHTML"))

driver.close()
driver.quit()