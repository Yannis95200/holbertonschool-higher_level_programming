#!/usr/bin/python3
"""
Defines a class `Square`.
"""


class Square:
    """
    A class used to represent a Square.

    Attributes:
        __size (int): The size of the square's side (private).
        Must be a non-negative integer.

    Methods:
        __init__(self, size=0):
            Initializes the square with a given size.
    """

    def __init__(self, size=0):
        """
        Initializes the square with a given size.

        Args:
            size (int): The size of the square's side (default is 0).

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
