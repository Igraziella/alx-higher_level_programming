#!/usr/bin/python3
""" Defines a JSON string to object function """
import json


def from_json_string(my_str):
    """ Return an object represented by a JSON string """
    return json.load(my_str)
