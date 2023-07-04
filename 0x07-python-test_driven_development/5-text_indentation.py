#!/usr/bin/python3
"""
Text indentation.
"""


def text_indentation(text):
    """  function that prints a text with 2 new lines after each of these\
        characters: ., ? and : """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delims = [".", "?", ":"]
    lines = []
    current_line = ""

    for char in text:
        current_line += char
        if char in delims:
            lines.append(current_line.strip())
            lines.append("")
            current_line = ""

    lines.append(current_line.strip())
    formatted_text = "\n".join(lines)
    print(formatted_text)
