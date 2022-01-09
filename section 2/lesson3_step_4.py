# webdriver = набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()
    # confirm.dismiss()

    x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x.text

    answer = calc(x)

    input_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_field.send_keys(answer)

    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

