import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--start-maximized')
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
#driver.find_element(By.LINK_TEXT,"Shop").click()
#driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
driver.find_element(By.XPATH,"//a[contains(@href,'shop')]").click()

products=driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for product in products:
    productName=product.find_element(By.XPATH,"div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH,"div/button").click()

driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.CSS_SELECTOR,"button[class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("Ind")
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//label[@for='checkbox2']").click()
driver.find_element(By.XPATH,"//input[@value='Purchase']").click()
message=driver.find_element(By.CLASS_NAME,"alert-success").text
assert "Success!" in message
time.sleep(10)











time.sleep(10)