"""
Объявите класс DeltaClock для вычисления разницы времен. Объекты этого класса должны создаваться командой:

dt = DeltaClock(clock1, clock2)

где clock1, clock2 - объекты другого класса Clock для хранения текущего времени. Эти объекты должны создаваться командой:

clock = Clock(hours, minutes, seconds)

где hours, minutes, seconds - часы, минуты, секунды (целые неотрицательные числа).

В классе Clock также должен быть (по крайней мере) один метод (возможны и другие):

get_time() - возвращает текущее время в секундах (то есть, значение hours * 3600 + minutes * 60 + seconds).
"""


class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1.get_time()
        self.clock2 = clock2.get_time()

    def __len__(self):
        return 0 if self.clock1 - self.clock2 < 0 else self.clock1 - self.clock2

    def __str__(self):
        a = self.__len__()
        return f"{a // 3600 if a//3600 >9 else '0'+str(a//3600)}: " \
               f"{a % 3600 // 60 if len(str(a % 3600 // 60))==2 else '0'+str(a%3600//60)}: " \
               f"{a % 3600 % 60 if len(str(a%3600%60))==2 else '0'+str(a%3600%60)}"


class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds



if __name__ == '__main__':
    dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
    print(dt)  # 01: 30: 00
    len_dt = len(dt)  # 5400
    str_dt = str(dt)  # возвращает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
    len_dt = len(dt)  # разницу времен clock1 - clock2 в секундах (целое число)
    print(dt)  # отображает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды