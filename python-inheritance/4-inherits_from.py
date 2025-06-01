#!/usr/bin/python3
"""Function that returns True if the object inherits from a specified class,
but is not exactly an instance of that class."""


def inherits_from(obj, a_class):
    """Return True if obj is instance of a subclass (direct or indirect)
    of a_class, but not an instance of a_class itself."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
