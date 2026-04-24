#!/usr/bin/python3
"""Module that provides a function to indent text."""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these
    characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    flag = 0
    for char in text:
        if flag == 0:
            if char == ' ':
                continue
            else:
                flag = 1

        print(char, end="")

        if char in ".?:":
            print("\n")
            flag = 0
