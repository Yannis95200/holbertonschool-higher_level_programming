#!/usr/bin/python3
"""
Module that provides a function to load data from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Reads and loads data from a JSON file.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        object: The data loaded from the JSON file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
