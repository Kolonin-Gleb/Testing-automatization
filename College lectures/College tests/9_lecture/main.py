import functools


def my_decorator(func):
    @functools.wraps(func)
    def wrapper():
        functools.wraps(func)
        print("Начало декоратора", wrapper.__name__)
        func()
        print("Конец выполнения декоратора", wrapper.__name__)
    return wrapper


# Эту функцию мы будем декорировать
def my_func():
    print("Выполнение функции:", my_func.__name__)
    print()

# my_func()
#
# my_first_decorator = my_decorator(my_func)
# print(type(my_first_decorator))
# my_first_decorator()


@my_decorator
def my_func(arg1):
    print("Выполнение функции: ", my_func.__name__, 'с arg:', arg1)


my_func(3)
