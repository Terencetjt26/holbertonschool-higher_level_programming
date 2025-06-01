#!/usr/bin/python3
"""Function that returns True if the object is an instance of,
or inherited from, the specified class."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is instance of a_class or subclass thereof."""
    return isinstance(obj, a_class)
