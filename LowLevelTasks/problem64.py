"""
Из входного потока необходимо прочитать список строк командой:

lst_in = list(map(str.strip, sys.stdin.readlines()))

Каждая строка содержит информацию об учебном пособии в формате:

"Название; автор; год издания"
Необходимо каждую из этих строк представить объектом класса BookStudy, которые создаются командой:

bs = BookStudy(name, author, year)

где name - название пособия (строка); author - автор пособия (строка); year - год издания (целое число).
Такие же публичные локальные атрибуты должны быть в объектах класса BookStudy.

Для каждого объекта реализовать вычисление хэша по двум атрибутам: name и author (без учета регистра).

Сформировать список lst_bs из объектов класса BookStudy на основе прочитанных строк (списка lst_in).
После этого определить число книг с уникальными хэшами. Это число сохранить через переменную unique_books (целое число).
"""

import sys


class BookStudy:
    def __init__(self, name: str, author: str, year: int):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash(
            (self.name.lower(), self.author.lower())
        )

    @staticmethod
    def books_with_unique_num():
        c = 0
        for i in range(len(lst_in) - 1):
            for j in range(i + 1, len(lst_in)):
                if hash(lst_bs[i]) == hash(lst_bs[j]):
                    c += 1
        return len(lst_in) - c



lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_bs = [BookStudy(el.split('; ')[0], el.split('; ')[1], el.split('; ')[2]) for el in lst_in]
unique_books = lst_bs[0].books_with_unique_num()
