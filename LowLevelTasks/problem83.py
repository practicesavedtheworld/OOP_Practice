"""
Теперь, вам необходимо разработать итератор, который бы перебирал указанные столбцы двумерного списка.
Список представляет собой двумерную таблицу из данных:

lst = [[x11, x12, ..., x1N],
       [x21, x22, ..., x2N],
       ...
       [xM1, xM2, ..., xMN]
      ]

Для этого в программе необходимо объявить класс с именем IterColumn, объекты которого создаются командой:

it = IterColumn(lst, column)

где lst - ссылка на двумерный список; column - индекс перебираемого столбца (отсчитывается от 0).

Затем, с объектами класса IterColumn должны быть доступны следующие операции:

it = IterColumn(lst, 1)
for x in it:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
    print(x)

it_iter = iter(it)
x = next(it_iter)

"""


class IterColumn:
    def __init__(self, lst, column):
        self.__lst = lst
        self.__col = column

    def __iter__(self):
        self.__row = -1
        return self

    def __next__(self):
        self.__row += 1
        if self.__row == len(self.__lst):
            raise StopIteration

        return self.__lst[self.__row][self.__col]


