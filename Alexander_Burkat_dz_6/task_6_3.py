# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов
# и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь
# в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше
# записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из
# скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз
# меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# горные лыжи

from itertools import zip_longest
import json

with open('users.csv', 'w', encoding='UTF-8') as f, open('hobby.csv', 'w', encoding='UTF-8') as b:
    f.write('''Иванов,Иван,Иванович
Петров,Петр,Петрович'''
            )
    b.write('''скалолазание,охота
вело
фото'''
            )


with open('users.csv', 'r', encoding='UTF-8') as f, open('hobby.csv', 'r', encoding='UTF-8') as b:
    users = f.read().split('\n')
    hobby = b.read().split('\n')
    if len(users) - len(hobby) >= 0:
        dct = {user.replace(',', ' '): hob.split(',') if hob else None for user, hob in zip_longest(users, hobby)}
    else:
        exit(1)


with open ('users_hobby.json', 'w', encoding='UTF-8') as f:
    json.dump(dct, f, ensure_ascii=False)

