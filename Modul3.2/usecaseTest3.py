from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest


browser = webdriver.Chrome()

class Test(unittest.TestCase):
    def test1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)
        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        first_name.send_keys("dhfbr")
        last_name = browser.find_element(By.CSS_SELECTOR, " .first_block .second")
        last_name.send_keys("jhfue")
        email = browser.find_element(By.CSS_SELECTOR,".third")
        email.send_keys("furhfyrg7y")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        wait = WebDriverWait(browser,5)
        wait.until(EC.url_changes("http://suninjuly.github.io/registration2.html"))

    def test2(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text


browser.quit()

if __name__ == "__main__":
    unittest.main()