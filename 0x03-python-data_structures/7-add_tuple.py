#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) and len(tuple_b) == 2:
        (a1, b1) = (tuple_a)
        (a2, b2) = (tuple_b)
        ad_a = a1 + a2
        ad_b = b1 + b2
        new_tuple = (ad_a, ad_b)
        return (new_tuple)
    elif len(tuple_a) or len(tuple_b) < 2:
        if len(tuple_a) == 1:
            list_a = list(tuple_a)
            list_a.append(0)
            tuple_a = tuple(list_a)
            (a1, b1) = tuple_a
            (a2, b2) = tuple_b
            ad_a = a1 + a2
            ad_b = b1 + b2
            new_tuple = (ad_a, ad_b)
            return (new_tuple)
        elif len(tuple_b) == 1:
            list_b = list(tuple_b)
            list_b.append(0)
            tup_b = tuple(list_b)
            (a1, b1) = tuple_a
            (a2, b2) = tup_b
            ad_a = a1 + a2
            ad_b = b1 + b2
            new_tuple = (ad_a, ad_b)
            return (new_tuple)
        elif len(tuple_a) and len(tuple_b) == 0:
            list_a = list(tuple_a)
            list_a.append(0)
            list_a.append(0)
            list_b = list(tuple_b)
            list_b.append(0)
            list_b.append(0)
            ad_a = list_a[0] + list_b[0]
            ad_b = list_a[1] + list_b[1]
            new_list = [ad_a, ad_b]
            new_tuple = tuple(new_list)
            return (new_tuple)
        else:
            (a1, b1) = tuple_a
            (a2, b2) = tuple_b
            ad_a = a1 + a2
            ad_b = b1 + b2
            new_tuple = (ad_a, ad_b)
            return (new_tuple)
