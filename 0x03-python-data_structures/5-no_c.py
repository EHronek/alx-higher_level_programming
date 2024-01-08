#!/usr/bin/python3
def no_c(my_string):
    for c in my_string:
        if c == "c" or c == "C":
            return ''.join([char for char in my_string if char not in c])
