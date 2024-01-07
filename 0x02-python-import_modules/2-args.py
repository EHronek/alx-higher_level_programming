#!/usr/bin/python3
import sys
nums = len(sys.argv) - 1
if __name__ == "__main__":
    if nums == 1:
        print("1 argument:")
    elif nums == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(nums))
        for x in range(nums + 1):
            if x == 0:
                continue
            print("{}: {}".format(x, sys.argv[x]))
