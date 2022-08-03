#!/usr/bin/python3
"""
function that reads a text file
"""


def read_file(filename=""):
    """rads a text file (UTF8) and prints it to stdout
    returns none
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
