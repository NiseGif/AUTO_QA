import json

import pytest
from page.register_page import Register
from pathlib import Path

BASE_VALID = Path('C:/Users/niseg/OneDrive/Рабочий стол/AT/first/main/test/test_registration_page.py').resolve().parent.parent / 'data' / 'valid_users.json'
BASE_INVALID = Path('C:/Users/niseg/OneDrive/Рабочий стол/AT/first/main/test/test_registration_page.py').resolve().parent.parent / 'data' / 'invalid_users.json'

with open(BASE_VALID,'r', encoding='utf-8') as f:
    test_valid_data = json.load(f)

@pytest.mark.parametrize(
    "email,password",[
        (user['email'],user['pass']) for user in test_valid_data])
def test_registration(browser, email, password):
    link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = Register(browser,link)
    page.open()
    page.add_email(email)
    page.add_password_and_confirm(password)