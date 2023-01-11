#!/usr/bin/python3
""" Defines a JSON file loading function """
import json


def load_from_json_file(filename):
    """ Creates an Object from a JSON file """
    with open(filename) as file:
        json.load(file)
