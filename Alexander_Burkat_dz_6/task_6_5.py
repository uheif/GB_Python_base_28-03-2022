# Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было
# задать имя обоих исходных файлов и имя выходного файла. Проверить работу скрипта.
from sys import argv

with open(argv[1], 'r', encoding='UTF-8') as f, open(argv[2], 'r', encoding='UTF-8') as b:
    with open(argv[3], 'a', encoding='UTF-8') as c:
        for line_f in f:
            c.write(f'{line_f.strip().replace(",", " ")}: {b.readline().strip() or None}\n')