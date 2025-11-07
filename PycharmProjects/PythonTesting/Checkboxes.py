import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(10)
checkboxes=driver.find_elements(By.XPATH,"//div[4]/fieldset/label/input")
for checkbox in checkboxes:
    if checkbox.get_attribute("value")=="option3":
        checkbox.click()
        break

time.sleep(10)