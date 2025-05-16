#!/usr/bin/python3
"""
Module 0-add_integer
Defines a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers a and b.

    a and b must be integers or floats, otherwise raise a TypeError
    exception with the message:
      - "a must be an integer" if a is not int/float
      - "b must be an integer" if b is not int/float

    Floats are casted to integers before addition.

    Args:
        a (int or float): first number
        b (int or float): second number (default 98)

    Returns:
        int: addition of a and b

    Raises:
        TypeError: if a or b is not int or float

    Examples:
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    >>> add_integer(4, "School")
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    >>> add_integer(None)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
