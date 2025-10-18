from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    link = browser.find_element(By.PARTIAL_LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()


    first_name = browser.find_element(By.NAME, "first_name")
    first_name.send_keys("Ivan")
    last_name = browser.find_element(By.NAME, "last_name")
    last_name.send_keys("Petrov")
    city = browser.find_element(By.CLASS_NAME, "city")
    city.send_keys("Smolensk")
    country = browser.find_element(By.ID, "country")
    country.send_keys("Russia")

    button_submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_submit.click()


finally:
    # успеваем скопировать код за 30секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()


# не забываем оставить пустую строку в конце файла