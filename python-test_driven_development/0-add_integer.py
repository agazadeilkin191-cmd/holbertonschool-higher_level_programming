#!/usr/bin/python3
"""
Module that provides the add_integer function.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: first integer or float.
        b: second integer or float.

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: if a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Check for NaN (Not a Number)
    if isinstance(a, float) and a != a:
        raise TypeError("a must be an integer")
    if isinstance(b, float) and b != b:
        raise TypeError("b must be an integer")

    # Cast to integer and handle OverflowError (e.g., float('inf'))
    try:
        a = int(a)
    except (OverflowError, ValueError):
        raise TypeError("a must be an integer")

    try:
        b = int(b)
    except (OverflowError, ValueError):
        raise TypeError("b must be an integer")

    return a + b
