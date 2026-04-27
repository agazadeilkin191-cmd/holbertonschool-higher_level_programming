#!/usr/bin/python3
"""
Module 5-save_to_json_file
Provides a function to save an object to a file in JSON format.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj: The object to serialize.
        filename: The name of the file to save to.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
