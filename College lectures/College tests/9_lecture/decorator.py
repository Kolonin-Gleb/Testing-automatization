

def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper


@do_twice
def twice_2_params(str1, str2):
    print("В этой функции 2 параметра - {0} и {1}".format(str1, str2))


twice_2_params("1", "2")