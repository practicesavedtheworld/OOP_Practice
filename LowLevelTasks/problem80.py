"""
Объявите в программе класс Bag (сумка), объекты которого создаются командой:

bag = Bag(max_weight)

где max_weight - максимальный суммарный вес предметов, который можно положить в сумку.

Каждый предмет описывается классом Thing и создается командой:

t = Thing(name, weight)

где name - название предмета (строка); weight - вес предмета (вещественное или целочисленное значение).
В объектах класса Thing должны автоматически формироваться локальные свойства с теми же именами: name и weight.

В классе Bag должен быть реализован метод:

add_thing(thing) - добавление нового объекта thing класса Thing в сумку.

Добавление выполняется только если суммарный вес вещей не превышает параметра max_weight. Иначе, генерируется исключение:

raise ValueError('превышен суммарный вес предметов')

Также с объектами класса Bag должны выполняться следующие команды:

t = bag[indx] # получение объекта класса Thing по индексу indx (в порядке добавления вещей, начиная с 0)
bag[indx] = t # замена прежней вещи на новую t, расположенной по индексу indx
del bag[indx] # удаление вещи из сумки, расположенной по индексу indx

Если индекс в этих командах указывается неверно, то должно генерироваться исключение:

raise IndexError('неверный индекс')
"""


class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.bag = []

    def get_w(self, item):
        if not sum([i.weight for i in self.bag]) + item.weight <= self.max_weight:
            raise ValueError('превышен суммарный вес предметов')

    def add_thing(self, thing):
        self.get_w(thing)
        self.bag.append(thing)

    def check_index(self, idx):
        if not isinstance(idx, int) and 0 <= idx < len(self.bag):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.check_index(item)
        return self.bag[item]

    def __setitem__(self, key, value):
        self.check_index(key)
        if sum([i.weight for i in self.bag]) -self.bag[key].weight + value.weight <= self.max_weight:
            self.bag[key] = value
        else:
            raise ValueError('превышен суммарный вес предметов')

    def __delitem__(self, index):
        self.check_index(index)
        del self.bag[index]


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


if __name__ == '__main__':
    bag = Bag(1000)
    bag.add_thing(Thing('книга', 100))
    bag.add_thing(Thing('носки', 200))
    bag.add_thing(Thing('рубашка', 500))
    bag.add_thing(Thing('ножницы', 300))  # генерируется исключение ValueError
    print(bag[2].name)  # рубашка
    bag[1] = Thing('платок', 100)
    print(bag[1].name)  # платок
    del bag[0]
    print(bag[0].name)  # платок
    t = bag[4]  # генерируется исключение IndexError