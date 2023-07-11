#!/usr/bin/python3
"""
Appends text to a file.
"""


def append_write(filename="", text=""):
    """Appends text to the end of file filename"""

    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
