import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR,"#autocomplete").send_keys("Ind")
time.sleep(5)

countries=driver.find_elements(By.CSS_SELECTOR,"li div")
for country in countries:
    if country.text=="India":
        country.click()
        break


