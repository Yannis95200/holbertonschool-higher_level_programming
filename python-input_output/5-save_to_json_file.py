#!/usr/bin/python3

"""
Saves a Python object as a JSON file.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Saves a Python object to a file in JSON format.

    Args:
        my_obj: The Python object to save.
        filename (str): The name of the file to save the object to.

    Returns:
        None
    """
    with open(filename, 'w', encoding="utf-8") as file:
        return json.dump(my_obj, file)
