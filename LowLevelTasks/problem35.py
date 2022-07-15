"""
Объявите класс-декоратор InputDigits для декорирования стандартной функции input так, чтобы при вводе
строки из целых чисел, записанных через пробел, например:

"12 -5 10 83"

на выходе возвращался список из целых чисел:

[12, -5, 10, 83]

Назовите декорированную функцию input_dg и вызовите ее командой:

res = input_dg()
"""


class InputDigits:
    def __init__(self, f):
        self.__f = f

    def __call__(self, *args):
        return list(map(int, self.__f.split()))


if __name__ == '__main__':
    input_dg = InputDigits(input())
    res = input_dg()