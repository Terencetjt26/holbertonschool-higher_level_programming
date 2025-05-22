#!/usr/bin/python3
"""Defines a class Square with getter and setter for size."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new square with size validation."""
        self.size = size  # Utilise le setter pour valider

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
