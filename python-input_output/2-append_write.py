#!/usr/bin/python3
"""Define a function to append in a file"""


def append_write(filename="", text=""):
    """function to append in a file"""

    with open(filename, "a") as f:
        append_f = f.write(text)
        return append_f
