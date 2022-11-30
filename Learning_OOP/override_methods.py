from abc import ABC


class Shape(ABC):
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length


def area(self):
    return self.length * self.length
