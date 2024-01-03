#!/usr/bin/python3
print(*["%c" % i for i in range(ord('a'), ord('z')) if i not in (ord('q'), ord('e'))], sep = '', end = '')
