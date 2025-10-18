from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/get_attribute.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute('valuex')

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(calc(x))

    check_robot = browser.find_element(By.ID,"robotCheckbox")
    check_robot.click()

    rdb_robot = browser.find_element(By.ID,"robotsRule")
    rdb_robot.click()

    button_submit = browser.find_element(By.CSS_SELECTOR, "button[type=submit]")
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()






