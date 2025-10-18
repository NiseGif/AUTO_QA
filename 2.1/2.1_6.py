from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # people_rule = browser.find_element(By.ID,"peopleRule")
    #
    # people_checked = people_rule.get_attribute("checked")
    # print("value of people radio: ", people_checked)
    # assert people_checked is not None

    robots_rule = browser.find_element(By.ID,"robotsRule")

    robots_rule = robots_rule.get_attribute("checked")
    print(robots_rule)
    assert robots_rule is None, "пиздешь"

finally:

    browser.quit()