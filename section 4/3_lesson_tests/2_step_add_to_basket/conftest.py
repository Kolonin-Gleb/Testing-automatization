# Код для настройки тестового окружения (Инициализация браузера)

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
# Функция инициализации браузера
def browser(request):
    # Эта команда запрашивает значение параметра в cmd
    browser_name = request.config.getoption("browser_name")
    # request - встроенная фикстура, позволяющая получать данные о тек. запущенном тесте.
    # Она полезна для сохранения доп. данных в отчёт и т.д.

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
