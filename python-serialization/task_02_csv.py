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
    data = []

    with open(filename, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            data.append(row)
    json_filename = filename.replace('.csv', '.json')
    with open(json_filename, "w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile, indent=4)
