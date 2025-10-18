from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time

link = "https://suninjuly.github.io/selects2.html"


def summ(x,y):
    return x+y

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = int(browser.find_element(By.ID,"num1").text)
    num2 = int(browser.find_element(By.ID,"num2").text)
    print(summ(num1,num2))

    (Select(browser.find_element(By.CSS_SELECTOR,"select"))
     .select_by_value("%d" % (summ(num1,num2))))


    button = (browser.find_element(By.TAG_NAME, "button")
              .click())

finally:
    time.sleep(7)
    browser.quit()