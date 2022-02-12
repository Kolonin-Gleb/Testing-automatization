# Поскольку я собираюсь тестировать всего одну страницу сайта не имеет смысла 
# создавать базовую страницу и наследоваться от неё

# Импорт искл., что будет обрабатываться
from selenium.common.exceptions import NoAlertPresentException
# Для решения загадки
import math

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

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert # Переход в окно alert
        x = alert.text.split(" ")[2] 
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try: # Попытка работы с 2 alert, что дает верный ответ
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    