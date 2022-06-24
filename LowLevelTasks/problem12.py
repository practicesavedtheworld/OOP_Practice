'''
Объявите класс DigitRetrieve для преобразования данных из строки в числа.
Целые числа в строке следует приводить к целочисленному типу данных, а все остальные - к значению None.
'''

import re


class DigitRetrieve:
    def __call__(self, string):
        return int(string) if re.fullmatch('-?\d+', string) is not None else None


if __name__ == '__main__':
    dg = DigitRetrieve()
    st = ["123", "abc", "-56.4", "0", "-5"]
    digitss = list(map(dg, st))  # [123, None, None, 0, -5]

