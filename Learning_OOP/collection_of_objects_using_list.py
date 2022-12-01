from typing import List


class Screw:

    MAX_TIGHTNESS = 5

    def __init__(self):
        self.tightness = 0

    def loosen(self):
        if (self.tightness > 0):
            self.tightness -= 1

    def tighten(self):
        if (self.tightness < self.MAX_TIGHTNESS):
            self.tightness += 1

    def __str__(self):
        return "Screw with tightness {}".format(self.tightness)


class Nail:
    def __init__(self):
        self.in_wall = False

    def nail_in(self):
        if (not self.in_wall):
            self.in_wall = True

    def remove(self):
        if (self.in_wall):
            self.in_wall = False

    def __str__(self):
        return "Nail {}in wall.".format("" if self.in_wall else "not ")


numberList = [1.2, 3.5, 4.3, 2.8]
phoneNumberDictionary = {"alice": "01234 567890", "bob": "01324 765098"}
mixedList = [5, 4, 3, 2, 1, "boom"]

volunteers = [Person("Alice"), Person("Bob"), Person("Carol")]

for volunteer in volunteers:
    volunteer.walk()

toolbox = {
    "screwdriver": Screwdriver(50),
    "hammer": Hammer(),
    "nails": [Nail(), Nail(), Nail() …]
}

volunteers = [Person("Alice"), Fish("Wanda"), Person("Bob")]
for volunteer in volunteers:
    volunteer.walk()  # Oops!


# Typed python


def highest(numbers: List[int]) -> int:
    max_value = 0
    for n in numbers:
        if n > max_value:
            max_value = n
    return max_value


# Defensive approach
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return 0


def divide2(a, b):
    assert b != 0
    return a / b
