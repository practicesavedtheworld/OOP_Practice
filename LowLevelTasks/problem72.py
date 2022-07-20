"""
Объявите в программе класс Vector, объекты которого создаются командой:

v = Vector(x1, x2, x3,..., xN)

где x1, x2, x3,..., xN - координаты вектора (числа: целые или вещественные).

С каждым объектом класса Vector должны выполняться операторы:

v1 + v2 # суммирование соответствующих координат векторов
v1 - v2 # вычитание соответствующих координат векторов
v1 * v2 # умножение соответствующих координат векторов

v1 += 10 # прибавление ко всем координатам вектора числа 10
v1 -= 10 # вычитание из всех координат вектора числа 10
v1 += v2
v2 -= v1

v1 == v2 # True, если соответствующие координаты векторов равны
v1 != v2 # True, если хотя бы одна пара координат векторов не совпадает

При реализации бинарных операторов +, -, * следует создавать новые объекты класса Vector с новыми (вычисленными) координатами.
При реализации операторов +=, -= координаты меняются в текущем объекте, не создавая новый.

Если число координат (размерность) векторов v1 и v2 не совпадает, то при операторах +, -, * должно генерироваться исключение командой:

raise ArithmeticError('размерности векторов не совпадают')
"""


class Vector:
    def __init__(self, *args):
        self.coords = list(args)

    def lencheck(self, oth):
        if len(self.coords) == len(oth.coords):
            return True
        else:
            raise ArithmeticError('размерности векторов не совпадают')

    def __add__(self, other):
        if isinstance(other, Vector):
            if self.lencheck(other):
                return Vector(*map(sum, zip(self.coords, other.coords)))
        else:
            return self.__radd__(other)

    def __radd__(self, other):
        return Vector(*[i + other for i in self.coords])

    def __sub__(self, other):
        if isinstance(other, Vector):
            if self.lencheck(other):
                return Vector(*map(self.ssub, zip(self.coords, other.coords)))
        else:
            return self.__rsub__(other)

    def __rsub__(self, other):
        return Vector(*[i - other for i in self.coords])

    def __mul__(self, other):
        if isinstance(other, Vector):
            if self.lencheck(other):
                return Vector(*map(self.mmul, zip(self.coords, other.coords)))
        else:
            return self.__rmul__(other)

    def __rmul__(self, other):
        return Vector(*[i * other for i in self.coords])

    def __eq__(self, other):
        return self.coords == other.coords

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            s = tuple([i + other for i in self.coords])
            return Vector(*s)
        elif isinstance(other, Vector):
            self.coords = tuple(map(sum, zip(self.coords, other.coords)))
            return Vector(*self.coords)

    def __isub__(self, other):
        if isinstance(other, (int, float)):
            s = tuple([i - other for i in self.coords])
            return Vector(*s)
        elif isinstance(other, Vector):
            self.coords = tuple(map(self.ssub, zip(self.coords, other.coords)))
            return Vector(*self.coords)

    def __imul__(self, other):
        if isinstance(other, (int, float)):
            s = tuple([i * other for i in self.coords])
            return Vector(*s)
        elif isinstance(other, Vector):
            self.coords = list(map(self.mmul, zip(self.coords, other.coords)))
            return Vector(*self.coords)

    @staticmethod
    def ssub(ar):
        return ar[0] - ar[1]

    @staticmethod
    def mmul(ar):
        return ar[0] * ar[1]


if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    print((v1 + v2).coords)  # [5, 7, 9]
    print((v1 - v2).coords)  # [-3, -3, -3]
    print((v1 * v2).coords)  # [4, 10, 18]

    v1 += 10
    print(v1.coords)  # [11, 12, 13]
    v1 -= 10
    print(v1.coords)  # [1, 2, 3]
    v1 += v2
    print(v1.coords)  # [5, 7, 9]
    v2 -= v1
    print(v2.coords)  # [-1, -2, -3]

    print(v1 == v2)  # False
    print(v1 != v2)  # True