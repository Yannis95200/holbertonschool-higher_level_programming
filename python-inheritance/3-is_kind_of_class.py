#!/usr/bin/python3
"""
Checks if an object is an instance of a class or its subclass.
"""

def is_kind_of_class(obj, a_class):
    """
    Returns True if `obj` is an instance of `a_class` or its subclass, else False.
    """
    return isinstance(obj, a_class)