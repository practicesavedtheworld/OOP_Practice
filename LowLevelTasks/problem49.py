"""
Вам поручается создать программу по учету книг (библиотеку). Для этого необходимо в программе объявить два класса:

Lib - для представления библиотеки в целом;
Book - для описания отдельной книги.

Объекты класса Book должны создаваться командой:

book = Book(title, author, year)

где title - заголовок книги (строка); author - автор книги (строка); year - год издания (целое число).

Объекты класса Lib создаются командой:

lib = Lib()

Каждый объект должен содержать локальный публичный атрибут:

book_list - ссылка на список из книг (объектов класса Book). Изначально список пустой.

При реализации бинарных операторов + и - создавать копии библиотек (объекты класса Lib) не нужно.

Также с объектами класса Lib должна работать функция:

n = len(lib) # n - число книг

которая возвращает число книг в библиотеке.
"""


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Lib:
    def __init__(self):
        self.book_list = list()

    def __len__(self):
        return len(self.book_list)

    def __add__(self, obj):
        if isinstance(obj, Book):
            self.book_list.append(obj)
        return self

    def __sub__(self, arg):
        if isinstance(arg, Book) and arg in self.book_list:
            self.book_list.remove(arg)
        elif isinstance(arg, int) and arg < len(self.book_list):
            del self.book_list[arg]
        return self

