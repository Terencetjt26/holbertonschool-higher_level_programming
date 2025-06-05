#!/usr/bin/python3
"""Define a function that writes an object to a text file
    using a json representation"""

import json


def save_to_json_file(my_obj, filename):
    """function to write an object to a text file by a json representation"""

    with open(filename, "w") as f:
        json.dump(my_obj, f)
