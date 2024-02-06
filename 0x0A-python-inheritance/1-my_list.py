#!/usr/bin/python3
"""This module writes a class MyList that inherits from list"""


class MyList(list):
    """this is a custom list class inherits from list
"""

    def print_sorted(self):
        """prints the list in the sorted order"""
        sorted_list = sorted(self)
        print(sorted_list)
