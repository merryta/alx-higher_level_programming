#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
print('Last digit of ', end='')
if last_digit > 5:
    print("{} is {} and is greater than 5".format(number, last_digit))
elif last_digit == 0:
    print("{} is {} and is 0".format(number, last_digit))
elif last_digit < 6 and last_digit != 0:
    print("{} is {} and is less than 6 and not 0".format(number, last_digit))
