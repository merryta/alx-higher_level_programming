#!/usr/bin/python3
"""
contains fuction write_file
"""


def write_file(filename="", text=""):
    """
    function  writes a string to text fileie(UTF8) and returns the numbber of the charctere
    """
    with open(filename, "w", encoding="utf-8") as f:
        return(f.write(text))
