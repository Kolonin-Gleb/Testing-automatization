# Тесты для калькулятора на библиотеке pytest

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

def test_division():
    firstNum = 2
    secondNum = 5
    assert division(firstNum, secondNum) == 0.4

def test_substraction():
    firstNum = 2
    secondNum = 5
    assert substraction(firstNum, secondNum) == -3
    
# Для запуска тестов в терминале этой директории ввсети команду 
# pytest

