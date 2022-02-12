# Поскольку я собираюсь тестировать всего одну страницу сайта не имеет смысла 
# создавать базовую страницу и наследоваться от неё

# Подключение локаторов
from .locators import ProductPageLocators

# Страница описанная классом:
# http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear
class ProductPage:
    def __init__(self, browser, url, timeout=10): # timeout - необходим для настройки неявного ожидания.
        # Ожидания нужны, т.к. сайты и их эл. могут загружаться с задержками
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    # метод для добавления товара в корзину
    def add_to_basket(self):
        # Выполнить нажатие на кнопку добавления товара
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

