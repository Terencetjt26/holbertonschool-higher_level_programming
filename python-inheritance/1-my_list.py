#!/usr/bin/python3
"""Define MyList Class"""


class MyList(list):
    """Craete a List with inheritance"""
    def print_sorted(self):
        """Method to print a sorted list"""
        print(sorted(self))
