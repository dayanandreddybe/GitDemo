from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Click Here").click()
windows=driver.window_handles
print(len(windows))
driver.switch_to.window(windows[1])
print(driver.title)
driver.switch_to.window(windows[0])
print(driver.title)