import time

from selenium import webdriver
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--ignore-certificate-errors")
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
#driver.execute_script("widow.scrollTo(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("daya.png")
time.sleep(10)