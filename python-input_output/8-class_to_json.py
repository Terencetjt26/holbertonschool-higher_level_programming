#!/usr/bin/python3
"""Class to json"""


def class_to_json(obj):
    """Function that return the dictionnary description
        fir json serialization of an object"""

    return obj.__dict__
