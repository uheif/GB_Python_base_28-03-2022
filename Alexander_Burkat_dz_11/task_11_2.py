# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class MyExc(Exception):
    def __init__(self, message):
        self.message = message

a = int(input('Введите делимое: '))
b = int(input('Введите делитель: '))

try:
    if not b:
        raise MyExc('На ноль делить нельзя')
except MyExc as e:
    print(e)
else:
    print(round(a / b, 2))