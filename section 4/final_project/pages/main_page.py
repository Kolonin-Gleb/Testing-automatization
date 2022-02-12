# Импорт класса-страницы, необх. для описания класса MainPage
from .base_page import BasePage

# Импорт локаторов, для удобной работы с селекторами при изм. в верстке
from .locators import MainPageLocators

from selenium.webdriver.common.by import By

class MainPage (BasePage): # Наследование
    # Тест-действие
    def go_to_login_page(self):
        # *MainPageLocators.LOGIN_LINK - исп. инструкций для селектора, что описаны во внешнем файле
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK) 
        login_link.click()


    # Тест-проверка
    def should_be_login_link(self):
        # Исп. конструкции assert для выполнения проверки
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"


    