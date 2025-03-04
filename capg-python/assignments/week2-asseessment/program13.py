class Shape:
    def area(self):
        print("Use square or triangle not base shape.")

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        print(f"Area of Square:{self.side_length ** 2}")

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        print(f"Area of Triangle:{0.5 * self.base * self.height}")

default = Shape()
square = Square(side_length=5)
triangle = Triangle(base=4, height=3)
default.area()
square.area()
triangle.area()
