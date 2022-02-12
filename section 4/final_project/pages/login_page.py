# Тест с переходом к логину должен проходить с проверками.
# Поэтому нам необходим этот файл

# Импорт класса-страницы, необх. для описания класса LoginPage
from .base_page import BasePage

# Импорт локаторов для удобной работы с селекторами при изменении в верстке
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        # Заглушки для методов проверок
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert True

