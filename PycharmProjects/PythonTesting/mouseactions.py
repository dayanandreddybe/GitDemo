import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)
action=ActionChains(driver)

#action.context_click()
#action.double_click()
#draganddrop
#action.drag_and_drop()
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()

action.double_click(driver.find_element(By.ID,"checkBoxOption2")).click().perform()
time.sleep(10)
