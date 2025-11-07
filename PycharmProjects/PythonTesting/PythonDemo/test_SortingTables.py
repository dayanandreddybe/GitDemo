import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_sort(browserInstance):
    driver=browserInstance
    browserSortedveggies=[]
    driver=webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
#Click on columnheader
    driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
#collect all vegie names ->brosersortveggielist(A,B,C)
    vegiewebelements=driver.find_elements(By.XPATH,"//tbody/tr/td[1]")
    for ele in vegiewebelements:
        browserSortedveggies.append(ele.text)
        print(browserSortedveggies)
        originalbrowsersortedlist=browserSortedveggies.copy()
#sort this browser sortedveggie list ->newsortedList->(A,B,C)
        browserSortedveggies.sort()
        assert browserSortedveggies==originalbrowsersortedlist
        time.sleep(10)