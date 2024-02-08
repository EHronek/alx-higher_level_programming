#!/usr/bin/python3
"""defines a functions that writes a string to a text file and
returns the number of characters written"""


def write_file(filename='', text=''):
    """writes a string to a text file and returns the number of
    number of chars written
"""
    with open(filename, 'w', encoding="utf-8") as f:
        chars_written = f.write(text)
    return chars_written
