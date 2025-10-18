from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/execute_script.html"


def sum(x):
    return str(math.log(abs(12 * math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID,"input_value").text
    input = browser.find_element(By.ID,"answer").send_keys(sum(int(x)))

    button = browser.find_element(By.TAG_NAME,"button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    checkBox = browser.find_element(By.ID,"robotCheckbox")
    checkBox.click()

    button = browser.find_element(By.TAG_NAME,"button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    radioBox = browser.find_element(By.ID, "robotsRule")
    radioBox.click()

    button.click()

finally:
    time.sleep(7)
    browser.quit()