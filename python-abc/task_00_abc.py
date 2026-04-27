#!/usr/bin/env python3
"""
Defines an Animal class and its subclasses.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class for all animals.
    """
    @abstractmethod
    def sound(self):
        """
        Abstract method to be implemented by subclasses.
        """
        pass


class Dog(Animal):
    """
    Subclass representing a dog.
    """
    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    Subclass representing a cat.
    """
    def sound(self):
        return "Meow"
