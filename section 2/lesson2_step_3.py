from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Поиск значения х
    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    num1 = x_element.text

    x_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    num2 = x_element.text

    sum = int(num1) + int(num2)

    # Решение задачи
    y = calc(sum)


    # Открытие списка
    browser.find_element_by_tag_name("select").click()
    # Выбор элемента с верным ответом
    browser.find_element_by_css_selector(f"[value='{sum}']").click()

    # Выбор кнопки и уточнение по 2 её классам
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default") 
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

