from page.base_page import BasePage
from page.locators import RegisterPageLocators


class Register(BasePage):
    def add_email(self, email):
        self.wait_element(*RegisterPageLocators.INPUT_REGISTER_EMAIL).send_keys(email)

    def add_password_and_confirm(self, password):
        self.wait_element(*RegisterPageLocators.INPUT_REGISTER_PASSWORD).send_keys(password)
        self.wait_element(*RegisterPageLocators.INPUT_REGISTER_PASSWORD_CONFIRM).send_keys(password)
