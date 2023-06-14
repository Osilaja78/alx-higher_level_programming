#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_numerals = {
            "I": 1, "V": 5, "X": 10, "C": 100, "D": 500, "M": 1000
            }

    prev_val = 0
    result = 0
    for char in reversed(roman_string):
        value = roman_numerals.get(char, 0)
        if value >= prev_val:
            result += value
        else:
            result -= value
        prev_val = value
    return result
