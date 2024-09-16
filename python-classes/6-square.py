#!/usr/bin/python3
"""
Defines a class `Square`.
"""


class Square:
    """
    A class used to represent a Square.

    Attributes:
        __size (int): The size of the square's side (private).
        __position (tuple): The position of the square (private).

    Methods:
        __init__(self, size=0, position=(0, 0)):
            Initializes the square with a given size and position.
        size(self):
            Retrieves the size of the square.
        size(self, value):
            Sets the size of the square with validation.
        position(self):
            Retrieves the position of the square.
        position(self, value):
            Sets the position of the square with validation.
        area(self):
            Returns the current square's area.
        my_print(self):
            Prints the square based on the size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with a given size and position.

        Args:
            size (int): The size of the square's side (default is 0).
            position (tuple): The position of the square (default is (0, 0)).

        Raises:
            TypeError: If `size` is not an integer or `position` is not a tuple of 2 positive integers.
            ValueError: If `size` is negative.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square with validation.

        Args:
            value (tuple): The position to set for the square.

        Raises:
            TypeError: If `value` is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square with the character `#` according to the size and position.
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return

        # Print new lines for vertical position (position[1])
        for index in range(self.__position[1]):
            print()

        # Print the square with spaces for horizontal position (position[0])
        for index in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
