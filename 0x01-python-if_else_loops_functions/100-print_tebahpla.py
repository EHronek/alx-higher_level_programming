#!/usr/bin/python3
for i in range(122, 96, -1):
    case = 'lower' if i % 2 == 0 else 'upper'
    print('{}'.format(chr(i) if case == 'lower' else chr(i - 32)), end='')
