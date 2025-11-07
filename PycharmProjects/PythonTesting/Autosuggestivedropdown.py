import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver.find_element(By.XPATH,"//div/fieldset/input").send_keys("Ind")
time.sleep(5)
countries=driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text=="India":
        country.click()
        break
print(driver.find_element(By.XPATH,"//div/fieldset/input").get_attribute("value"))
assert driver.find_element(By.XPATH,"//div/fieldset/input").get_attribute("value")=="India"