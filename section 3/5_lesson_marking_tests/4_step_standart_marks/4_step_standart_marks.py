import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

'''
В PyTest существуют стандартные метки, которые позволяют 
пропускать тесты (@pytest.mark.skip)
запускать тесты с ожидаемым падением (@pytest.mark.xfail)

Стандартные метки не нужно регистрировать в pytest.ini
'''

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    @pytest.mark.skip(reason="Not important test, so let's skip it")
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

    # Когда баг устранят, тест будет отмечен как XPASS - неожиданно пройденный
    # Когда это случится метку xfail можно будет убрать, сделав его обычным тестом
    @pytest.mark.xfail(reason="fixing this bug right now") # reason="" - для вывода всопомгатеельного сообщения
    def test_guest_should_see_search_button_on_the_main_page(self, browser): 
        browser.get(link)
        browser.find_element_by_css_selector("button.favorite")
        # input.btn.btn-default - селектор для прохождения теста
        # button.favorite - селектор для провала теста


# Запуск тестов: pytest -v 4_step_standart_marks.py

# Запуск тестов с подсказками: pytest -rx -v 4_step_standart_marks.py

