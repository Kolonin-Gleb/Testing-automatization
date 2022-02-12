# Тест с переходом к логину должен проходить с проверками.
# Поэтому нам необходим этот файл

# Импорт класса-страницы, необх. для описания класса LoginPage
from .base_page import BasePage

# Импорт локаторов для удобной работы с селекторами при изменении в верстке
from .locators import LoginPageLocators

## http://selenium1py.pythonanywhere.com/ru/accounts/login/ - страница описываемая классом
class LoginPage(BasePage):
    def should_be_login_page(self):
        # Вызов методов, чтобы убедиться, что мы на нужной странице (Выполнить тест)
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.currect_url == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/", "Not a login url" 

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина

        # TODO: Задать неверный селектор и посмотреть, как тест упадёт
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице

        # TODO: Задать неверный селектор и посмотреть, как тест упадёт
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "Register button is not presented"

