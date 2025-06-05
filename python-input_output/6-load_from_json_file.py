#!/usr/bin/python3
"""Define a function to create an object from a json file"""

import json


def load_from_json_file(filename):
    """function to create an object from a json file"""

    with open(filename, "r") as f:
        return json.load(f)
