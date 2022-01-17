import pytest # для запуска тестов
from selenium import webdriver # Для проведения тестов в браузере
from selenium.webdriver.common.by import By

# Для решения задач на страницах
import time
import math

def get_task_answer():
    return math.log(int(time.time()))

# Ссылки, по которым должен будет пройти тест необходимо подготовить.
# Сделать это можно через фикстуру
# @pytest.fixture(scope="function")
# def links():
#     print("\nStart preparing links for test.")
#     links = [
#     "https://stepik.org/lesson/236895/step/1",
#     "https://stepik.org/lesson/236896/step/1",
#     "https://stepik.org/lesson/236897/step/1",
#     "https://stepik.org/lesson/236898/step/1",
#     "https://stepik.org/lesson/236899/step/1",
#     "https://stepik.org/lesson/236903/step/1",
#     "https://stepik.org/lesson/236904/step/1",
#     "https://stepik.org/lesson/236905/step/1"
#     ]
#     yield links
#     print("End of preparing links for test.")

# Также обрабатываемую ссылку можно подавать через параметр.
# Для этого тесту необх. доб. декоратор с соотв. маркировкой.
links = [
"https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"
]

# Фикстура инициализирующая браузер для тестов
@pytest.fixture(scope="function")
def browser():
    print("\nStart browser for test.")
    browser = webdriver.Chrome()
    yield browser
    print("\nQuit browser. Test finished.")

# Тестом ниже я буду возращать фидбек с каждой страницы по ссылке
# Как можно возращать значения из теста? Если он запускается с исп. команды pytest?

# Маркировка для проведения тестов с различными ссылками
@pytest.mark.parametrize('link', links) # link - имя параметра. links - список возможных значения параметра.
def test_get_feedback(browser, link):
    browser.get(link)
    answer = get_task_answer()

    # Страница не загружается моментально. Нужно настроить задержку
    input_field = browser.find_element(By.CSS_SELECTOR, "textarea")
    input_field.send_keys(answer)
    # Поиск кнопки и нажатие
    button = browser.find_element(By.CSS_SELECTOR, "div.attempt__actions > button") # По кнопке и тексту на ней
    button.click()

    # Жду фидбек и возвращаю его

    # Читаю feedback
    feedback = browser.find_element(By.XPATH, '//*[@id="ember211"]/pre') 

    # В упавших тестах найдите кусочки послания. Тест должен падать, если текст в опциональном фидбеке не совпадает со строкой 
    # "Correct!" Соберите кусочки текста в одно предложение и отправьте в качестве ответа на это задание. 

    
    # Перед запуском следующего теста необх. закрыть тек. окно браузера




# Запуск тестов
# pytest -s -v 3_step_aliens.py

