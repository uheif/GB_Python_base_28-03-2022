# Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса; атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна; проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500т.

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_calc(self, weight=25, depth=1):
        return round(self._length * self._width * weight * depth / 1000, 2)


r = Road(10, 15)
print(r.asphalt_calc())  # 3,75
