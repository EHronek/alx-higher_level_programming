#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return None
    max_int = my_list[0]
    for num in my_list[1:]:
        if num > max_int:
            max_int = num
    return (max_int)
