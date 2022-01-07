from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    # # Поиск значения х
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text

    # Решение задачи
    y = calc(x)

    # Ввод полученного ответа

    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    
    # Скрол до button, checkbox и radiobutton
    browser.execute_script("button = document.getElementsByTagName('button')[0];button.scrollIntoView(true);")

    # Установка значений checkbox и radiobutton
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()
    # Нажатие кнопки
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

