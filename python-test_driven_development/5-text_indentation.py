#!/usr/bin/python3
"""
Module 5-text_indentation
Defines a function that prints text with 2 new lines after '.', '?' and ':'
"""


def text_indentation(text):
    """
    Prints text with two new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to be processed

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".:?":
            print("\n")
            i += 1
            # Skip following spaces
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
