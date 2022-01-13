import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Фикстуры, возращающие значение, финализаторы, области видимости и автоиспользование фикстур

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture() # scope="class"
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser # Финализатор - ключево слово yield
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()
    '''
    В pytest есть встроенный сборщик мусора. 
    Поэтому закрытие браузера произойдёт даже, если не указывать это явно.
    
    ВАЖНО! явно указывать закрытие окон браузера, т.к. если их будет открыто много, а сборщик мусора не приступит к очистке, то кончится ОЗУ
    '''

@pytest.fixture(autouse=True)
def prepare_data():
    print()
    print("preparing some critical data for every test")
'''
При описании фикстуры можно указать дополнительный параметр autouse=True,
который укажет, что фикстуру нужно запустить для каждого теста даже без явного вызова: 
'''

class TestMainPage1():
    # вызов фикстуры в тесте, после её получения в качестве параметра
    def test_guest_should_see_login_link(self, browser):
        print("start test 1")
        browser.get(link)
        browser.find_element(By.ID, "login_link")
        print("finish test 1")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("start test 2")
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        print("finish test 2")

'''
Для фикстур можно задавать область покрытия фикстур с пощью аргумента scope. Допустимые значения: “function”, “class”, “module”, “session”.
Соответственно, фикстура будет вызываться один раз для тестового метода, один раз для класса, один раз для модуля или один раз для всех тестов,
запущенных в данной сессии. 
Запустим все наши тесты из класса TestMainPage1 в одном браузере для экономии времени, задав scope="class" в фикстуре browser:
'''


