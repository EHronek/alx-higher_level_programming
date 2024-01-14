#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        n = abs(number) % 10
        print(n, end='')
        return (n)
    else:
        n = number % 10
        print(n, end='')
        return (n)
    print()
