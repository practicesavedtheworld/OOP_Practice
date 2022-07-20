"""
Объявите класс с именем ShopItem (товар), объекты которого создаются командой:

item = ShopItem(name, weight, price)

где name - название товара (строка); weight - вес товара (число: целое или вещественное); price - цена товара (число: целое или вещественное).

Определите в этом классе магические методы:

__hash__() - чтобы товары с одинаковым названием (без учета регистра), весом и ценой имели бы равные хэши;
__eq__() - чтобы объекты с одинаковыми хэшами были равны.

Затем, из входного потока прочитайте строки :

Строки имеют следующий формат:

название товара 1: вес_1 цена_1
...
название товара N: вес_N цена_N

Например:

Системный блок: 1500 75890.56
Монитор Samsung: 2000 34000
Клавиатура: 200.44 545
Монитор Samsung: 2000 34000

Как видите, товары в этом списке могут совпадать.

Необходимо для всех этих строчек сформировать соответствующие объекты класса ShopItem и добавить в словарь с именем shop_items.
Ключами словаря должны выступать сами объекты, а значениями - список в формате:

[item, total]

где item - объект класса ShopItem; total - общее количество одинаковых объектов (с одинаковыми хэшами).
Подумайте, как эффективно программно наполнять такой словарь, проходя по списку lst_in один раз.

"""

import sys


class ShopItem:
    def __init__(self, name: str, weight: (int, float), price: (int, float)):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash(
            (self.name.lower(), self.weight, self.price)
        )

    def __eq__(self, other):
        return hash(self) == hash(other)

    def xx(self):
        return len(lst_in) - sum(1 for i in range(len(lst_in)) if s[i] != self)


lst_in = list(map(str.strip, sys.stdin.readlines()))  # список lst_in в программе не менять!
s = [ShopItem(el.split(': ')[0], el.split(': ')[1].split()[0], el.split(': ')[1].split()[1]) for el in lst_in]
shop_items = {i: [i, i.xx()] for i in s}

if __name__ == '__main__':

    it1 = ShopItem('name', 10, 11)
    it2 = ShopItem('name', 10, 11)
    assert hash(it1) == hash(it2), "разные хеши у равных объектов"

    it2 = ShopItem('name', 10, 12)
    assert hash(it1) != hash(it2), "равные хеши у разных объектов"

    it2 = ShopItem('name', 11, 11)
    assert hash(it1) != hash(it2), "равные хеши у разных объектов"

    it2 = ShopItem('NAME', 10, 11)
    assert hash(it1) == hash(it2), "разные хеши у равных объектов"

    name = lst_in[0].split(':')
    for sp in shop_items.values():
        assert isinstance(sp[0], ShopItem) and type(sp[
                                                        1]) == int, "в значениях словаря shop_items первый элемент должен быть объектом класса ShopItem, а второй - целым числом"

    v = list(shop_items.values())
    if v[0][0].name.strip() == "Системный блок":
        assert v[0][1] == 1 and v[1][1] == 2 and v[2][1] == 1 and len(v) == 3, "неверные значения в словаре shop_items"

    if v[0][0].name.strip() == "X-box":
        assert v[0][1] == 2 and v[1][1] == 1 and v[2][1] == 2 and len(v) == 3, "неверные значения в словаре shop_items"
