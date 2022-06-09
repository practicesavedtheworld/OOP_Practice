from random import choice


class Cell:
    def __init__(self, mine: bool, around_mines=0, fl_open=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = fl_open


class GamePole:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.pole = [[Cell(choice([*range(1, 6)]), False).around_mines, Cell(choice([*range(1, 6)]), False).mine]
                for _ in range(self.n) for _ in range(self.n)]
        self.init()

    def init(self):


        for i, el in enumerate(self.pole):
            if i == self.m:
                break
            self.pole[choice([*range(1, len(self.pole))])] = [Cell(choice([*range(1, 6)]), True).around_mines,
                                                    Cell(choice([*range(1, 6)]), True).mine]
        return self.pole

    def show(self):
        for i in self.init():
            print(i)


# c1 = Cell(choice([*range(1, 6)]), choice([False, True]))

pole_game = GamePole(10, 12)
pole_game.show()