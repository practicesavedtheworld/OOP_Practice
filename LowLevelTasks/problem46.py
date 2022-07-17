"""
Известно, что в Python мы можем соединять два списка между собой с помощью оператора +:

lst = [1, 2, 3] + [4.5, -3.6, 0.78]

Но нет реализации оператора -, который бы убирал из списка все значения вычитаемого списка:

lst = [1, 2, 3, 4, 5, 6] - [5, 6, 7, 8, 1] # [2, 3, 4] (порядок следования оставшихся элементов списка должен сохраняться)

Давайте это поправим и создадим такой функционал. Для этого нужно объявить класс с именем NewList, объекты которого создаются командами:

lst = NewList() # пустой список
lst = NewList([-1, 0, 7.56, True]) # список с начальными значениями
Также в классе NewList необходимо объявить метод:

get_list() - для возвращения результирующего списка объекта класса NewList
"""


class NewList:
    def __init__(self, lis=None):
        self.n_l = lis[:] if lis and type(lis) == list else []

    def get_list(self):
        return self.n_l

    def __sub__(self, other):
        other_list = other if type(other) == list else other.get_list()
        return NewList(self.__diff(self.n_l, other_list))

    def __rsub__(self, other):
        return NewList(self.__diff(other, self.n_l))

    @staticmethod
    def __diff(l1, l2):
        if len(l2) == 0:
            return l1
        s = l2[:]
        return [i for i in l1 if not NewList.__iselem(i, s)]

    @staticmethod
    def __iselem(x, sub):
        res = any(map(lambda xx: type(x) == type(xx) and x == xx, sub))
        if res:
            sub.remove(x)
        return  res

if __name__ == '__main__':
    lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
    lst2 = NewList([0, 1, 2, 3, True])
    res_1 = lst1 - lst2  # NewList: [-4, 6, 10, 11, 15, False]
    lst1 -= lst2  # NewList: [-4, 6, 10, 11, 15, False]
    res_2 = lst2 - [0, True]  # NewList: [1, 2, 3]
    res_3 = [1, 2, 3, 4.5] - res_2  # NewList: [4.5]
    a = NewList([2, 3])
    res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]
