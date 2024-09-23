#!/usr/bin/python3
"""
This module defines a class BaseGeometry with an unimplemented area method
and an integer_validator method.
"""


class BaseGeometry:
    """
    Base class for geometry-related operations.
    """

    def area(self):
        """
        Raises an Exception indicating that the area method is not implemented.

        This method is intended to be overridden in a subclass.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the provided value is a positive integer.

        Args:
            name (str): The name of the value (for error message purposes).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))