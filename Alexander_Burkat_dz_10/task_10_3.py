class Cell:
    def __init__(self, nucl: int):
        self.nucl = nucl

    def __str__(self):
        return str(self.nucl)

    def __add__(self, other):
        return Cell(self.nucl + other.nucl)

    def __sub__(self, other):
        if self.nucl > other.nucl:
            return Cell(self.nucl - other.nucl)
        else:
            return 'Неверное количество ячеек'

    def __mul__(self, other):
        return Cell(self.nucl * other.nucl)

    def __floordiv__(self, other):
        return Cell(self.nucl // other.nucl)

    def make_order(self, row):
        return ''.join([f'{"*" * row}\\n' for _ in range(self.nucl // row - 1)]) + f'{"*" * row}' + \
               f'{"*" * (self.nucl % row)}'

x = Cell(17)
y = Cell(21)
print(x + y)
print(x - y)
print(y // x)
print(y.make_order(4))
