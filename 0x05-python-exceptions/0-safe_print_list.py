#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i, count = 0, 0
    lis = []
    try:
        while i != x:
            print(my_list[i], end='')
            lis.append(my_list[i])
            count += 1
            i += 1
    except Exception:
        pass
    finally:
        print()
        return (count)
