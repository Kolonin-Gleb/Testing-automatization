# Методы калькулятора

def sum(a, b):
    return a + b

def multiplication(a, b):
    return a * b

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Ошибка деления на 0"
    except:
        return "Ошибка деления"
    
def substraction(a, b):
    return a - b
