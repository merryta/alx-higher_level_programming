#!/usr/bin/python3
"""
contans append_write function
"""


def append_write(filename="", text=""):
    """
    append a string at the end of text file(UTF8) and  returns number of charcter added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return(f.write(text))
