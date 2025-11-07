import time

from selenium import webdriver
from selenium.webdriver.common.by import By

expectedlist=["Cucumber - 1 Kg","Raspberry - 1/4 Kg","Strawberry - 1/4 Kg"]
actuallist=[]
driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
driver.find_element(By.CSS_SELECTOR,".search-button").click()
time.sleep(4)
actual=driver.find_elements(By.CSS_SELECTOR,"div h4")
print(len(actual))
for l in actual:
    actuallist.append(l.text)
print(actuallist)
assert actuallist==expectedlist



time.sleep(10)