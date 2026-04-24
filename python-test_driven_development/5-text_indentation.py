#!/usr/bin/python3
"""
Module to print text with specific indentation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Replace delimiters with delimiter + newline + newline
    for delim in ".?:":
        text = text.replace(delim, delim + "\n\n")

    # Split into lines and strip spaces from each line
    lines = text.split('\n')
    for i, line in enumerate(lines):
        # strip() remove spaces at the beginning and the end
        stripped = line.strip()
        # Print the line. If it's the last line, don't add extra newline
        if i < len(lines) - 1:
            print(stripped)
        else:
            print(stripped, end="")
