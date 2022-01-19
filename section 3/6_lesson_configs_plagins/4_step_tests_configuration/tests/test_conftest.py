link = "http://selenium1py.pythonanywhere.com/"

# browser - будет проинициализирован файлом
# conftest.py, который конфигурирует все тесты в поддиректориях от своего положения
def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

'''
PyTest автоматически находит и подгружает файлы
conftest.py, которые находятся в директории с тестами

Будьте внимательны и следите, чтобы не было разных conftest во вложенных друг в друга директориях
Если такое произойдёт, то применится оба conftest.py файла и возникнут непредсказуемые ошибки!
'''

