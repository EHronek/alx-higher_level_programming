#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = dict()
    for key in a_dictionary:
        value = a_dictionary[key] * 2
        new_dict.update({key: value})
    return (new_dict)
