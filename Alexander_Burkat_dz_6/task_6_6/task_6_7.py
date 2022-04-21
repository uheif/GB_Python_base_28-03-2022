# (вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта:
# передаём ему номер записи и новое значение. При этом файл не должен читаться целиком — обязательное требование.
# Предусмотреть ситуацию, когда пользователь вводит номер записи, которой не существует.


id = '2'
id_exists = False
price = '0'
position = 0

with open('bakery.csv', 'br+') as f:
    line = f.readline().decode()
    while line:
        position += f.tell()
        if line.split()[0] == id:
            id_exists = True
            f.seek(position - f.tell())
            new_line = f'{id} {float(price)}'
            f.write((new_line + ' ' * (len(line) - len(new_line) - 1)).encode())
            break
        line = f.readline().decode()

if not id_exists:
    print('Такой записи не существует')
