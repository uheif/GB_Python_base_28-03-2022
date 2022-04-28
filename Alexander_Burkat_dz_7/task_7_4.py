# Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,
# но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

import os

data = os.walk(os.path.join('some_data'))

stat = {10 ** n: 0 for n in range(2, 6)}

for root, dirs, files in data:
    for file_name in files:
        file_size = os.stat(os.path.join(root, file_name)).st_size
        size = -1
        for max_size in stat:
            if size < file_size <= max_size:
                stat[max_size] += 1
                break
            size = max_size

print(stat)
