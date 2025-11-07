import time

from selenium import webdriver
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--start-maximized")
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
time.sleep(5)