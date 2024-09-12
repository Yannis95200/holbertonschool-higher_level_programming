#!/usr/bin/python3
"""
This function prints a square using the '#' character.
"""


def print_square(size):
    """
    Prints a square with the size defined by `size` parameter.

    Parameters:
    size (int): The size of the square (both width and height).

    Raises:
    TypeError: If `size` is not an integer.
    ValueError: If `size` is less than 0.
    """
    if type(size) not in [int]:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for index in range(size):
        print("#" * size)
