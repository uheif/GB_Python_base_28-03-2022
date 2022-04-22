# (вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта:
# передаём ему номер записи и новое значение. При этом файл не должен читаться целиком — обязательное требование.
# Предусмотреть ситуацию, когда пользователь вводит номер записи, которой не существует.

from sys import argv

id = argv[1]
id_exists = False
price = argv[2]

with open('bakery.csv', 'br+') as f:
    for line in f:
        if line.decode().split()[0] == id:
            id_exists = True
            f.seek(-len(line), 1)
            new_line = f'{id} {float(price)}'
            dif = len(line.decode()) - len(new_line) - 1
            if dif >= 0:
                f.write((new_line + ' ' * dif).encode())
            else:
                print('''упс, я не дослушал конец лекции и не сделал в шестом задании записи фиксированной длины :(
попробуйте ввести число покороче''')
            break

if not id_exists:
    print('Такой записи не существует')
