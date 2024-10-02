#!/usr/bin/env python3
"""
Module for converting a CSV file to a JSON file.
"""

import csv
import json


def convert_csv_to_json(filename):
    """
    Converts a CSV file to a JSON file.

    Args:
        filename (str): The name of the CSV file to be converted.

    The function reads the CSV file, converts it into a list of dictionaries,
    and saves it as a JSON file with the same name.
    """
    try:
        data = []
        with open(filename, 'r',) as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                data.append(row)
        with open("data.json", "w",) as jsonfile:
            json.dump(data, jsonfile, indent=4)
            return True
    except: FileNotFoundError
    return False
