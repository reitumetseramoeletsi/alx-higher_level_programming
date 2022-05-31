#!/usr/bin/python3
i = 122
while i >= 97:
    f = 0
    if i % 2 != 0:
        i = i - 32
        f = 1
    print("{:s}".format(chr(i)), end='')
    if f == 1:
        i = i + 32
    i = i - 1
