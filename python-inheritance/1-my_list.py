#!/usr/bin/python3
"""
A subclass of list that includes a method to print the list in sorted order.
"""


class MyList(list):
    """
    Prints the list in sorted (ascending) order.
    """

    def print_sorted(self):
        """
        The original list is not modified.
        """
        print(sorted(self))