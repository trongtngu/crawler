
# TIP: use 'py' to run file in terminal

from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service

def launchBrowser ():
    driver_service = Service(executable_path="C:\Program Files (x86)\chromedriver.exe")

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(service=driver_service)

    driver.get("https://google.com")
    while(True):
        pass

launchBrowser()