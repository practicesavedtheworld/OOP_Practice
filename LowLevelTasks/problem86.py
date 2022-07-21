"""
Объявите класс Matrix (матрица) для операций с матрицами. Объекты этого класса должны создаваться командой:

m1 = Matrix(rows, cols, fill_value)

где rows, cols - число строк и столбцов матрицы;
    fill_value - заполняемое начальное значение элементов матрицы (должно быть число: целое или вещественное).
Если в качестве аргументов передаются не числа, то генерировать исключение:

raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')

Также объекты можно создавать командой:

m2 = Matrix(list2D)

где list2D - двумерный список (прямоугольный), состоящий из чисел (целых или вещественных).
Если список list2D не прямоугольный, или хотя бы один из его элементов не число, то генерировать исключение командой:

raise TypeError('список должен быть прямоугольным, состоящим из чисел')

Для объектов класса Matrix должны выполняться следующие команды:

matrix = Matrix(4, 5, 0)
res = matrix[0, 0] # возвращается первый элемент матрицы
matrix[indx1, indx2] = value # элементу матрицы с индексами (indx1, indx2) присваивается новое значение

Если в результате присвоения тип данных не соответствует числу, то генерировать исключение командой:

raise TypeError('значения матрицы должны быть числами')

Если указываются недопустимые индексы матрицы (должны быть целыми числами от 0 и до размеров матрицы), то генерировать исключение:

raise IndexError('недопустимые значения индексов')

Также с объектами класса Matrix должны выполняться операторы:

matrix = m1 + m2 # сложение соответствующих значений элементов матриц m1 и m2
matrix = m1 + 10 # прибавление числа ко всем элементам матрицы m1
matrix = m1 - m2 # вычитание соответствующих значений элементов матриц m1 и m2
matrix = m1 - 10 # вычитание числа из всех элементов матрицы m1

Во всех этих операция должна формироваться новая матрица с соответствующими значениями.
Если размеры матриц не совпадают (разные хотя бы по одной оси), то генерировать исключение командой:

raise ValueError('операции возможны только с матрицами равных размеров')
"""


def add(a, b):
    "Same as a + b."
    return a + b


def sub(a, b):
    "Same as a - b."
    return a - b


def mul(a, b):
    "Same as a * b."
    return a * b


class Matrix:

    def __init__(self, *args):
        if len(args) == 3:
            if not isinstance(args[0], int) and isinstance(args[1], int) and isinstance(args[2], (int.float)):
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
            self._table = [[args[2]] * args[1] for _ in range(args[0])]
            self._rows, self._cols = args[0], args[1]
            return
        if len(args) == 1:
            data = args[0]
            if not isinstance(data, list):
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            self._cols = len(data[0])
            for row in data:
                if not (len(row) == self._cols and all((isinstance(i, (int, float)) for i in row))):
                    raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            self._table = data.copy()
            self._rows = len(self._table)
            return
        raise TypeError('аргументами должно быть или прямоугольная матрица, либо три числа')

    def get_coords(self):
        return self._rows, self._cols

    def _is_index_correct(self, row, col):
        if not (0 <= row < self._rows and 0 <= col < self._cols):
            raise IndexError('недопустимые значения индексов')
        return True

    def __getitem__(self, coords):
        self._is_index_correct(*coords)
        return self._table[coords[0]][coords[1]]

    def __setitem__(self, coords, value):
        self._is_index_correct(*coords)
        if not isinstance(value, (int, float)):
            raise TypeError('значения матрицы должны быть числами')
        self._table[coords[0]][coords[1]] = value

    def __operation_on_matrix(self, other, func):
        if isinstance(other, (int, float)):
            return Matrix([[func(item, other) for item in row] for row in self._table])
        if isinstance(other, Matrix):
            if self.get_coords() != other.get_coords():
                raise ValueError('операции возможны только с матрицами равных размеров')
            return Matrix(
                [[func(item, other[i, j]) for j, item in enumerate(row)] for i, row in enumerate(self._table)])
        raise ValueError('операции возможны только с матрицами равных размеров или числом')

    def __add__(self, other):
        return self.__operation_on_matrix(other, add)

    def __sub__(self, other):
        return self.__operation_on_matrix(other, sub)

    def __mul__(self, other):
        return self.__operation_on_matrix(other, mul)


if __name__ == '__main__':
    mt = Matrix([[1, 2], [3, 4]])
    res = mt[0, 0]  # 1
    res = mt[0, 1]  # 2
    res = mt[1, 0]  # 3
    res = mt[1, 1]  # 4