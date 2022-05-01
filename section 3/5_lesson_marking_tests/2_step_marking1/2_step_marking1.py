import pytest
from selenium import webdriver

link = 'http://selenium1py.pythonanywhere.com/'

'''
Когда тестов много их делят на категории для удобства.
Это деление производится маркировкой тестов.

smoke - критические тесты
regression - второстепенные тесты (только перед релизом)
Можно маркировать тесты, что будут проводиться только в опр. браузере, к примеру.
''' 

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test...")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser")
    browser.quit()

class TestMainPage1():

    @pytest.mark.smoke # Маркировка теста, как критически важного
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
    
    @pytest.mark.win10 # Тест только для Windows 10
    @pytest.mark.regression # Маркировка теста, что нужно сделать перед релизом
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

# Запуск тестов осуществляется командой с флагом -m и названием метки
# pytest -s -v -m smoke 2_step_marking1.py
# ! При запуске возникнут предупреждения

'''
В PyTest рекомендуется регистрировать метки перед использованием.
Это необх., для исключения ситуаций, в которых тест
помечается несуществующей меткой и как результат
пропускается в тестах
'''
# Для регистрации меток создаются .ini файлы

'''
Для запуска всех тестов не имеющих заданную марку используется команда:
pytest -s -v -m "not smoke" 2_step_marking1.py

Для запуска тестов имеющих 1 из маркировок списка:
pytest -s -v -m "smoke or regression" 2_step_marking1.py

Для запуска тестов имеющих все марикровки списка:
pytest -s -v -m "regression and win10" 2_step_marking1.py
'''

