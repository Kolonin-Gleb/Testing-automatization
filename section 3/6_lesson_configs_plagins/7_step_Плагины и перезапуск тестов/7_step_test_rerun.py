# Плагины и перезапуск тестов

'''
Flaky-тесты или "мигающие тесты" - тесты, которые по независящим от нас внешним обстоятельствам или из-за
трудновоспроизводимых багов, могут иногда падать, хотя всё остальное время они проходят успешно.

Устранение таких багов может быть нерационнальным. 
Поэтому упавшие тесты имеет смысл перезапускать, чтобы 
убедиться, что он действительно нашел баг, а не упал случайно.
'''

# Для этого мы будем использовать плагин pytest-rerunfailures.
# pip install pytest-rerunfailures

'''
Чтобы указать количество перезапусков для каждого из упавших тестов, нужно добавить в командную строку параметр:
"--reruns n", где n — это количество перезапусков

параметр "--tb=line" добавляется для сокращения вывода с результатами теста
'''

# pytest -v --tb=line --reruns 1 --browser_name=chrome 7_step_test_rerun.py

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#magic_link") #неверный селектор


