from abc import ABC, abstractmethod

class IShape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(IShape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        print(f"Area of Rectangle: {area}")

class Circle(IShape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = 3.14159 * (self.radius ** 2)
        print(f"Area of Circle: {area}")

rectangle = Rectangle(length=5, width=10)
circle = Circle(radius=7)

rectangle.calculate_area()
circle.calculate_area()