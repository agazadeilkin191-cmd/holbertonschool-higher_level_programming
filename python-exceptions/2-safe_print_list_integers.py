#!/usr/bin/python3
"""Module that provides a function to print integers safely."""


def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list that are integers.

    Args:
        my_list (list): The list to process.

    Returns:
        int: The number of integers successfully printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError)
            continue
    print()
    return count
