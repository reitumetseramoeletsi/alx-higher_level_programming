#!/usr/bin/python3
import sys


def args_1(argv):

    n = len(argv) - 1

    if n == 0:
        print("{:d} arguments.".format(n))
        return
    elif n == 1:
        print("{:d} argument:".format(n))
    else:
        print("{:d} arguments:".format(n))

    for i in range(1, n + 1):
        print("{:d}: {:s}".format(i, argv[i]))


if __name__ == "__main__":
    args_1(sys.argv)
