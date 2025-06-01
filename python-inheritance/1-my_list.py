#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """Custom list class that can print its elements sorted."""

    def print_sorted(self):
        """Prints the list in ascending order (sorted)"""
        print(sorted(self))
