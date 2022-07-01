'''
Объявите в программе класс с именем Box (ящик), объекты которого должны создаваться командой:

box = Box()

А сам класс иметь следующие методы:

add_thing(self, obj) - добавление предмета obj (объект другого класса Thing) в ящик;
get_things(self) - получение списка объектов ящика.

Для описания предметов необходимо объявить еще один класс Thing. Объекты этого класса должны создаваться командой:

obj = Thing(name, mass)

где name - название предмета (строка); mass - масса предмета (число: целое или вещественное).
Объекты класса Thing должны поддерживать операторы сравнения:

obj1 == obj2
obj1 != obj2

Предметы считаются равными, если у них одинаковые названия name (без учета регистра) и массы mass.

Также объекты класса Box должны поддерживать аналогичные операторы сравнения:

box1 == box2
box1 != box2

Ящики считаются равными, если одинаковы их содержимое (для каждого объекта класса Thing
одного ящика и можно найти ровно один равный объект из второго ящика).
'''


class Box:
    def __init__(self, *args):
        self.__items = []
        if len(args):
            self.__items += list(args)

    def add_thing(self, obj):
        self.get_things().append(obj)

    def get_things(self):
        return self.__items

    def __eq__(self, other):
        return set([el.get_ch() for el in self.get_things()]) == set([el.get_ch() for el in other.get_things()])


class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.mass == other.mass

    def get_ch(self):
        return self.name, self.mass


if __name__ == '__main__':
    b1 = Box()
    b2 = Box()
    t1 = Thing('мел', 100)
    t2 = Thing('тряпка', 200)
    t3 = Thing('тряпка', 200)
    t4 = Thing('тряпка', 200)
    b1.add_thing(Thing('мел', 100))
    b1.add_thing(Thing('тряпка', 200))
    b1.add_thing(Thing('доска', 2000))
    b2.add_thing(Thing('тряпка', 200))
    b2.add_thing(Thing('мел', 100))
    b2.add_thing(Thing('доска', 2000))
    res = b1 == b2
