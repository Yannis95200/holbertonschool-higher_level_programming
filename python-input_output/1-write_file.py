#!/usr/bin/python3

"""
Writes a string to a specified file.

Parameters:
    filename (str): The name of the file to
    write to (default is an empty string).
    text (str): The text to write to the file (default is an empty string).

Returns:
    int: The number of characters written to the file.
"""


def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
