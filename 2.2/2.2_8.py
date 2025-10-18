from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    first_name.send_keys("gvbhih")
    last_name = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    last_name.send_keys("gvbhih")
    email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    email.send_keys("gvbhih")

    upload = browser.find_element(By.ID,"file")
    file_directory = Path(__file__).parent.parent  # parent.parent = main/
    file_path_pathlib = file_directory / "2.1" / "text.txt"
    tmp = file_path_pathlib.resolve()   # Преобразуем в абсолютный путь
    assert os.path.exists(file_path_pathlib), f"Файл не найден: {file_path_pathlib}"

    upload.send_keys(str(tmp)) #??????

    button = browser.find_element(By.TAG_NAME,"button").click()

finally:
    time.sleep(7)
    browser.quit()