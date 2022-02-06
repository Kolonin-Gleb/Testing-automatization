'''
Настройка тестового окружения через передачу параметров в cmd

Это делается с помощью встроенной функции pytest_addoption и фикстуры request

'''

import pytest
from selenium import webdriver


# Встроенная функция
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
    help="Choose browser: chrome or firefox")
    # default="chrome" - сделает браузером по умолчанию chrome


# Фикстура инициализирующая браузер, для проведения теста, согласно выбору пользователя
@pytest.fixture(scope="function")
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

