#!/usr/bin/python3
"""
This function creates an Object from a "JSON file".
"""
import json


def load_from_json_file(filename):
    """The load_from_json_file module"""
    with open(filename, 'r') as f:
        return json.loads(f.read())
