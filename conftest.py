import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help = 'Выбери браузер, Chrome или Firefox')
    parser.addoption('--language', action='store', default = "ru")

@pytest.fixture(scope='function')
def language(request):
    return request.config.getoption('language')

@pytest.fixture(scope="function")
def browser(request, language):
    browser_name = request.config.getoption('browser_name')
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option(
            "prefs", {"intl.accept_languages": language}
        )
        print(f"\nStart Chrome with language: {language}")
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.set_preference("intl.accept_languages", language)
        print(f"\nStart Firefox with language: {language}")
        browser = webdriver.Firefox(options=options)

    else:
        raise pytest.UsageError(
            "--browser_name should be chrome or firefox"
        )

    yield browser
    print("\nQuit browser")
    browser.quit()

