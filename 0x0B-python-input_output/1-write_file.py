#!/usr/bin/python3
"""
Writes to a file.
"""


def write_file(filename="", text=""):
    """Opens a file in write mode and writes text  to it"""

    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
