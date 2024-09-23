#!/usr/bin/python3
"""
Checks if an object inherits from a class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if `obj` is an instance
    of a class that inherited from `a_class`,
    but not exactly an instance of `a_class`.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
