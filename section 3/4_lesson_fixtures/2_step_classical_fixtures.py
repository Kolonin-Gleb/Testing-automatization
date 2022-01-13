from selenium import webdriver

# Классические фикстуры

link = "http://selenium1py.pythonanywhere.com/"

# Фикстуры в контексте PyTest — это вспомогательные функции для наших тестов, которые не являются частью тестового сценария.

# Классический способ работы с фикстурами — создание setup- и teardown-методов в файле с тестами

# Можно создавать фикстуры для модулей, классов и отдельных функций.

# Давайте попробуем написать фикстуру для инициализации браузера, который мы затем сможем использовать в наших тестах.

# Тест-сьют (Test Suite, TS) – комплект тестовых наборов для исследуемого компонента или системы.
# Обычно в нём постусловие одного теста используется в качестве предусловия для последующего (Feature Testing)

# Здесь Тест-сьюты оформлены в виде классов
'''
# 1 - Создание экземпляра браузера и его закрытие только один раз для всех тестов первого тест-сьюта 
class TestMainPage1():
    # @classmethod - декоратор, позволюящий обратиться к классу, а не объекту.

    # Запуск 1 раз перед всеми тестами
    @classmethod
    def setup_class(cls):
        print("\nstart browser for test suite..")
        cls.browser = webdriver.Chrome()

    # Тесты начнут выполняться отсюда
    def test_guest_should_see_login_link(self):
        print('start test link 1')
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print('start test basket 1')
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")

    # Запуск 1 раз после всех тестов
    @classmethod
    def teardown_class(cls):
        print("quit browser for test suite..")
        cls.browser.quit()
    # Методы класса привязаны к самому классу, а не его экземпляру.
    # Они могут менять состояние класса, что отразится на всех объектах этого класса, но не могут менять конкретный объект.
'''

# 2 - создание браузера для каждого теста во втором тест-сьюте
# Минус: Такой подход займет в 2 раза больше времени для прохождения тестов
# Плюс: Данные и кэш, оставшиеся от запуска предыдущего теста, могут влиять на результаты выполнения следующего теста, поэтому
# лучше всего запускать отдельный браузер для каждого теста, чтобы тесты были стабильнее. К тому же если вдруг браузер зависнет
# в одном тесте, то другие тесты не пострадают, если они запускаются каждый в собственном браузере.


class TestMainPage2():
    # Запуск перед каждым тестом
    def setup_method(self):
        print("start browser for test..")
        self.browser = webdriver.Chrome()
    # Запуск после каждого теста
    def teardown_method(self):
        print("quit browser for test..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print('start test link 2')
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print('start test basket 2')
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")

