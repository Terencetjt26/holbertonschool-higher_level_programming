#!/usr/bin/python3
"""MyList class module"""


class MyList(list):
    """Create a class with a method to print a sorted list"""
    def print_sorted(self):
        """Print the list in sorted order"""
        print(sorted(self))
