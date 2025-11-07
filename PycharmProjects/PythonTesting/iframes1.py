from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()
driver.switch_to.frame("mce_0_ifr")
txt=driver.find_element(By.TAG_NAME,"p").text
print(txt)
driver.switch_to.default_content()
txt2=driver.find_element(By.TAG_NAME,"h3").text
print(txt2)