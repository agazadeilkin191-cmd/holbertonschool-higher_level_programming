#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then saves them to a file.
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load the existing list or create a new one if the file doesn't exist
try:
    my_list = load_from_json_file(filename)
except Exception:
    my_list = []

# Add all arguments to the list
my_list.extend(sys.argv[1:])

# Save the list back to the file
save_to_json_file(my_list, filename)
