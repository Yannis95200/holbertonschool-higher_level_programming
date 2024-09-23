#!/usr/bin/python3
"""
Defines a class `BaseGeometry`.
"""

class BaseGeometry:
    """
    A class used as a base for geometry-related classes.
    """

    def area(self):
        """
        Raises an exception indicating that
        the area method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that `value` is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is not greater than 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))