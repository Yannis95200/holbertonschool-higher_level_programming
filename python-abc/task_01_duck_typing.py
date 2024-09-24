#!/usr/bin/python3
"""Shapes, Interfaces, and Duck Typing"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    Abstract base class for geometric shapes
    """
    @abstractmethod
    def area(self):
        """
        Abstract method to calculate area
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate perimeter
        """
        pass


class Circle(Shape):
    """
    A subclass of Shape that represents a circle
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Returns the area of the circle
        """
        return pi * self.radius ** 2

    def perimeter(self):
        """
        Returns the perimeter (circumference) of the circle
        """
        return 2 * pi * self.radius


class Rectangle(Shape):
    """
    A subclass of Shape that represents a rectangle
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape
    """
    area = shape.area()
    perimeter = shape.perimeter()
    print("Area: {}".format(area))
    print("Perimeter: {}".format(perimeter))


if __name__ == "__main__":
    # Optional: Add some test cases
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    print("Circle info:")
    shape_info(circle)

    print("\nRectangle info:")
    shape_info(rectangle)
