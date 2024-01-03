#!/usr/bin/python3
for alphas in range(ord('a'), ord('z') + 1):
    if alphas == 101 or alphas == 113:
        continue
    print(f"{chr(alphas)}", end='')
