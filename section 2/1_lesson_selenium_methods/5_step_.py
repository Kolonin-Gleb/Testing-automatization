from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Поиск значения х

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text

    # Решение задачи
    y = calc(x)

    # Ввод полученного ответа

    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    
    # Установка значений checkbox и radiobutton

    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default") # Выбор кнопки и уточнение по 2 её классам
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

