#!/usr/bin/python3
"""
Function to read and print the contents of a file
"""


def read_file(filename=""):
    """
    Reads and prints the content of a file.
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
