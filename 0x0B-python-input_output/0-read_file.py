#!/usr/bin/python3
"""
Reads a textfile.
"""


def read_file(filename=""):
    """Readsa a text file and prints to stdout"""

    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')
