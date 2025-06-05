#!/usr/bin/python3
"""Define a funtion to return a json represntation of an object"""

import json


def to_json_string(my_obj):
    """Function to turn a python object into a json string"""

    return json.dumps(my_obj)
