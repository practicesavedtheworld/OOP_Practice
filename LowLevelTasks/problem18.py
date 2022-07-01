class Body:
    def __init__(self, name, ro, volume):
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
    body1 = Body('qw', 12, 21)
    body2 = Body('qwer', 12, 3)
    print(body1 > body2)
    print(body1 == body2)
    print(body1 < 10)
    print(body2 != 5)
