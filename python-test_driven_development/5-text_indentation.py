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
    new_line = False
    while i < len(text):
        if text[i] in ".?:":
            print(text[i])
            print()
            new_line = True
            i += 1
            # Skip spaces after punctuation
            while i < len(text) and text[i] == " ":
                i += 1
        else:
            if new_line:
                print(" ", end="")  # Add the indentation space
                new_line = False
            print(text[i], end="")
            i += 1
