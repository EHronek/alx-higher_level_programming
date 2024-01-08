#!/usr/bin/python3
def element_at(my_list, idx):
    nums = len(my_list)
    if idx < 0 or idx > nums:
        return None
    else:
        return (my_list[idx])
