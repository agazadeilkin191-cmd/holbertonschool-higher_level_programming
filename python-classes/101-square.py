#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the current size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the current position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position."""
        if not isinstance(value, tuple) or len(value) != 2 or \
           not isinstance(value[0], int) or not isinstance(value[1], int) or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the # character."""
        print(self.__str__())

    def __str__(self):
        """Return the string representation of the square."""
        if self.__size == 0:
            return ""
        
        result = []
        # Add newlines for position y
        for _ in range(self.__position[1]):
            result.append("")
        
        # Add square rows
        for _ in range(self.__size):
            result.append(" " * self.__position[0] + "#" * self.__size)
            
        return "\n".join(result)
