#!/usr/bin/python3
"""
Module that provides a function to convert an object's attributes
to a dictionary representation.
"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object
    for JSON serialization.

    Args:
        obj (object): The object whose attributes will be converted.

    Returns:
        dict: A dictionary representation of the object's attributes.
    """
    return obj.__dict__
