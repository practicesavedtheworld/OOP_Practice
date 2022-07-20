"""
Объявите класс Record (запись), который описывает одну произвольную запись из БД.
Объекты этого класса создаются командой:

r = Record(field_name1=value1,... , field_nameN=valueN)

где field_nameX - наименование поля БД; valueX - значение поля из БД.

В каждом объекте класса Record должны автоматически создаваться локальные публичные атрибуты по
именам полей (field_name1,... , field_nameN) с соответствующими значениями. Например:

r = Record(pk=1, title='Python ООП', author='Балакирев')

В объекте r появляются атрибуты:

r.pk # 1
r.title # Python ООП
r.author # Балакирев

Также необходимо обеспечить доступ к этим полям через индексы

Если указывается неверный индекс (не целое число или некорректное целое число), то должно генерироваться исключение командой:

raise IndexError('неверный индекс поля')
"""


class Record:
    def __init__(self, **kwargs):
        for i in kwargs:
            setattr(self, i, kwargs.get(i))

    def __getitem__(self, item):
        if self.check(item):
            return tuple(self.__dict__.values())[item]

    def __setitem__(self, item, val):
        if self.check(item):
            setattr(self, tuple(self.__dict__)[item], val)

    def check(self, digit):
        if not isinstance(digit, int) or digit < 0 or digit >= len(self.__dict__):
            raise IndexError('неверный индекс поля')
        return True


