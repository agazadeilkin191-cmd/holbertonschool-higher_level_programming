#!/usr/bin/python3
"""
Defines an integer addition function.
"""

def add_integer(a, b=98):
    """Returns the addition of a and b.

    Float arguments are typecasted to integers before addition is performed.
    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
