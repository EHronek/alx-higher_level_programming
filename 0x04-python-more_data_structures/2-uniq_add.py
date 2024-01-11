#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_s = set()
    add = 0
    for item in my_list:
        if item not in uniq_s:
            add += item
            uniq_s.add(add)
    return (add)
