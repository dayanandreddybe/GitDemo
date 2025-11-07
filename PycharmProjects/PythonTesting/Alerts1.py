import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.ID,"name").send_keys("DAYANANDA REDDY")
driver.find_element(By.ID,"confirmbtn").click()
alerts=driver.switch_to.alert
print(alerts.text)
alerts.accept()

time.sleep(5)