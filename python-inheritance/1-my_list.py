#!/usr/bin/python3
"""
Module 1-my_list
Contains class MyList
"""


class MyList(list):
    """
    MyList class that inherits from list
    """

    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort).

        >>> my_list = MyList()
        >>> my_list.append(1)
        >>> my_list.append(4)
        >>> my_list.append(2)
        >>> my_list.append(3)
        >>> my_list.append(5)
        >>> my_list.print_sorted()
        [1, 2, 3, 4, 5]
        >>> my_list.append(-1)
        >>> my_list.print_sorted()
        [-1, 1, 2, 3, 4, 5]
        >>> my_list = MyList()
        >>> my_list.print_sorted()
        []
        """
        print(sorted(self))
