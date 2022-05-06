# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, day: int, month: int, year: int):  # не по условию, но иначе я не понимаю зачем метод класса
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return '-'.join(map(str, [self.day, self.month, self.year]))

    @classmethod
    def date_int(cls, str_date):
        """Date from string"""
        day, month, year = map(int, str_date.split('-'))
        return Date(day, month, year)

    @staticmethod
    def check(day, month, year):
        return 0 < day <= 31, 0 < month <= 12, 0 < year < 2022


my_date = Date.date_int('02-04-1983')
print(my_date, my_date.check(my_date.day, my_date.month, my_date.year))
