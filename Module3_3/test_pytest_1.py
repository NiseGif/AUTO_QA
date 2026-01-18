from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def test_1(browser):
    link = "http://suninjuly.github.io/registration1.html"
    browser.get(link)
    (browser.find_element(By.CSS_SELECTOR, ".first_block .first")
     .send_keys("dhfbr"))
    (browser.find_element(By.CSS_SELECTOR, ".first_block .second")
     .send_keys("jhfue"))
    (browser.find_element(By.CSS_SELECTOR, ".third")
     .send_keys("furhfyrg7y"))
    (browser.find_element(By.CSS_SELECTOR, "button.btn")
     .click())

    (WebDriverWait(browser, 5)
     .until(EC.url_changes("http://suninjuly.github.io/registration_result.html?")))

    # записываем в переменную welcome_text текст из элемента
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

def test_2(browser):
    link = "http://suninjuly.github.io/registration2.html"
    browser.get(link)

    (browser.find_element(By.CSS_SELECTOR, ".first_block .first").
     send_keys("dhfbr"))
    (browser.find_element(By.CSS_SELECTOR, ".first_block .second").
     send_keys("jhfue"))
    (browser.find_element(By.CSS_SELECTOR, ".third").
     send_keys("furhfyrg7y"))
    (browser.find_element(By.CSS_SELECTOR, "button.btn")
     .click())

    (WebDriverWait(browser, 5)
     .until(EC.url_changes("http://suninjuly.github.io/registration_result.html?")))

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text


if __name__ == "__main__":
    pytest.main()