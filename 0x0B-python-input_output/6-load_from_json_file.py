#!/usr/bin/python3
"""definesa  function that creates an object from a "JSON file"""
import json


def load_from_json_file(filename):
    """creates an object from  json file"""
    with open(filename, 'r') as f:
        return json.load(f)
