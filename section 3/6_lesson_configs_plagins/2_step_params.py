import pytest
from selenium import webdriver

# Фикстура инициализирующая браузер для тестов.
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test...")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser...")
    browser.quit()

# Тест
# @pytest.mark.parametrize('language', ["ru", "en-gb"]) # В [] указывается список параметров, с которыми будет запускаться тест.
# def test_guest_should_see_login_link(browser, language):
#     link = f"http://selenium1py.pythonanywhere.com/{language}/"
#     browser.get(link)
#     browser.find_element_by_css_selector("#login_link")

# Запуск теста
# pytest -s -v 2_step_params.py

# После запуска в [] будут указан параметр, с которым был запущен тест
# C каждым параметром тест будет запущен отдельно

# Параметры можно задавать для всего тестового класса.
# Это позволит запустить все тесты в нём с каждым из указанных параметров.

@pytest.mark.parametrize('language', ["ru", "en-gb"])
class TestLogin:
    def test_guest_should_see_login_link(self, browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        browser.get(link)

        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_navbar_element(self, browser, language):
        pass

# В данном случае каждый тест класса будет запущен 2 раза
