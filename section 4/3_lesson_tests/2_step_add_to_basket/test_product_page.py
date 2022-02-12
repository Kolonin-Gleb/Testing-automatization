# Добавить новый файл для тест-кейсов, связанных со страницей ProductPage.


# Импорт страницы, на которой будут проводиться тесты
from pages.product_page import ProductPage # Нужна ли . перед pages?

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()

    # Нажать на кнопку добавления товара
    page.add_to_basket()

    page.solve_quiz_and_get_code()


# Проверка работоспособности тестов
# -s - чтобы увидеть вывод в консоль
# -v - многословные пояснения
# --tb=line - вывод 1 строки пояснений
# Команда для запуска проверок
# pytest -s -v --tb=line test_product_page.py

