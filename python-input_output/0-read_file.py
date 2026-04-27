#!/usr/bin/python3
"""
Module 0-read_file
This module provides a function to read text files.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
