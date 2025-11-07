from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.ID,"hide-textbox").click()
driver.find_element(By.ID,"show-textbox").click()
assert driver.find_element(By.ID,"displayed-text").is_displayed()