import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nStart browser for test")
    ### Настройки для более чистого вывода в консоль
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    ###
    browser = webdriver.Chrome(options=options) # Применение настроек
    yield browser
    print("\nQuit browser")
    browser.quit()

