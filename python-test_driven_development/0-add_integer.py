#!/usr/bin/python3
"""
Defines an integer addition function.
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float) and a != a:
        raise TypeError("a must be an integer")
    if isinstance(b, float) and b != b:
        raise TypeError("b must be an integer")
    try:
        a = int(a)
    except OverflowError:
        raise TypeError("a must be an integer")
    try:
        b = int(b)
    except OverflowError:
        raise TypeError("b must be an integer")
    return a + b
