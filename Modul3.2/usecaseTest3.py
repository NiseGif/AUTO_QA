from numpy.ma.testutils import assert_equal
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest
import pytest

class Test(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.browser.get(link)
        (self.browser.find_element(By.CSS_SELECTOR, ".first_block .first")
         .send_keys("dhfbr"))
        (self.browser.find_element(By.CSS_SELECTOR, " .first_block .second")
         .send_keys("jhfue"))
        (self.browser.find_element(By.CSS_SELECTOR,".third")
         .send_keys("furhfyrg7y"))
        (self.browser.find_element(By.CSS_SELECTOR, "button.btn")
         .click())

        (WebDriverWait(self.browser,5)
                .until(EC.url_changes("http://suninjuly.github.io/registration_result.html?")))

        # записываем в переменную welcome_text текст из элемента
        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!",welcome_text, "ХУЙНЯ")

    def test_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.browser.get(link)

        (self.browser.find_element(By.CSS_SELECTOR, ".first_block .first").
         send_keys("dhfbr"))
        (self.browser.find_element(By.CSS_SELECTOR, " .first_block .second").
         send_keys("jhfue"))
        (self.browser.find_element(By.CSS_SELECTOR,".third").
         send_keys("furhfyrg7y"))
        (self.browser.find_element(By.CSS_SELECTOR, "button.btn")
         .click())

        (WebDriverWait(self.browser,5)
                .until(EC.url_changes("http://suninjuly.github.io/registration_result.html?")))

        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!",welcome_text, "ХУИТА")


if __name__ == "__main__":
    unittest.main()