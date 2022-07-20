"""
Объявите класс с именем Triangle, объекты которого создаются командой:

tr = Triangle(a, b, c)

где a, b, c - длины сторон треугольника (числа: целые или вещественные).
В классе Triangle объявите следующие дескрипторы данных:

a, b, c - для записи и считывания длин сторон треугольника.

При записи нового значения нужно проверять, что присваивается положительное число (целое или вещественное).
Иначе, генерируется исключение командой:

raise ValueError("длины сторон треугольника должны быть положительными числами")

Также нужно проверять, что все три стороны a, b, c могут образовывать стороны треугольника.

Иначе генерируется исключение командой:

raise ValueError("с указанными длинами нельзя образовать треугольник")

Наконец, с объектами класса Triangle должны выполняться функции:

len(tr) - возвращает периметр треугольника, приведенный к целому значению с помощью функции int();
tr() - возвращает площадь треугольника (можно вычислить по формуле Герона)
"""


class TDescr:
    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.name, value)
        else:
            raise ValueError("длины сторон треугольника должны быть положительными числами")


class Triangle:
    a = TDescr()
    b = TDescr()
    c = TDescr()

    def __init__(self, a, b, c):
        if a < b+c and  b < a+c and c < a+b :
            self.a = a
            self.b = b
            self.c = c
        else:
            raise ValueError("с указанными длинами нельзя образовать треугольник")

    def check(self):
        return self.a < self.b + self.c and self.b < self.a + self.c and self.c < self.a + self.b

    def __len__(self):
        if self.check():
            return sum([self.a, self.b, self.c])
        else:
            raise ValueError("с указанными длинами нельзя образовать треугольник")

    def __call__(self, *args, **kwargs):
        # s = sqrt(p * (p-a) * (p-b) * (p-c))
        if self.check():
            p = len(self) // 2
            return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        else:
            raise ValueError("с указанными длинами нельзя образовать треугольник")


if __name__ == '__main__':
    tr = Triangle(5, 4, 3)
    assert tr.a == 5 and tr.b == 4 and tr.c == 3, "дескрипторы вернули неверные значения"

    try:
        tr = Triangle(-5, 4, 3)
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError"

    try:
        tr = Triangle(10, 1, 1)
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError"

    tr = Triangle(5, 4, 3)
    assert len(tr) == 12, "функция len вернула неверное значение"
    assert 5.9 < tr() < 6.1, "метод __call__ вернул неверное значение"
