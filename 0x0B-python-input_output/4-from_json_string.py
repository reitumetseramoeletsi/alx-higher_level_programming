#!/usr/bin/python3
"""
This function returns an object (Python data structure) represented by a JSON string
"""

import json


def from_json_string(my_str):
    """The from_json_string module"""
    return json.loads(my_str)
