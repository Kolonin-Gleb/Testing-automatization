# Код для настройки тестового окружения через
# через передачу параметров в cmd


import pytest
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

## Прием параметров из cmd
def pytest_addoption(parser):
    # Параметр для выбора браузера
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: chrome or firefox")

    # Параметр для выбора языка.
    # Будут запускаться тесты, для сайта на выбранном языке
    parser.addoption('--language', action='store', default='en', help="Choose language")

## Применение полученных параметров для подготовки тестового окружения
@pytest.fixture(scope="function")
# Функция выбора браузера
def browser(request):

    # Эта команда запрашивает значение параметра в cmd
    browser_name = request.config.getoption("browser_name")
    # request - встроенная фикстура, позволяющая получать данные о тек. запущенном тесте. Она полезна для сохранения доп. данных в отчёт и т.д.

    browser = None # По умолчанию браузер не выбран
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

'''
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
       print("\nstart firefox browser for test..")
       fp = webdriver.FirefoxProfile()
       fp.set_preference("intl.accept_languages", user_language)
       browser = webdriver.Firefox(firefox_profile=fp)
    else:
        print(f"{browser_name} wasn't implemented")
       #raise pytest.UsageError("please choose the language")
    yield browser
    print("\nquit browser..")
    browser.quit()
'''


