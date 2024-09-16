#!/usr/bin/python3
"""
Defines a class `Square`.
"""


class Square:
    """
    A class used to represent a Square.

    Attributes:
        __size (int): The size of the square's side (private).
    """

    def __init__(self, size):
        """
        Initializes the square with a given size.

        Args:
            size (int): The size of the square's side.
        """
        self.__size = size
