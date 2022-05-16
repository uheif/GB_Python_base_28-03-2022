# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
# Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру (например, словарь).
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.


class OfficeEq:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.name = f'{brand} {model}'

    def __str__(self):
        return self.name


class Printer(OfficeEq):
    """Привет, я принтер! Я умею распечатывать!"""

    @staticmethod
    def printing():
        print("Бзз! Бзз! Вжжуухх!")


class Scanner(OfficeEq):
    """Привет, я сканер! Я умею сканировать!"""

    @staticmethod
    def scanning():
        print("Жжжжжжжжжж! КхКх!")


class Copier(Printer, Scanner):
    """Привет, я ксерокс! Я умею сканировать и распечатывать!"""


class OfficeEqStorage:
    def __init__(self):
        self.storage = {}
        self.departments = {'панды': {}, 'носухи': {}, 'котики': {}}

    @staticmethod
    def amount_check(amount):
        if type(amount) is not int:
            print('Введите целое положительное число')
            exit(1)

    def getting(self, item, amount):
        self.amount_check(amount)
        if item.name not in self.storage:
            self.storage[item.name] = amount
        else:
            self.storage[item.name] += amount
        print(f"получен {item} в количестве {amount} шт.")

    def transfer(self, item, amount, department):
        if item in self.storage and self.storage[item] > 0:
            if amount <= self.storage[item]:
                self.storage[item] -= amount
                if not item in self.departments[department]:
                    self.departments[department][item] = amount
                else:
                    self.departments[department][item] += amount
                print(f'{department} получили {amount} {item}')
            else:
                print(f'На складе в наличии только {self.storage[item]} {item}')
        else:
            print('Такого наименования нет в наличии')


printer1 = Printer('Canon', '100500')
stor = OfficeEqStorage()
stor.getting(printer1, 53)
stor.getting(printer1, 1)
print(stor.storage)
stor.transfer('Canon 100500', 20, 'котики')
print(stor.storage, stor.departments)
stor.transfer('Canon 100500', 2, 'котики')
print(stor.storage, stor.departments)
stor.transfer('HP 42', 8, 'носухи')
stor.transfer('Canon 100500', 73, 'котики')
stor.getting(printer1, 'ы')
