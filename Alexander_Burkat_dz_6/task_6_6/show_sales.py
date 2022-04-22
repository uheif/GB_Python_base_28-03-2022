from sys import argv


def show(start=0, end=0):
    line = f.readline()
    while line and int(line.split()[0]) < start:
        line = f.readline()
    while line and (int(line.split()[0]) <= end or not end):
        print(line.split()[1])
        line = f.readline()


lena = len(argv)

with open('bakery.csv', 'r', encoding='UTF-8') as f:
    if lena == 1:
        show()
    elif lena == 2:
        show(int(argv[1]))
    elif lena == 3:
        show(int(argv[1]), int(argv[2]))
