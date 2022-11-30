class Cat:
    def __init__(self, mass, lifespan, speed):
        self.mass_in_kg = mass
        self.lifespan_in_years = lifespan
        self.speed_in_kph = speed

    def vocalize(self):
        print("Meowwww")

    def print_facts(self):
        print("The {} weighs {} kg, has a lifespan of {} years can run at a maximum speed of {} kph.".format(
            type(self).__name__.lower(), self.mass_in_kg, self.lifespan_in_years, self.speed_in_kph))


class Cheetah(Cat):
    def vocalize(self):  # Overriding vocalize() method
        print("Chirrup")


class Lion(Cat):
    def vocalize(self):  # Overriding vocalize() method
        print("ROARRRRRRRR")


class Leopard(Cat):
    def vocalize(self):  # Overriding vocalize() method
        print("Roar")


cat = Cat(4, 18, 48)
cat.print_facts()
cat.vocalize()


cheetah = Cheetah(72, 12, 120)
cheetah.print_facts()
cheetah.vocalize()


leopard = Leopard(90, 17, 58)
leopard.print_facts()
leopard.vocalize()


lion = Lion(190, 14, 80)
lion.print_facts()
lion.vocalize()
