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
