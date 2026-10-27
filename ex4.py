from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @property
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        print("Area:", round(self.area, 2))
        print("Perimeter:", round(self.perimeter(), 2))

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    @property
    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

circle = Circle(5)
rectangle = Rectangle(4, 6)

print("Circle:")
circle.describe()

print("\nRectangle:")
rectangle.describe()
