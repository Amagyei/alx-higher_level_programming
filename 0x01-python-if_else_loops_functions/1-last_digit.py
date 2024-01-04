#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    val = number % 10
else:
    val = ((number * -1) % 10) * -1
print(f"Last digit of {number:d} is {val:d} and is ", end="")
if val > 5:
    print("greater than 5")
elif val == 0:
    print("0")
else:
    print("less than 6 and not 0")
