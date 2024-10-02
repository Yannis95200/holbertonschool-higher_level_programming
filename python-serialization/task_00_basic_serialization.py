#!/usr/bin/env python3
"""
Module that provides functions to serialize data to a JSON file
and deserialize data from a JSON file.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes the given data to a JSON file and saves it.

    Args:
        data (object): The data to be serialized, can be any object
        that is JSON serializable.
        filename (str): The name of the file where the data will be saved.
    """
    with open(filename, "w", encoding="utf-8") as dt:
        json.dump(data, dt)


def load_and_deserialize(filename):
    """
    Loads and deserializes data from a JSON file.

    Args:
        filename (str): The name of the file from which to load the data.

    Returns:
        object: The deserialized data from the file.
    """
    with open(filename, "r", encoding="utf-8") as dr:
        return json.load(dr)
