from selenium import webdriver
from selenium.webdriver.common.by import By
# Для явных ожиданий
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  browser = webdriver.Chrome()
  # говорим WebDriver искать каждый элемент в течение 5 секунд
  browser.implicitly_wait(5)

  browser.get("https://suninjuly.github.io/explicit_wait2.html")

  # говорим Selenium проверять в течение 12 секунд, пока цена не будет нужной
  price = WebDriverWait(browser, 12).until(
          EC.text_to_be_present_in_element((By.ID, "price"), "$100")
      )

  if price: # Если цена подходит
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    x = browser.find_element(By.ID, "input_value")
    x = x.text

    answer = calc(x)

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(answer)

    button = browser.find_element(By.ID, "solve")
    button.click()
  
finally:
  time.sleep(10)
  browser.quit()

