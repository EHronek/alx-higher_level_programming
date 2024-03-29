#!/usr/bin/python3
""" defines a function that that reads a text file(utf-8) and prints
it to stdout
"""


def read_file(filename=''):
    """prints contents of utf8 text to stdout
    Args:
        filename: the file to read
"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end='')
