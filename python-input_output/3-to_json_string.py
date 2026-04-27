#!/usr/bin/python3
"""
Module 3-to_json_string
Provides a function to convert an object to a JSON string.
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to serialize.

    Returns:
        The JSON string representation.
    """
    return json.dumps(my_obj)
