"""
Вам нужно реализовать в программе игровое поле для игры "Крестики-нолики".
Для этого требуется объявить класс TicTacToe (крестики-нолики), объекты которого создаются командой:

game = TicTacToe()

Каждый объект game должен иметь публичный атрибут:

pole - игровое поле: кортеж размером 3х3 с объектами класса Cell.

Каждая клетка игрового поля представляется объектом класса Cell и создается командой:

cell = Cell()

Объекты класса Cell должны иметь следующие публичные локальные атрибуты:

is_free - True, если клетка свободна; False в противном случае;
value - значение поля: 1 - крестик; 2 - нолик (по умолчанию 0).

Также с каждым объектом класса Cell должна работать функция:

bool(cell)

которая возвращает True, если клетка свободна (cell.is_free=True) и False в противном случае.

Класс TicTacToe должен иметь следующий метод:

clear() - очистка игрового поля (все клетки заполняются нулями и переводятся в закрытое состояние);

А объекты этого класса должны иметь следующую функциональность (обращение по индексам):

game[0, 0] = 1 # установка нового значения, если поле закрыто
res = game[1, 1] # получение значения центральной ячейки поля (возвращается число)

Если указываются некорректные индексы, то должно генерироваться исключение командой:

raise IndexError('неверный индекс клетки')

Если идет попытка присвоить новое значение в открытую клетку поля, то генерировать исключение:

raise ValueError('клетка уже занята')

Также должны быть реализованы следующие срезы при обращении к клеткам игрового поля:

slice_1 = game[:, indx] # выбираются все элементы (кортеж) столбца с индексом indx
slice_2 = game[indx, :] # выбираются все элементы (кортеж) строки с индексом indx
"""


class Cell:
    """Класс описывающий клетку игрового поля в крестики-нолики"""

    # 1 крестик; 2 нолик; 0 пустое место
    # is_free == True (клетка свободна, можно размещать);
    # is_free == False (клетка закрыта, размещать нельзя)
    def __init__(self):
        self.is_free = True
        self.value = 0

    # ниже объект свойство контролирует чтобы значение ячейки игрового поля менялось
    # только в том случае - если эта ячейка свободна, иначе вызываем исключение

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, v: int):
        if not self.is_free:
            raise ValueError("клетка уже занята")
        self.__value = v

    def __bool__(self):
        return self.is_free


class TicTacToe:
    """Класс описывающий игровое поле"""

    def __init__(self):
        # игровое поле представленное в виде двумерного кортежа
        self.pole = tuple(
            tuple(Cell() for col in range(3)) for row in range(3)
        )

    def clear(self):
        """Очищает игровое поле (убирает все крестики и нолики, закрывает клетки)"""

        # Циклом проходимся по каждой клетке
        for row in range(3):
            for col in range(3):
                self.pole[row][col].is_free = True
                self.pole[row][col].value = 0

    @staticmethod
    def __validate_coordinate(coordinate: int):
        """Проверяет чтобы координата не выходила за пределы размеров поля"""
        if coordinate not in range(3):
            raise IndexError("неверный индекс")

    def __getitem__(self, item: tuple):
        """Получение значения по координатам x, y (одна из координат может быть
        представлена срезом (slice). В этом случае выбираются все значения, находящиеся
        на той координате, которая представлена целым числом). Если обе координаты
        представлены целыми числами - просто возвращаем элемент поля находящийся на
        соответствующей координате"""

        row, col = item

        # Возвращается конкретная клетка
        if isinstance(row, int) and isinstance(col, int):
            self.__validate_coordinate(row)  # Проверяем координату (см. выше)
            self.__validate_coordinate(col)  # Проверяем координату (см. выше)
            return self.pole[row][col].value

        # Возвращаются все клетки, находящиеся под столбцом col
        elif isinstance(row, slice) and isinstance(col, int):
            self.__validate_coordinate(col)  # Проверяем координату (см. выше)
            return tuple(self.pole[r][col].value for r in range(3))

        # Возвращаются все клетки, находящиеся под строкой row
        elif isinstance(row, int) and isinstance(col, slice):
            self.__validate_coordinate(row)  # Проверяем координату (см. выше)
            return tuple(self.pole[row][c].value for c in range(3))

    def __setitem__(self, key, value):
        """Устанавливает значение конкретной клетке игрового поля"""

        row, col = key
        self.__validate_coordinate(row)  # Проверяем координату (см. выше)
        self.__validate_coordinate(col)  # Проверяем координату (см. выше)

        self.pole[row][col].value = value  # Срабатывает сеттер из класса Cell
        # (см. выше)
        self.pole[row][col].is_free = False


if __name__ == "__main__":
    g = TicTacToe()
    g.clear()
    assert g[0, 0] == 0 and g[2, 2] == 0, "начальные значения всех клеток должны быть равны 0"
    g[1, 1] = 1
    g[2, 1] = 2
    assert g[1, 1] == 1 and g[
        2, 1] == 2, "неверно отработала операция присваивания новых значений клеткам игрового поля (или, некорректно работает считывание значений)"

    try:
        res = g[3, 0]
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось исключение IndexError при считывании из несуществующей ячейки"

    try:
        g[3, 0] = 5
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось исключение IndexError при записи в несуществующую ячейку"

    g.clear()
    g[0, 0] = 1
    g[1, 0] = 2
    g[2, 0] = 3

    assert g[0, :] == (1, 0, 0) and g[1, :] == (2, 0, 0) and g[:, 0] == (
    1, 2, 3), "некорректно отработали срезы после вызова метода clear() и присваивания новых значений"

    cell = Cell()
    assert cell.value == 0, "начальное значение атрибута value класса Cell должно быть равно 0"
    res = cell.is_free
    cell.is_free = True
    assert bool(cell), "функция bool вернула False для свободной клетки"
