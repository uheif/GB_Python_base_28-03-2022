#  Реализуйте базовый класс Car. У класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы:  go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def to_go(self):
        print('go-go!')

    def stop(self):
        print('stop!')

    def turn(self, direction):
        print(f'turning {direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        print(self.speed if self.speed <= 60 else f'{self.speed}! Превышаете, молодой человек!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(self.speed if self.speed <= 60 else f'{self.speed}! Превышаешь, Петрович!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name)
        self.is_police = is_police


car1 = TownCar(220, 'red', 'ласточка')
car1.to_go()
car1.show_speed()
car1.stop()
print(car1.name, car1.color)

car2 = PoliceCar(300, 'black-white', 'bluesmobile')
print(car2.is_police)
print(car2.name, car2.speed)
