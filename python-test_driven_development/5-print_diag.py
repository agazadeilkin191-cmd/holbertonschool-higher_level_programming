#!/usr/bin/python3
"""
Module 5-print_diag
"""


def print_diag(size):
    """
    Prints a diagonal pattern of '#' characters.
    Args:
        size (int): The size of the diagonal
    """
    # Use type() instead of isinstance() to avoid bool() == True/False issue
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size <= 0:
        print()
        return

    for i in range(size):
        print(" " * i + "#")
