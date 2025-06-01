#!/usr/bin/python3
"""Class MyList that inherits from list."""


class MyList(list):
    """Inherits from list and adds a method to print a sorted list."""

    def print_sorted(self):
        """Print the list, but sorted (ascending sort)."""
        print(sorted(self))
