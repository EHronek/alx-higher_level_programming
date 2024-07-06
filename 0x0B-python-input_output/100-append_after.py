#!/usr/bin/python3
"""
100-append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file"""
    with open(filename, 'r') as file_read:
        lines = file_read.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
