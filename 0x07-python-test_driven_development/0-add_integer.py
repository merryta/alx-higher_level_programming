#!/usr/bin/python3
"""
This is the "0-add_integer" module.

add a and b and it can be int or floats
"""


def add_integer(a, b):
    '''
    add two number
    Args:
    a : int or float
    b : int or float
    Rueturn an int
    '''
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
