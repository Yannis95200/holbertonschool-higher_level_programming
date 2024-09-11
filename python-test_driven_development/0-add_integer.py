#!/usr/bin/python3
"""
function that adds two numbers
"""


def add_integer(a, b=98):

    """
    Adds two numbers after converting them to integers.

    Parameters:
    a (int, float): The first number.
    b (int, float, optional): The second number, default is 98.

    Returns:
    int: The sum of the two numbers.

    Raises:
    TypeError: If `a` or `b` are not integers or floats.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
