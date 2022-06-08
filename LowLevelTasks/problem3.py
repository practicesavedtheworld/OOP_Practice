"""
Объявите три класса геометрических фигур: Line, Rect, Ellipse. Должна быть возможность создавать объекты
каждого класса, следующими командами:

g1 = Line(a, b, c, d)
g2 = Rect(a, b, c, d)
g3 = Ellipse(a, b, c, d)

Здесь в качестве аргументов a, b, c, d передаются координаты верхнего правого и нижнего левого
углов (произвольные числа). В каждом объекте координаты должны сохраняться в локальных
свойствах sp (верхний правый угол) и ep (нижний левый) в виде кортежей (a, b) и (c, d) соответственно.

Сформируйте 217 объектов этих классов: для каждого текущего объекта класс
выбирается случайно (или Line, или Rect, или Ellipse). Координаты также генерируются
случайным образом (числовые значения). Все объекты сохраните в списке elements.

В списке elements обнулите координаты объектов только для класса Line.
"""
from random import sample, choice


class Line:

    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:

    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:

    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


if __name__ == '__main__':
    elements = [choice([Line(0, 0, 0, 0),
                        Rect(*sample(range(22), 4)),
                        Ellipse(*sample(range(6), 4))]) for _ in range(217)]
