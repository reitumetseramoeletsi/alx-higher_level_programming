#!/usr/bin/python3
def print_last_digit(number):
    inv = 0
    if number < 0:
        number = number * -1
        inv = 1
    last = number % 10
    if inv == 1:
        number = number * -1
    print("{:d}".format(last), end='')
    return last
