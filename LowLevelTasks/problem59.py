"""
body = Body(name, ro, volume)

где name - название тела (строка); ro - плотность тела (число: вещественное или целочисленное);
            volume - объем тела  (число: вещественное или целочисленное).

Для объектов класса Body должны быть реализованы операторы сравнения:

body1 > body2  # True, если масса тела body1 больше массы тела body2
body1 == body2 # True, если масса тела body1 равна массе тела body2
body1 < 10     # True, если масса тела body1 меньше 10
body2 == 5     # True, если масса тела body2 равна 5

Масса тела вычисляется по формуле:

m = ro * volume
"""


class Body:
    def __init__(self, name: str, ro: int, volume: int | float):
        self.name = name
        self.ro = ro
        self.volume = volume

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return len(self) > other
        return len(self) > len(other)

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return len(self) < other
        return len(self) < len(other)

    def __len__(self):
        return self.ro * self.volume

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return len(self) == other
        return len(self) == len(other)


if __name__ == '__main__':

    body = Body('s', 123, 33)
    print(body > 15)
    print(15 < body)
    print(body < 15)
    print(15 > body)