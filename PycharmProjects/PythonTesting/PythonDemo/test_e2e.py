import json
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PythonDemo.PageObjects.Checkout_Confirmation import Checkout_Confirmation
from PythonDemo.PageObjects.Login import LoginPage
from PythonDemo.PageObjects.ShopPage import ShopPage
test_data_path ='C:\\Users\\reddyd\\PycharmProjects\\PythonTesting\\PythonDemo\\data\\test_e2e.json'
with open(test_data_path) as f:
    test_data=json.load(f)
    test_list=test_data["data"]
@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item",test_list)
def test_end2end(browserInstance,test_list_item):
    driver = browserInstance

    loginpage=LoginPage(driver)
    loginpage.login(test_list_item["userEmail"],test_list_item["userPassword"])
    print(loginpage.getTitle())
    print(loginpage.getcurrent_url())
    shoppage=ShopPage(driver)
    shoppage.add_product_to_cart("productName")
    shoppage.goToCart()
    print(shoppage.getTitle())
    print(shoppage.getcurrent_url())
    check=Checkout_Confirmation(driver)
    check.checkout()
    check.enter_delivery_Address(test_list_item["countryName"])
    check.validation_order()
    print(check.getTitle())
    print(check.getcurrent_url())
    # driver.find_element(By.LINK_TEXT,"Shop").click()
    # driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
    #driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()
    time.sleep(10)
