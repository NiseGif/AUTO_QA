from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим х
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    check_robot = browser.find_element(By.CSS_SELECTOR,"[for='robotCheckbox']")
    check_robot.click()

    robots_rule = browser.find_element(By.ID,"robotsRule")
    robots_rule.click()

    button = browser.find_element(By.TAG_NAME,"button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()