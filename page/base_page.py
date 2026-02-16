import math
from selenium.common import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException # в начале файла
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from page.locators import BasePageLocators


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        #self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET)
        link.click()

    def change_language(self,language):
        self.browser.find_element(*BasePageLocators.LANGUAGE).click()
        self.browser.find_element(By.CSS_SELECTOR,f"[value={language}]").click() #подумать над реализацией динамического локатора

        assert self.is_element_present(*BasePageLocators.BUTTION_LANGUAGE), 'ERROR button_lg'
        self.browser.find_element(*BasePageLocators.BUTTION_LANGUAGE).click()

        assert self.is_element_present(*BasePageLocators.WEB_LANGUAGE), 'ERROR load language in site'
        web_lg = self.browser.find_element(*BasePageLocators.WEB_LANGUAGE).get_attribute("lang")
        assert web_lg == language, "Languages don't match"


    def should_be_change_language(self):
        assert self.is_element_present(*BasePageLocators.LANGUAGE), "Change language is not available"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what, timeout = 4):
        try:
            WebDriverWait(self.browser,timeout).\
                until(EC.visibility_of_element_located((how,what)))
            #self.browser.find_element(how,what) # Добавить явное ожидание
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self,how,what,timeout=4):
        try:
            WebDriverWait(self.browser, timeout).\
                until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True