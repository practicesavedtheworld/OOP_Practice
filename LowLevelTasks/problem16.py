class Dimensions:
    __MIN_DIMENSION = 10
    __MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    '''Get result of a*b*c'''
    def __len__(self):
        return self.a *self.b*self.c

    def __ge__(self, other):
        return self.__len__() >= other.__len__()

    def __le__(self, other):
        return self.__len__() <= other.__len__()

    def __lt__(self, other):
        return self.__len__() < other.__len__()

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, val):
        if val in range(self.__MIN_DIMENSION, self.__MAX_DIMENSION + 1):
            setattr(self, self.__c, val)

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, val):
        if val in range(self.__MIN_DIMENSION, self.__MAX_DIMENSION + 1):
            setattr(self, self.__a, val)

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, val):
        if val in range(self.__MIN_DIMENSION, self.__MAX_DIMENSION + 1):
            setattr(self, self.__b, val)


class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim


if __name__ == '__main__':
    item1 = ShopItem('кеды', 1024, Dimensions(40, 30, 120))
    item2 = ShopItem('зонт', 500.24, Dimensions(10, 20, 50))
    item3 = ShopItem('холодильник', 40000, Dimensions(2000, 600, 500))
    item4 = ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
    lst_shop = [item1, item2, item3, item4]
    lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim.__len__()) == sorted(lst_shop, key=lambda x: x.dim)