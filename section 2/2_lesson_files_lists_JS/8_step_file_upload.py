from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import os # для загрузки файла

try: 
  browser = webdriver.Chrome()
  link = "https://suninjuly.github.io/file_input.html"
  browser.get(link)

  # Селекторы по атрибутам name
  input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']") 
  input1.send_keys("Имя")
  input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']") 
  input2.send_keys("Фамилия")
  input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']") 
  input3.send_keys("Почта")

  # Создание файла с фейкровой биографией
  with open("fake-bio.txt", "w") as file:
    content = file.write("my fake bio")

  # Прикрепление файла
  
  input_file = browser.find_element_by_css_selector("#file")

  current_dir_path = os.path.abspath(os.path.dirname(__file__))
  file_path = os.path.join(current_dir_path, 'fake-bio.txt')
  input_file.send_keys(file_path)

  time.sleep(2) # Задержка, чтобы увидеть заполнение нужных полей

  # Отправка заполненной формы
  button = browser.find_element_by_css_selector("button.btn")
  button.click()

finally:
  # ожидание чтобы визуально оценить результаты прохождения скрипта
  time.sleep(10)
  # закрываем браузер после всех манипуляций
  browser.quit()

