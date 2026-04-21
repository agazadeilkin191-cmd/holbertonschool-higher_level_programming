#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a: The first integer or float.
        b: The second integer or float, defaults to 98.

    Returns:
        The sum of a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # NaN (Not a Number) check
    if isinstance(a, float) and (a != a):
        raise TypeError("a must be an integer")
    if isinstance(b, float) and (b != b):
        raise TypeError("b must be an integer")

    # Infinity check (prevents float overflow)
    if isinstance(a, float) and (a == float('inf') or a == float('-inf')):
        raise TypeError("a must be an integer")
    if isinstance(b, float) and (b == float('inf') or b == float('-inf')):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
