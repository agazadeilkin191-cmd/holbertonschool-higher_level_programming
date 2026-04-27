#!/usr/bin/python3
"""
Module 6-load_from_json_file
Provides a function to create an object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file.

    Args:
        filename: The path to the JSON file.

    Returns:
        The Python object.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
