#!/usr/bin/python3
"""
3-say_my_name modulu
"""

def say_my_name(first_name, last_name=""):
    """
    first_name və last_name çap edən funksiya
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
