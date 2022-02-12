# Чтобы не изменять селектор в нескольких местах их выносят во внешний файл.
# Этот файл содержит используемые селекторы

from selenium.webdriver.common.by import By

# Локаторы для страницы http://selenium1py.pythonanywhere.com/ru/
class MainPageLocators():
    # Это кортеж, который содержит в себе информацию как искать и что искать. 
    # Он используется в селекторах, а при изменении в верстке,
    # нужно будет изменить только как искать в этом файле
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

# Локаторы для страницы http://selenium1py.pythonanywhere.com/ru/accounts/login/
class LoginPageLocators():
    # Кнопка Войти на форме логина
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login_form > button")

    # Кнопка зарегистрироваться на форме регистрации
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

