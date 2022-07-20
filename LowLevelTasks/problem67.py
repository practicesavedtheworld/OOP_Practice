"""
Объявите в программе класс Player (игрок), объекты которого создаются командой:

player = Player(name, old, score)

где name - имя игрока (строка); old - возраст игрока (целое число); score - набранные очки в игре (целое число).
В каждом объекте класса Player должны создаваться аналогичные локальные атрибуты: name, old, score.

С объектами класса Player должна работать функция:

bool(player)

которая возвращает True, если число очков больше нуля, и False - в противном случае.

С помощью команды:

lst_in = list(map(str.strip, sys.stdin.readlines()))

считываются строки из входного потока в список строк lst_in. Каждая строка записана в формате:
"имя; возраст; очки"
Каждую строку списка lst_in необходимо представить в виде объекта класса Player с соответствующими данными.
И из этих объектов сформировать список players.

Отфильтруйте этот список (создайте новый: players_filtered), оставив всех игроков с числом очков больше нуля.
Используйте для этого стандартную функцию filter() совместно с функцией bool() языка Python.
"""


import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))


class Player:
    def __init__(self, name: str, old: int, score: int):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return int(self.score) > 0


if __name__ == '__main__':
    players = [Player(*el.split('; ')) for el in lst_in]
    players_filtered = list(filter(lambda x: bool(x) is True, players))
