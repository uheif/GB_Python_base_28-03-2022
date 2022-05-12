# Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма(2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    cloth = 0

    @abstractmethod
    def __init__(self, name):
        self.name = name


    @abstractmethod
    def rate(self):
        pass


class Coat(Clothes):
    def __init__(self, name, v):
        super().__init__(name)
        self.v = v
        Clothes.cloth += self.rate  # наверное было бы логично это прописать в родительском классе, но не получилось

    @property
    def rate(self):
        return round((self.v / 6.5 + 0.5), 2)


class Suit(Clothes):
    def __init__(self, name, h):
        super().__init__(name)
        self.h = h
        Clothes.cloth += self.rate

    @property
    def rate(self):
        return round((2 * self.h + 0.3), 2)


x = Coat('пальтшко', 46)
print(x.rate)

y = Suit('костюмчик', 180)
print(y.rate)

print(Clothes.cloth)
