#!/usr/bin/python3
"""
Module 9-student
Defines a Student class.
"""


class Student:
    """
    Defines a student by:
    - Public instance attributes: first_name, last_name, age
    - Instantiation with first_name, last_name, and age
    - Public method to_json
    """
    def __init__(self, first_name, last_name, age):
        """Initializes the Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary description of the student."""
        return self.__dict__
