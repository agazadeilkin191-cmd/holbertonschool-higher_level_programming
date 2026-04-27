#!/usr/bin/env python3
"""
Module defining Shape abstract class and concrete classes Circle and Rectangle.
"""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class for shapes.
    """
    @abstractmethod
    def area(self):
        """Calculates area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates perimeter of the shape."""
        pass


class Circle(Shape):
    """
    Concrete class representing a circle.
    """
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius must be non-negative")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Concrete class representing a rectangle.
    """
    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("Width and height must be non-negative")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(obj):
    """
    Function that demonstrates duck typing.
    """
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")
