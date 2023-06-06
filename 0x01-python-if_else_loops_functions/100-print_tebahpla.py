#!/usr/bin/python3
for i in range(ord('Z'), ord('A') - 1, -1):
    if (i % 2 == 0):
        i += 32
    print(chr(i), end='')
