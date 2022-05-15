# Тесты для калькулятора на библиотеке pytest

import pytest

# Импорт исходников калькулятора
from calculator import *

# Тесты для калькулятора

def test_sum():
    firstNum = 2
    secondNum = 1
    assert sum(firstNum, secondNum) == 3

def test_multiplication():
    firstNum = 2
    secondNum = 5
    assert multiplication(firstNum, secondNum) == 10

@pytest.mark.smoke # Маркировка теста, как критически важного
def test_division():
    firstNum = 2
    secondNum = 0
    trirdNum = "not a number"
    fourthNum = 5
    assert division(firstNum, secondNum) == "Ошибка деления на 0"
    assert division(firstNum, trirdNum) == "Ошибка деления"
    assert division(firstNum, fourthNum) == 0.4

def test_substraction():
    firstNum = 2
    secondNum = 5
    assert substraction(firstNum, secondNum) == -3
    
# Для запуска всех тестов в терминале этой директории ввсети команду
# pytest

# Для регистрации меток создаются .ini файлы
# -- Для этого нужно будет создать файл pytest.ini и в нём зарегестрировать метки

# Для запуска критически важных тестов
# Запустить команду (флаг -m названием метки )
# pytest -s -v calculator_test.py

