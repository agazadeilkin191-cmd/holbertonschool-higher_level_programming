#!/usr/bin/python3
"""
Module 100-my_int
Contains the class MyInt which inherits from int.
"""


class MyInt(int):
    """
    MyInt is a rebel class that inverts == and != operators.
    """

    def __eq__(self, other):
        """
        Inverts the equality operator.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the inequality operator.
        """
        return super().__eq__(other)
