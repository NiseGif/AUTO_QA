from selenium.webdriver.common.by import By
from conftest import language


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    CHECK_FIRST_ALERT_INNER = (By.CSS_SELECTOR, '.alertinner strong')
    TEXT_ALERT_INNER = (By.CSS_SELECTOR, 'div h1')
    CHECK_PRICE_IN_PRODUCT_PAGE = (By.CSS_SELECTOR, 'div[class = "alertinner "] p strong')
    PRICE_BOOK = (By.CSS_SELECTOR, '.product_main .price_color')
    PRICE_BOOK_IN_BASKET = (By.CSS_SELECTOR, '.basket-mini')

class BasePageLocators:
    BASKET = (By.CSS_SELECTOR,"span.btn-group")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    LANGUAGE = (By.CSS_SELECTOR, "[name='language']")
    BUTTION_LANGUAGE = (By.CSS_SELECTOR, "button[type = 'submit']")
    WEB_LANGUAGE = (By.CSS_SELECTOR, "html")

class BasketPageLocators():
    PRODUCT_FIELD = (By.CSS_SELECTOR,"#basket_formset") #Поле товара
    TEXT_NULL_BASKET = (By.CSS_SELECTOR, "div#content_inner p")