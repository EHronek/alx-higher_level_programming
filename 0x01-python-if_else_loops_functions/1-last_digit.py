#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dgt = abs(number) % 10
if last_dgt > 5:
    print(f"Last digit of {number} is {last_dgt} and is greater than 5")
elif last_dgt == 0:
    print(f"Last digit of {number} is {last_dgt} and is 0")
else:
    print(f"Last digit of {number} is {last_dgt} and is less 6 and not 0")
