# Файл селекторов для страниц

from selenium.webdriver.common.by import By

# Локаторы для страницы http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear
class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    
