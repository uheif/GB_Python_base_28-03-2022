# Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск); атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.

import time


class TrafficLight:
    colors = {1: (f'\r\033[31m{"red"}', 7), 2: (f'\r\033[33m{"yellow"}', 2), 3: (f'\r\033[32m{"green"}', 5)}
    __color = None

    def running(self, color: int, work_time: int):
        TrafficLight.__color = color
        stop = time.perf_counter() + work_time
        while time.perf_counter() <= stop:
            if self.__color > 3:
                self.__color = 1
            print(TrafficLight.colors[self.__color][0], end='')
            time.sleep(TrafficLight.colors[self.__color][1])
            self.__color += 1


t_l = TrafficLight()
t_l.running(1, 20)
