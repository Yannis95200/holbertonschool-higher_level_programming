#!/usr/bin/python3
"""
This module defines a class BaseGeometry with an unimplemented area method
and an integer_validator method.
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
