import pytest
from page.basket_page import BasketPage
from page.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser,link)
    page.open()
    page.go_to_login_page()

def test_guest_should_see_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser,link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "https://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser,link)
    page.open()
    page.go_to_basket_page()
    page.check_null_basket()
    page.check_null_basket_text()

@pytest.mark.parametrize('language',["ru",
                                     "en-gb",
                                     "ar",
                                     "ca",
                                     "cs"])
def test_change_language(browser,language):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    page = MainPage(browser,link)
    page.open()
    page.should_be_change_language()
    page.change_language(language)