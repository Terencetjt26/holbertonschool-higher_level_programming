#!/usr/bin/python3
"""Define a function that return an object represented by a json string"""

import json


def from_json_string(my_str):
    """function to return an object represented by a json string"""

    return json.loads(my_str)
