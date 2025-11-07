import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(10)
dropdown=Select(driver.find_element(By.CSS_SELECTOR,"#dropdown-class-example"))
dropdown.select_by_visible_text("Option2")
time.sleep(10)