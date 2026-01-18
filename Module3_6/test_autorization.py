import json
import pytest
from joblib.testing import fixture
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions  as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://stepik.org/lesson/236895/step/1"
path = "user.json"

@pytest.fixture
def open_file():
    with open('user.json', 'r') as file:
        return json.load(file)

class Test_1():
    def test_inpt(self,browser,open_file):

        browser.get(link)

        wait = WebDriverWait(browser,10)

        answer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ember-text-area")))
        answer.send_keys("123")

        submit = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
        submit.click()

        switch = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".light-tabs__switch")))
        switch.click()

        login = wait.until(EC.visibility_of_element_located((By.ID, "id_login_email")))
        login.send_keys(open_file["login"])
        browser.find_element(By.ID, "id_login_password").send_keys(open_file["pwd"])

        browser.find_element(By.CSS_SELECTOR, ".button_with-loader").click()