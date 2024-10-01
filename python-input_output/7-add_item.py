#!/usr/bin/python3
"""
Loads an object from a text file containing JSON data.
"""


import sys
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]

filname = "add_item.json"

try:
    my_list = load_from_json_file(filname)
except FileNotFoundError:
    my_list = []

my_list.extend(args)
save_to_json_file(my_list, filname)
