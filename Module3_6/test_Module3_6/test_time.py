import pytest
import json
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions  as EC

from selenium.webdriver.common.by import By




class Test():

    wrong_answers = []
    @classmethod
    def teardown_class(cls):
        if cls.wrong_answers:
            print("\nСобранный текст:")
            print("".join(cls.wrong_answers))

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
    def test_guest_should_see_login_link(self,browser, site):

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

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"learn-last-activity-dropdown__counter")))
    #==============================================================

        answer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "string-quiz__textarea")))
        #answer.clear()
        answer.send_keys(str(math.log(int(time.time()))))

        submit = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
        submit.click()

        hint = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
        )

        hint_text = hint.text
        assert hint_text == "Correct!", f"Expected 'Correct!', but got '{hint_text}'"

        if hint_text != "Correct!":
            self.wrong_answers.append(hint_text)


