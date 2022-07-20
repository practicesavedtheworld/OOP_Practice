"""
Вам необходимо написать программу для удобного обращения с таблицами однотипных данных (чисел, строк,
булевых значений и т.п.), то есть, все ячейки таблицы должны представлять какой-то один указанный тип.

Для этого в программе необходимо объявить три класса:

TableValues - для работы с таблицей в целом;
CellInteger - для операций с целыми числами;
IntegerValue - дескриптор данных для работы с целыми числами.

Начнем с дескриптора IntegerValue. Это должен быть дескриптор данных (то есть, и для записи и считывания значений).
Если присваиваемое значение не является целым числом, должно генерироваться исключение командой:

raise ValueError('возможны только целочисленные значения')

Следующий класс CellInteger описывает одну ячейку таблицы для работы с целыми числами.
В этом классе должен быть публичный атрибут (атрибут класса):

value - объект дескриптора, класса IntegerValue.

А объекты класса CellInteger должны создаваться командой:

cell = CellInteger(start_value)

где start_value - начальное значение ячейки (по умолчанию равно 0 и сохраняется в ячейке через дескриптор value).

Наконец, объекты последнего класса TableValues создаются командой:

table = TableValues(rows, cols, cell=CellInteger)

где rows, cols - число строк и столбцов (целые числа); cell - ссылка на класс, описывающий работу с отдельными ячейками таблицы.
Если параметр cell не указан, то генерировать исключение командой:

raise ValueError('параметр cell не указан')

Иначе, в объекте table класса TableValues создается двумерный (вложенный) кортеж с именем cells размером rows x cols,
состоящий из объектов указанного класса (в данном примере - класса CellInteger).

Также в классе TableValues предусмотреть возможность обращения к отдельной ячейке по ее индексам, например:

value = table[1, 2] # возвращает значение ячейки с индексом (1, 2)
table[0, 0] = value # записывает новое значение в ячейку (0, 0)

Обратите внимание, по индексам сразу должно возвращаться значение ячейки, а не объект класса CellInteger.
И то же самое с присваиванием нового значения.
"""


class IntegerValue:
    @staticmethod
    def check(d):
        if not isinstance(d, int):
            raise ValueError('возможны только целочисленные значения')

    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.check(value)
        setattr(instance, self.name, value)


class TableValues:
    def __init__(self, *args, **kwargs):
        if not len(kwargs):
            raise ValueError('параметр cell не указан')
        self.rows = args[0]
        self.cols = args[1]
        self.cell = kwargs.get(*kwargs)
        self.cells = tuple([
            tuple([self.cell() for i in range(self.cols)]) for j in range(self.rows)
        ])

    @staticmethod
    def __check(index):
        for el in index:
            if type(el) != int:
                raise IndexError('неверный индекс для доступа к элементам массива')

    def __getitem__(self, item):
        self.__check(item)
        return self.cells[item[0]][item[1]].value

    def __setitem__(self, key, val):
        self.__check(key)
        self.cells[key[0]][key[1]].value = val


class CellInteger:
    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value


if __name__ == "__main__":
    tb = TableValues(3, 2, cell=CellInteger)
    tb[0, 0] = 1
    assert tb[0, 0] == 1, "некорректно работает запись и/или считывание значения в ячейку таблицы по индексам"

    try:
        tb[2, 1] = 1.5
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError"

    for row in tb.cells:
        for x in row:
            assert isinstance(x, CellInteger), "коллекция cells должна содержать только объекты класса  CellInteger"

    cell = CellInteger(10)
    assert cell.value == 10, "дескриптор value вернул неверное значение"
