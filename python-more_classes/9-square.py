#!/usr/bin/python3
"""Defines a Square class."""
Rectangle = __import__('8-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""
    def __init__(self, size=0):
        """Initialize a new square."""
        super().__init__(size, size)
