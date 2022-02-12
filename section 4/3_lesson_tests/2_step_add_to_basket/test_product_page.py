# Добавить новый файл для тест-кейсов, связанных со страницей ProductPage.

# Импорт искл., что будет обрабатываться
from selenium.common.exceptions import NoAlertPresentException

import math

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


# Импорт страницы, на которой будут проводиться тесты
from pages.product_page import ProductPage # Нужна ли . перед pages?

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()

    # Нажать на кнопку добавления товара
    page.add_to_basket()

    # Далее нужно решить задачку из alert
    solve_quiz_and_get_code()

# Проверка работоспособности тестов
# -s - чтобы увидеть вывод в консоль
# -v - многословные пояснения
# --tb=line - вывод 1 строки пояснений
# Команда для запуска проверок
# pytest -s -v --tb=line test_product_page.py

