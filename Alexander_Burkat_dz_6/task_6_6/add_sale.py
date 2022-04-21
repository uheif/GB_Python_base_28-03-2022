from sys import argv


with open('bakery.csv', 'a+', encoding='UTF-8') as f:
    if f.tell() == 0:
        i = 1
    else:
        f.seek(0)
        i = int(f.readlines()[-1].split()[0]) + 1
    f.write(f'{i} {float(argv[1])}\n')
