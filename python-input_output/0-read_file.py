#!/usr/bin/python3
def read_file(filename=""):
    """
    Reads and prints the content of a file.
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")