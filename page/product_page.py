
from .base_page import BasePage
from .locators import ProductLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        assert self.is_element_present(*ProductLocators.ADD_TO_BASKET), 'No element #addToBasket'
        self.browser.find_element(*ProductLocators.ADD_TO_BASKET).click()
        self.solve_quiz_and_get_code()

    def check_text_add_book(self):
        assert self.is_element_present(*ProductLocators.CHECK_FIRST_ALERT_INNER), 'No element .alertinner'

        #Текст, что книга добавлена
        text_check_alerttiner = self.browser.find_element(*ProductLocators.CHECK_FIRST_ALERT_INNER).text
        #Наименование книги
        text_book = self.browser.find_element(*ProductLocators.TEXT_ALERT_INNER).text

        assert text_book == text_check_alerttiner, 'Error name book'

    def check_sum_basket(self):
        assert self.browser.find_element(*ProductLocators.CHECK_PRICE_IN_PRODUCT_PAGE).text == self.browser.find_element(*ProductLocators.PRICE_BOOK).text, \
            "Error Price in Page"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductLocators.CHECK_FIRST_ALERT_INNER), "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductLocators.CHECK_FIRST_ALERT_INNER), "Success message is presented, but should not be"