#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
last_digits = abs(number) % 10  # Use absolute value to handle negative numbers
if number > 0:
    if last_digits > 5:
        print(f"Last digit of {number} is {last_digits} and is greater than 5")
    elif last_digits == 0:
        print(f"Last digit of {number} is {last_digits} and is 0")
    else:
        print(f"Last digit of {number} is {last_digits} "
              "and is less than 6 and not 0")
elif number == 0:
    print(f"Last digit of {number} is {last_digits} and is 0")
else:
    print(f"Last digit of {number} is -{last_digits} "
          "and is less than 6 and not 0")
