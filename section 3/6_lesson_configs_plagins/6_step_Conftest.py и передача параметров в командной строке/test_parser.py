link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

'''
При запуске этого теста без параметра будет ошибка.
Т.к. параметр по умолчанию в каком браузере провести тест не задан, 
фикстура не подготовит браузер, что необходим для проведения теста.

# Запуск теста без параметра
pytest -s -v test_parser.py

# Запуск теста с параметром
pytest -s -v --browser_name=chrome test_parser.py



'''