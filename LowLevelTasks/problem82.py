"""
<<<<<<< HEAD
Объявите в программе класс Person, объекты которого создаются командой:

p = Person(fio, job, old, salary, year_job)

где fio - ФИО сотрудника (строка); job - наименование должности (строка); old - возраст (целое число); salary - зарплата (число: целое или вещественное); year_job - непрерывный стаж на указанном месте работы (целое число).

В каждом объекте класса Person автоматически должны создаваться локальные атрибуты с такими же именами: fio, job, old, salary, year_job и соответствующими значениями.

Также с объектами класса Person должны поддерживаться следующие команды:

data = p[indx] # получение данных по порядковому номеру (indx) атрибута (порядок: fio, job, old, salary, year_job и начинается с нуля)
p[indx] = value # запись в поле с указанным индексом (indx) нового значения value
for v in p: # перебор всех атрибутов объекта в порядке: fio, job, old, salary, year_job
    print(v)

При работе с индексами, проверить корректность значения indx. Оно должно быть целым числом в диапазоне [0; 4].
Иначе, генерировать исключение командой:

raise IndexError('неверный индекс')
"""


class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.n = ['fio', 'job', 'old', 'salary', 'year_job']
        self.c = 0

    def __getitem__(self, item):
        if isinstance(item, int) and 4 >= item >= 0:
            return getattr(self, self.n[item])
        else:
            raise IndexError('неверный индекс')

    def __setitem__(self, key, val):
        if isinstance(key, int) and 4 >= key >= 0:
            setattr(self, self.n[key], val)
        else:
            raise IndexError('неверный индекс')

    def __iter__(self):
        return self

    def __next__(self):
        if 4 >= self.c >= 0:
            vvv = self.__getitem__(self.c)
            self.c += 1
            return vvv
        else:
            raise StopIteration


if __name__ == '__main__':
    pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
    pers[0] = 'Минин Г. Г.'
    for v in pers:
        print(v)
    pers[5] = 123  # IndexError

