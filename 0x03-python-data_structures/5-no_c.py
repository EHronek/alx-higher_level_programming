#!/usr/bin/python3
def no_c(my_string):
    for c in my_string:
        if c == "c" or c == "C":
            my_string = my_string.replace(c, '')
        return my_string
