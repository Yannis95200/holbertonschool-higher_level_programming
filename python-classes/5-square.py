#!/usr/bin/python3
"""
Defines a class `Square`.
"""


class Square:
    """
    A class used to represent a Square.

    Attributes:
        __size (int): The size of the square's side (private)
        . Must be a non-negative integer.

    Methods:
        __init__(self, size=0):
            Initializes the square with a given size.
        size(self):
            Retrieves the size of the square.
        size(self, value):
            Sets the size of the square with validation.
        area(self):
            Returns the current square's area.
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
        self.__size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Args:
            value (int): The size to set for the square.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square with the character `#` according to the size.
        If size is 0, prints an empty line.
        """
        for index in range(self.__size):
            print('#' * self.__size)
        if self.__size == 0:
            print()
