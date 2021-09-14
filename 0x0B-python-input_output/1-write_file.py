#!/usr/bin/python3
"""
contains fuction write_file
"""


def write_file(filename="", text=""):
    """
    writes string to text fileie(UTF8) & returns the number of the char
    """
    with open(filename, "w", encoding="utf-8") as f:
        return(f.write(text))
