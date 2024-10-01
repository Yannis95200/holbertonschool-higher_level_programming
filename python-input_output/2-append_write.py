#!/usr/bin/python3


"""
Appends a string to a specified file.
"""


def append_write(filename="", text=""):
    """
    Appends a string to a text file (UTF8) and
    returns the number of characters appended.

    Args:
        filename (str): The name of the file to append to.
                        Defaults to an empty string.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters appended to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
