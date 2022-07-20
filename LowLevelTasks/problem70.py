"""
Объявите класс Ellipse (эллипс), объекты которого создаются командами:

el1 = Ellipse()  # без создания локальных атрибутов x1, y1, x2, y2
el2 = Ellipse(x1, y1, x2, y2)

где x1, y1 - координаты (числа) левого верхнего угла; x2, y2 - координаты (числа) нижнего правого угла.
Первая команда создает объект класса Ellipse без локальных атрибутов x1, y1, x2, y2.
Вторая команда создает объект с локальными атрибутами x1, y1, x2, y2 и соответствующими переданными значениями.

В классе Ellipse объявите магический метод __bool__(), который бы возвращал True,
если все локальные атрибуты x1, y1, x2, y2 существуют и False - в противном случае.

Также в классе Ellipse нужно реализовать метод:

get_coords() - для получения кортежа текущих координат объекта.

Если координаты отсутствуют (нет локальных атрибутов x1, y1, x2, y2), то метод get_coords() должен генерировать исключение командой:

raise AttributeError('нет координат для извлечения')

Сформируйте в программе список с именем lst_geom, содержащий четыре объекта класса Ellipse. Два объекта должны быть созданы командой

Ellipse()

и еще два - командой:

Ellipse(x1, y1, x2, y2)

Переберите список в цикле и вызовите метод get_coords() только для объектов, имеющих координаты x1, y1, x2, y2.
"""


class Ellipse:
    def __init__(self, *args):
        if args:
            self.x1, self.y1, self.x2, self.y2 = args


    def get_coords(self):
        if bool(self):
            return self.x1, self.y1, self.x2, self.y2
        else:
            raise AttributeError('нет координат для извлечения')

    def __bool__(self):
        try:
            return all((self.x1, self.y1, self.x2, self.y2))
        except:
            pass
        return False


if __name__ == '__main__':
    lst_geom = [Ellipse() if i in (0, 1) else Ellipse(1, 2, 3, i) for i in range(4)]
    for elm in lst_geom:
        if elm:
            elm.get_coords()