# Задача - протестировать код функций, для работы с API
# Использя pytest

import pytest

# Импорт исходников функций для взаимодействия с API

from API_functions import *


def test_get_key():
    # Успешное получение API ключа
    assert get_key('koloninGS20@st.ithub.ru','RwAWCy2AKsxWTga') == "some key"
    # Неудачное получение API ключа
    assert get_key('koloninGS20@st.ithub.ru','RwAWCy2AKsxWTga') == json.decoder.JSONDecodeError
    

'''
Для запуска всех тестов в терминале этой директории ввсети команду
pytest -s API test.py
'''
