from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  browser = webdriver.Chrome()
  # говорим WebDriver искать каждый элемент в течение 5 секунд
  browser.implicitly_wait(5)

  browser.get("http://suninjuly.github.io/cats.html")

  button = browser.find_element_by_id("button")
  # button.click()

finally:
  time.sleep(10)
  browser.quit()

