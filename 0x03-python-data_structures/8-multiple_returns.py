#!/usr/bin/python3
def multiple_returns(sentence):
    str_len = len(sentence)
    if str_len == 0:
        return (str_len, None)
    else:
        f_char = sentence[0]
        return (str_len, f_char)
