#!/usr/bin/python3
"""Define a function to write a file"""


def write_file(filename="", text=""):
    """Function to write in a file"""

    with open(filename, "w") as f:
        write_f = f.write(text)
        return write_f
