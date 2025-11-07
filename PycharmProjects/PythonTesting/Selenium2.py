import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
#ID,XPATH,CSSSELECTOR,NAME,CLASSNAME,LINKTEXT,PARTIALLINKteXT,

#ID is CSS

driver.find_element(By.NAME,"name").send_keys("DAYANANDA REDDY")
driver.find_element(By.NAME,"email").send_keys("dayanandreddybe@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("Nirosha@123")
driver.find_element(By.ID,"exampleCheck1").click()
dropdown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
driver.find_element(By.ID,"inlineRadio1").click()
driver.find_element(By.NAME,"bday").send_keys("17-06-1986")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message=driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success! The Form has been submitted successfully!." in message
time.sleep(5)