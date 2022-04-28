# Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую;
# можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов?
# Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

from functools import wraps


def type_logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        log = [f'{arg}: {type(arg)}' for arg in args]
        if kwargs:
            log.extend([f'{value}: {type(value)}' for value in kwargs.values()])
        print(f'{func.__name__}({", ".join(log)})')
        return result

    return wrapper


@type_logger
def calc_cube(a, b, c=45, d=''):
    return a, b, c, d


calc_cube(5, 6.34, c=False, d='i')
