"""
Объявите класс Circle (окружность), объекты которого должны создаваться командой:

circle = Circle(x, y, radius)   # x, y - координаты центра окружности; radius - радиус окружности

В каждом объекте класса Circle должны формироваться локальные приватные атрибуты:

__x, __y - координаты центра окружности (вещественные или целые числа);
__radius - радиус окружности (вещественное или целое положительное число).

Для доступа к этим приватным атрибутам в классе Circle следует объявить объекты-свойства (property):

x, y - для изменения и доступа к значениям __x, __y, соответственно;
radius - для изменения и доступа к значению __radius.

При изменении значений приватных атрибутов через объекты-свойства нужно дополнительно проверять,
что присваиваемые значения - числа (целые или вещественные). Дополнительно у радиуса проверять,
что число должно быть положительным (строго больше нуля). Сделать это нужно через магические методы.
При некорректных переданных значениях, прежние значения меняться не должны.

Если присваиваемое значение не числовое, то генерировать исключение командой:

raise TypeError("Неверный тип присваиваемых данных.")

При обращении к несуществующему атрибуту объектов класса Circle выдавать булево значение False.
"""


#class Descr:
#    def __set_name__(self, owner, name):
#        self.name = f"_{name}"
#
#    def __get__(self, instance, name):
#        return getattr(instance, self.name)
#
#    def __set__(self, instance, value):
#        setattr(instance, self.name, value)


class Circle:
    def __init__(self, x, y, radius):
        if not self.check(x):
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            self.__x = x
        if not self.check(y):
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            self.__y = y
        if not self.check(radius):
            raise TypeError("Неверный тип присваиваемых данных.")
        elif self.check(radius) and radius > 0:
            self.__radius = radius
        elif radius <= 0:
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            pass

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if not self.check(val):
            raise TypeError("Неверный тип присваиваемых данных.")
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        if not self.check(val):
            raise TypeError("Неверный тип присваиваемых данных.")
        self.__y = val

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, val):
        if not self.check(val):
            raise TypeError("Неверный тип присваиваемых данных.")
        if self.check(val):
            if val > 0:
                self.__radius = val
            else:
                pass

    @staticmethod
    def check(value):
        return isinstance(value, (int, float))

    def __getattr__(self, name):
        return False


if __name__ == '__main__':
    circle = Circle(10.5, 7, 22)
    circle.radius = -10  # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
    x, y = circle.x, circle.y
    res = circle.name  # False, т.к. атрибут name не существует
