#!/usr/bin/python3
"""
Module 4-from_json_string
Provides a function to convert a JSON string to a Python object.
"""
import json


def from_json_string(my_str):
    """
    Returns the Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string to parse.

    Returns:
        The Python object.
    """
    return json.loads(my_str)
