#!/usr/bin/python3
"""
Validates that the provided value is a positive integer.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Validates that the provided value is a positive integer.
    """
    def __init__(self, width, height):
        """
        Validates that the provided value is a positive integer.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Validates that the provided value is a positive integer.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Validates that the provided value is a positive integer.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
