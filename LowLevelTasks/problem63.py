"""
Объявите класс с именем DataBase (база данных - БД), объекты которого создаются командой:

db = DataBase(path)

где path - путь к файлу с данными БД (строка).

Также в классе DataBase нужно объявить следующие методы:

write(self, record) - для добавления новой записи в БД, представленной объектом record;
read(self, pk) - чтение записи из БД (возвращает объект Record) по ее уникальному идентификатору pk (уникальное целое положительное число); запись ищется в значениях словаря (см. ниже)

Каждая запись БД должна описываться классом Record, а объекты этого класса создаваться командой:

record = Record(fio, descr, old)

где fio - ФИО некоторого человека (строка); descr - характеристика человека (строка); old - возраст человека (целое число).

В каждом объекте класса Record должны формироваться следующие локальные атрибуты:

pk - уникальный идентификатор записи (число: целое, положительное); формируется автоматически при создании каждого нового объекта;
fio - ФИО человека (строка);
descr - характеристика человека (строка);
old - возраст человека (целое число).

Реализовать для объектов класса Record вычисление хэша по атрибутам: fio и old (без учета регистра).
Если они одинаковы для разных записей, то и хэши должны получаться равными. Также для объектов класса Record  с
одинаковыми хэшами оператор == должен выдавать значение True, а с разными хэшами - False.

Хранить записи в БД следует в виде словаря dict_db (атрибут объекта db класса DataBase), ключами которого являются
объекты класса Record, а значениями список из объектов с равными хэшами:

dict_db[rec1] = [rec1, rec2, ..., recN]

где rec1, rec2, ..., recN - объекты класса Record с одинаковыми хэшами.

Для наполнения БД прочитайте строки из входного потока с помощью команды:

lst_in = list(map(str.strip, sys.stdin.readlines()))

где каждая строка представлена в формате:

"ФИО; характеристика; возраст"


Каждая строка должна быть представлена объектом класса Record и записана в БД db (в словарь db.dict_db).
"""


import sys


class Record:

    def __init__(self, fio: str, descr: str, old: int) -> None:
        self.fio = fio
        self.descr = descr
        self.old = old
        self.pk = hash((self.fio, self.descr, self.old, __import__('random').randint(1, 10000)))

    def __eq__(self, other) -> bool:
        return hash(self) == hash(other)

    def __hash__(self) -> int:
        return hash((self.fio.lower(), self.old))


class DataBase:

    def __init__(self, path: str) -> None:
        self.path = path
        self.dict_db: dict = dict()

    def write(self, record: Record) -> None:
        self.dict_db.setdefault(hash(record), []).append(record)

    def read(self, pk: int) -> Record:
        for i in sum(self.dict_db.values(), []):
            if i.pk == pk:
                return i


lst_in = list(map(str.strip, sys.stdin.readlines()))

if __name__ == '__main__':
    db = DataBase('path')
    for i in lst_in:
        db.write(Record(*i.split('; ')))
    db22345 = DataBase('123')
    r1 = Record('fio', 'descr', 10)
    r2 = Record('fio', 'descr', 10)
    assert r1.pk != r2.pk, "равные значения атрибута pk у разных объектов класса Record"

    db22345.write(r2)
    r22 = db22345.read(r2.pk)
    assert r22.pk == r2.pk and r22.fio == r2.fio and r22.descr == r2.descr and r22.old == r2.old, "при операциях write и read прочитанный объект имеет неверные значения атрибутов"

    assert len(db22345.dict_db) == 1, "неверное число объектов в словаре dict_db"

