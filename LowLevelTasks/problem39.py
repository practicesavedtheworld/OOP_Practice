"""
Объявите класс WordString, объекты которого создаются командами:

w1 = WordString()
w2 = WordString(string)

где string - передаваемая строка. Например:

words = WordString("Курс по Python ООП")

Реализовать следующий функционал для объектов этого класса:

len(words) - должно возвращаться число слов в переданной строке (слова разделяются одним или несколькими пробелами);
words(indx) - должно возвращаться слово по его индексу (indx - порядковый номер слова в строке, начиная с 0).

Также в классе WordString реализовать объект-свойство (property):

string - для передачи и считывания строки.
"""


class WordString:
    def __init__(self, string=''):
        self.__s = string

    def __call__(self, *args, **kwargs):
        return self.words(*args)

    def __len__(self, *args):
        return len(self.__s.split())

    def words(self, indx):
        return self.__s.split()[indx]

    @property
    def string(self):

        return self.__s

    @string.setter
    def string(self, val):
        self.__s = val


if __name__ == '__main__':
    words = WordString()
    words.string = "ООП Да"
    n = len(words)
    first = "" if n == 0 else words(0)
    print(words.string)
    print(f"Число слов: {n}; первое слово: {first}")