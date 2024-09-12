#!/usr/bin/python3
"""
This function prints a full name given the first and optional last name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is" followed by the first and last name.

    Parameters:
    first_name (str): The first name.
    last_name (str, optional): The last name, defaults to an empty string.

    Raises:
    TypeError: If `first_name` or `last_name` is not a string.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
