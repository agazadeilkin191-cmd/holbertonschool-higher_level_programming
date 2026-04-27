#!/usr/bin/python3
"""
Module 8-class_to_json
Provides a function to return the dictionary description of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization.

    Args:
        obj: An instance of a Class.

    Returns:
        A dictionary representing the object's attributes.
    """
    return obj.__dict__
