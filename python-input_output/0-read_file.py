#!/usr/bin/env python3
"""
Task 0: Read file
"""

def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints it to stdout.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
