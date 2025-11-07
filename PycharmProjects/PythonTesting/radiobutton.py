import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
rad=driver.find_elements(By.XPATH,"//div[1]/fieldset/label/input")
print(len(rad))
for r in rad:
    if r.get_attribute("value")=="radio2":
        r.click()
        assert r.is_selected()
        break

time.sleep(5)