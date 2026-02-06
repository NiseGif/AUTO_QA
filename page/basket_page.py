from page.base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def check_null_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_FIELD), "Bask is not null"

    def check_null_basket_text(self):
        assert self.is_element_present(
            *BasketPageLocators.TEXT_NULL_BASKET
        ), "Empty basket text is not present"

        text = self.browser.find_element(
            *BasketPageLocators.TEXT_NULL_BASKET).text
        assert "Ваша корзина пуста" in text, "Error null basket"