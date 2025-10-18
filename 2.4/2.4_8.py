import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions  as EC

import math
link = "http://suninjuly.github.io/explicit_wait2.html"

def summ(x):
    return math.log(abs(12*math.sin(x)))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser,12).until(
        EC.text_to_be_present_in_element((By.ID,"price"),'100'))
    button_book = (browser.find_element(By.ID, "book").
                   click())

    x = int(browser.find_element(By.ID,'input_value').text)

    input_summ = (browser.find_element(By.ID, 'answer').
                  send_keys(summ(x)))

    button_last = browser.find_element(By.ID,'solve').click()

finally:
    time.sleep(7)
    browser.quit()
