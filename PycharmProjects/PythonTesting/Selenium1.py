import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj=Service("C:\\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)

#driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/")
print(driver.title)
print(driver.current_url)

time.sleep(2)