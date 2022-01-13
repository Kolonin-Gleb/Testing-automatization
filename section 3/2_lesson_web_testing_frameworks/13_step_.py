from selenium import webdriver
import unittest

import time

# Класс с тестами
class Test(unittest.TestCase):
    # Запуск браузера. Будет выполнен перед прогоном всех тестов
    def setUp(self):
        self.driver = webdriver.Chrome()

    # Тест ссылки 1
    def test_registration_link1(self):
        link = "http://suninjuly.github.io/registration1.html"
        driver = self.driver
        driver.get(link)

        # Заполнение обязательных полей
        # Селекторы с прикрплением к label, чтобы точно указать необходимое поле
        input1 = driver.find_element_by_css_selector("div.first_block > div.form-group.first_class > input")
        input1.send_keys("Имя")
        input2 = driver.find_element_by_css_selector("div.first_block > div.form-group.second_class > input")
        input2.send_keys("Фамилия")
        input3 = driver.find_element_by_css_selector("div.first_block > div.form-group.third_class > input")
        input3.send_keys("Почта")

        time.sleep(2) # Задержка, чтобы увидеть заполнение нужных полей

        # Отправка заполненной формы
        button = driver.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = driver.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # Проверка, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Полученный текст со страницы не совпадает с ожидаемым результатом")

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)

    # Тест ссылки 2
    def test_registration_link2(self):
        link = "http://suninjuly.github.io/registration2.html"
        driver = self.driver
        driver.get(link)

        # Заполнение обязательных полей
        # Селекторы с прикрплением к label, чтобы точно указать необходимое поле
        input1 = driver.find_element_by_css_selector("div.first_block > div.form-group.first_class > input")
        input1.send_keys("Имя")
        input2 = driver.find_element_by_css_selector("div.first_block > div.form-group.second_class > input")
        input2.send_keys("Фамилия")
        input3 = driver.find_element_by_css_selector("div.first_block > div.form-group.third_class > input")
        input3.send_keys("Почта")

        time.sleep(2) # Задержка, чтобы увидеть заполнение нужных полей

        # Отправка заполненной формы
        button = driver.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = driver.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # Проверка, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Полученный текст со страницы не совпадает с ожидаемым результатом")

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)

    # Закрытие браузера. Будет выполнено после прогона всех тестов
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

