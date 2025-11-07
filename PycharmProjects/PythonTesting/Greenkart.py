import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,".search-button").click()
wait = WebDriverWait(driver, 10)

wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH, "//div[@class='products']/div")))
products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(products))
for product in products:
    product.find_element(By.XPATH,"div/button").click()
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
#subtotal
prices=driver.find_elements(By.XPATH,"//tr/td[5]/p")
sum=0
for price in prices:
    print(int(price.text))
    sum=sum+int(price.text)
    print(sum)
totalamount=int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
print(totalamount)
assert sum==totalamount


driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait = WebDriverWait(driver, 10)
message=wait.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, ".promoInfo")))
print(message)
disc=eval(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
print(disc)
assert totalamount > disc

time.sleep(10)
