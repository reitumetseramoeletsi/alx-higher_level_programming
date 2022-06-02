#!/usr/bin/python3
import sys


def add_3(argv):
    n = len(argv) - 1
    sum_3 = 0

    if n == 0:
        print("{:d}".format(sum_3))
        return

    for i in range(1, n + 1):
        sum_3 += int(argv[i])
    print("{:d}".format(sum_3))


if __name__ == "__main__":
    add_3(sys.argv)
