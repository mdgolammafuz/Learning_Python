# Writing a Class ( here for instance Rectangle Class) in Python

class Rectangle:

    # Conxctructor Method to Instiate Objects using Rectangle Class
    def __init__(self, length, width, color="red"):
        self.length = length
        self.width = width
        self.color = color

    # calculate_area method to calculate the the areea of Objects created using Rectangle Class
    def calculate_area(self):

        return self.width * self.width


# Instanciation of Reactangle class to create rect object
rect = Rectangle(5, 3)

rect1 = Rectangle(4, 2, "blue")  # Second Instance of rectangle Object
rect2 = Rectangle(3, 1, color="pink")

print("Initial object : ", rect)
print("initial length attribute of the object : ", rect.length)
area = rect.calculate_area()
print("Area of the initial object : ", area)