import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
browsersortedprice=[]
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
driver.find_element(By.XPATH,"//span[text()='Price']").click()
pricelist=(driver.find_elements(By.XPATH,"//tbody/tr/td[2]"))
for price in pricelist:
    browsersortedprice.append(int(price.text))
print(browsersortedprice)
originalbrowsersortedlist=browsersortedprice.copy()
browsersortedprice.sort()
assert browsersortedprice==originalbrowsersortedlist






time.sleep(5)