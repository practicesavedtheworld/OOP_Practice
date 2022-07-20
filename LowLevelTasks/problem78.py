"""
Объявите в программе класс с именем RadiusVector (радиус-вектор), объекты которого создаются командой:

v = RadiusVector(x1, x2,..., xN)

где x1, x2,..., xN - координаты радиус-вектора (числа: целые или вещественные).

В каждом объекте класса RadiusVector должен быть локальный атрибут:

coords - список из координат радиус-вектора.

Для доступа к отдельным координатам, реализовать следующий функционал:

coord = v[i] # получение значения i-й координаты (целое число, отсчет с нуля)
coords_1 = v[start:stop] # получение среза (набора) координат в виде кортежа
coords_2 = v[start:stop:step] # получение среза (набора) координат в виде кортежа
v[i] = value # изменение i-й координаты
v[start:stop] = [val_1, val_2, ...] # изменение сразу нескольких координат
v[start:stop:step] = [val_1, val_2, ...] # изменение сразу нескольких координат
"""


class RadiusVector:
    def __init__(self, *args):
        self.coords = list(args)

    def __setitem__(self, key, value):
        self.coords[key] = value

    def __getitem__(self, item):
        return tuple(self.coords[item]) if isinstance(item, slice) else self.coords[item]


if __name__ == '__main__':
    v = RadiusVector(1, 1, 1, 1)
    print(v[1])  # 1
    v[:] = 1, 2, 3, 4
    print(v[2])  # 3
    print(v[1:])  # (2, 3, 4)
    v[0] = 10.5