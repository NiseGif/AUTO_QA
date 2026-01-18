import json
from linecache import cache

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions  as EC

from selenium.webdriver.common.by import By

path = "user.json"


class Test_reset():
    @pytest.mark.parametrize('site', [
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"
    ]
)
    def test_reset(self,browser, site):
        browser.get(site)

        #===============================================================
        wait = WebDriverWait(browser,10)

        switch = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".navbar__auth_login.st-link.st-link_style_button")))
        switch.click()

        with open('user.json', 'r') as file:
            user = json.load(file)

        login = wait.until(EC.visibility_of_element_located((By.ID, "id_login_email")))
        login.send_keys(user["login"])
        browser.find_element(By.ID, "id_login_password").send_keys(user["pwd"])

        button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "sign-form__btn.button_with-loader")))
        button.click()
        #==============================================================

        reset = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "again-btn.white")))
        reset.click()

        fake_confim = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='OK']")))
        fake_confim.click()



