from selenium import webdriver
from selenium.webdriver.common.by import By
import  time
import math

link = "http://suninjuly.github.io/alert_accept.html"

def summ(x):
    return str(math.log(abs(12*math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button_magic = (browser.find_element(By.TAG_NAME,"button")
                    .click())

    # confirm - вариант модального окна, который предлагает пользователю выбор согласиться с сообщением или отказаться от него
    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.ID,"input_value").text

    input_summ = (browser.find_element(By.TAG_NAME,"input")
                  .send_keys(summ(int(x))))

    button_submit = (browser.find_element(By.TAG_NAME,"button")
                     .click())

    #alert - вариант модального окна, в котором 1 вариант ответа, обычно "ОК"
    alert = browser.switch_to.alert.text
    print(alert)

finally:
    time.sleep(5)
    browser.quit()