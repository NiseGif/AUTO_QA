from selenium.webdriver.common.by import By
from page.basket_page import BasketPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/"
    page = BasketPage(browser,link)
    page.open()
    page.go_to_basket_page()
    page.check_null_basket()
    page.check_null_basket_text()