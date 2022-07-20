"""
Вы начинаете разрабатывать игру "Сапер". Для этого вам нужно уметь представлять и управлять игровым полем.
Будем полагать, что оно имеет размеры N x M клеток. Каждая клетка будет представлена объектом класса Cell и
содержать либо число мин вокруг этой клетки, либо саму мину.

Для начала в программе объявите класс GamePole, который будет создавать и управлять игровым полем.
Объект этого класса должен формироваться командой:

pole = GamePole(N, M, total_mines)

И, так как поле в игре одно, то нужно контролировать создание только одного объекта класса GamePole.

Объект pole должен иметь локальный приватный атрибут:

__pole_cells - двумерный (вложенный) кортеж, размерами N x M элементов (N строк и M столбцов), состоящий из объектов класса Cell.

Для доступа к этой коллекции объявите в классе GamePole объект-свойство (property):

pole - только для чтения (получения) ссылки на коллекцию __pole_cells.

Далее, в самом классе GamePole объявите следующие методы:

init_pole() - для инициализации начального состояния игрового поля (расставляет мины и делает все клетки закрытыми);
open_cell(i, j) - открывает ячейку с индексами (i, j); нумерация индексов начинается с нуля; метод меняет значение
атрибута __is_open объекта Cell в ячейке (i, j) на True;
show_pole() - отображает игровое поле в консоли (как именно сделать - на ваше усмотрение, этот метод - домашнее задание).

Расстановку мин выполняйте случайным образом по игровому полю (для этого удобно воспользоваться функцией randint модуля random).
После расстановки всех total_mines мин, вычислите их количество вокруг остальных клеток (где нет мин). Область охвата - соседние (прилегающие) клетки (8 штук).

В методе open_cell() необходимо проверять корректность индексов (i, j).
Если индексы указаны некорректно, то генерируется исключение командой:

raise IndexError('некорректные индексы i, j клетки игрового поля')

Следующий класс Cell описывает состояние одной ячейки игрового поля. Объекты этого класса создаются командой:

cell = Cell()

При этом в самом объекте создаются следующие локальные приватные свойства:

__is_mine - булево значение True/False; True - в клетке находится мина, False - мина отсутствует;
__number - число мин вокруг клетки (целое число от 0 до 8);
__is_open - флаг того, открыта клетка или закрыта: True - открыта; False - закрыта.

Для работы с этими приватными атрибутами объявите в классе Cell следующие объекты-свойства с именами:

is_mine - для записи и чтения информации из атрибута __is_mine;
number - для записи и чтения информации из атрибута __number;
is_open - для записи и чтения информации из атрибута __is_open.

В этих свойствах необходимо выполнять проверку на корректность переданных значений
(либо булево значение True/False, либо целое число от 0 до 8).
Если передаваемое значение некорректно, то генерировать исключение командой:

raise ValueError("недопустимое значение атрибута")

С объектами класса Cell должна работать функция:

bool(cell)

которая возвращает True, если клетка закрыта и False - если открыта.
"""


import random


class GamePole:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if GamePole.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, N, M, total_mines):
        self.n = N
        self.m = M
        if self.n * self.m <= total_mines:
            raise AttributeError("Очень много мин!!! N * M <= total_mines")
        self.total_mines = total_mines
        self.__pole_cells = [[Cell() for j in range(self.m)] for i in range(self.n)]

    @property
    def pole(self):
        return self.__pole_cells

    @staticmethod
    def __random_cord(n, m):
        return random.randint(0, n - 1), random.randint(0, m - 1)

    def init_pole(self):
        for _ in range(self.total_mines):
            i, j = self.__random_cord(self.n, self.m)
            while self.pole[i][j].is_mine:
                i, j = self.__random_cord(self.n, self.m)
            self.pole[i][j].is_mine = True
        self.count_mines()

    def count_mines(self):
        for i in range(self.n):
            for j in range(self.m):
                if not self.pole[i][j].is_mine:
                    self.pole[i][j].number = self.__count_mines_for_ceil(i, j)

    def __count_mines_for_ceil(self, i, j):
        n = 0
        for line in range(-1, 2):
            for row in range(-1, 2):
                x = i + line
                y = j + row
                if x < 0 or y < 0 or x >= self.n or y >= self.m:
                    continue
                if self.pole[x][y].is_mine:
                    n += 1
        return n

    def open_cell(self, i, j):
        if isinstance(i, int) and isinstance(j, int) and 0 <= i < self.n and 0 <= j < self.m:
            self.__pole_cells[i][j].is_open = True
        else:
            raise IndexError('некорректные индексы i, j клетки игрового поля')

    def show_pole(self):
        for i in range(self.n):
            for j in range(self.m):
                if not self.__pole_cells[i][j]:
                    print(" # ", end="")
                else:
                    if self.__pole_cells[i][j].is_mine:
                        print(" * ", end="")
                    else:
                        print(f" {self.__pole_cells[i][j].number} ", end="")
            print()


class Cell:
    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value):
        if not type(value) == bool:
            raise ValueError("недопустимое значение атрибута")
        self.__is_mine = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if not (isinstance(value, (int)) and 0 <= value <= 8):
            raise ValueError("недопустимое значение атрибута")
        self.__number = value

    @property
    def is_open(self):
        return self.__is_open

    @is_mine.setter
    def is_open(self, value):
        if not type(value) == bool:
            raise ValueError("недопустимое значение атрибута")
        self.__is_open = value

    def __bool__(self):
        return not self.__is_open


if __name__ == "__main__":
    p1 = GamePole(10, 20, 10)
    p2 = GamePole(10, 20, 10)
    assert id(p1) == id(p2), "создается несколько объектов класса GamePole"
    p = p1

    cell = Cell()
    assert type(Cell.is_mine) == property and type(Cell.number) == property and type(
        Cell.is_open) == property, "в классе Cell должны быть объекты-свойства is_mine, number, is_open"

    cell.is_mine = True
    cell.number = 5
    cell.is_open = True
    assert bool(cell) == False, "функция bool() вернула неверное значение"

    try:
        cell.is_mine = 10
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError"

    try:
        cell.number = 10
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError"

    p.init_pole()
    m = 0
    for row in p.pole:
        for x in row:
            assert isinstance(x, Cell), "клетками игрового поля должны быть объекты класса Cell"
            if x.is_mine:
                m += 1

    assert m == 10, "на поле расставлено неверное количество мин"
    p.open_cell(0, 1)
    p.open_cell(9, 19)

    try:
        p.open_cell(10, 20)
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось исключение IndexError"


    def count_mines(pole, i, j):
        n = 0
        for k in range(-1, 2):
            for l in range(-1, 2):
                ii, jj = k + i, l + j
                if ii < 0 or ii > 9 or jj < 0 or jj > 19:
                    continue
                if pole[ii][jj].is_mine:
                    n += 1

        return n


    for i, row in enumerate(p.pole):
        for j, x in enumerate(row):
            if not p.pole[i][j].is_mine:
                m = count_mines(p.pole, i, j)
                assert m == p.pole[i][j].number, "неверно подсчитано число мин вокруг клетки"
