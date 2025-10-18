from selenium import webdriver
from selenium.webdriver.common.bidi.browser import Browser
from selenium.webdriver.common.by import By
import  time
import math

link ="http://suninjuly.github.io/redirect_accept.html"

def summ(x):
    return str(math.log(abs(12*math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    fly_button = (browser.find_element(By.TAG_NAME, "button")
                  .click())

    new_window = browser.window_handles[1] #узнаем имя 2-й вкладки
    browser.switch_to.window(new_window) #переходим во 2-е окно

    x = browser.find_element(By.ID,"input_value").text

    input_summ = (browser.find_element(By.TAG_NAME,"input")
                  .send_keys(summ(int(x))))

    button_submit = (browser.find_element(By.TAG_NAME,"button")
                     .click())

    #alert - вариант модального окна, в котором 1 вариант ответа, обычно "ОК"
    alert = browser.switch_to.alert.text
    print(alert)

finally:

    browser.quit()