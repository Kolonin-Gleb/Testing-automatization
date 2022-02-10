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
# from .pages.base_page import BasePage # Импорт класса, описывающего возможные действия между пользователем и страницей

# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = BasePage(browser, link)
#     page.open()

# # Проверка работоспособности теста. 
# # pytest -v --tb=line test_main_page.py

