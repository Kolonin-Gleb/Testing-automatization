# # тест для основной страницы

# # Написаный не по Page Object
# from time import sleep

# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     browser.get(link)
#     login_link = browser.find_element_by_css_selector("#login_link")
#     login_link.click()
#     sleep(3)

# # Проверка работоспособности теста. 
# # pytest -v --tb=line test_main_page.py

# Написанный по Page Object
from .pages.main_page import MainPage # Действия между пользователем и MainPage

from .pages.login_page import LoginPage # Действия между пользователем и LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open() # Открытие страницы, на которой следует провести тест

    # Переход на страницу логина
    page.go_to_login_page()

    # Создание объекта представляющего страницу, на которую был совершен преход
    # Передаём browser и url, соответствующие странице логина, на которую был совершен переход 
    login_page = LoginPage(browser, browser.current_url)
    # Проверка, что попали туда, куда нужно. 
    # Чтобы отработал этот последний этап теста данный метод должен верно отработать
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    # С новой ссылокой этот тест упадёт, поэтому нужно будет менять селектор в методе MainPage.
    # Чтобы не менять селектор во всех методах MainPage Селекторы объявляются в 
    # отдельном файле locators.py
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

# Нужно написать тест для страницы LoginPage?


# Проверка работоспособности тестов
# pytest -v --tb=line test_main_page.py

