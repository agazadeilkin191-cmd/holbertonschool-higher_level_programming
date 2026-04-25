#!/usr/bin/python3
"""
Module 11-square
Inherits from Rectangle and implements Square class with proper __str__.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square that inherits from Rectangle.
    """
    def __init__(self, size):
        """
        Initializes a Square instance with size.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns the string representation of the square: [Square] <width>/<height>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
