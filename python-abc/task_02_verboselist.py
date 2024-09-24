#!/usr/bin/python3
"""
A custom list class that provides verbose output for list operations.
"""


class VerboseList(list):
    """
    List subclass that prints messages for add, remove, and pop operations.

    Methods:
        append(item): Adds item and prints a message.
        extend(item): Extends list with items and prints count.
        remove(item): Removes item and prints a
        message; raises ValueError if not found.
        pop(index=-1): Pops item and prints a message.
    """

    def append(self, item):
        """Adds an item and prints a message."""
        print("Added [{}] to the list.".format(item))
        super().append(item)

    def extend(self, item):
        """Extends the list and prints the number of items added."""
        x = len(item)
        print("Extended the list with [{}] items.".format(x))
        super().extend(item)

    def remove(self, item):
        """Removes an item and prints a message;
        raises ValueError if not found."""
        if item not in self:
            raise ValueError(f"{item} not in list")
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pops an item and prints a message."""
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return item
