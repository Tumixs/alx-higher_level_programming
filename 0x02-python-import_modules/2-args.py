#!/usr/bin/python3
import sys
if __name__ == "__main__":
    n = (len(sys.argv) - 1)
    if n == 0:
        print("0 arguments.")
    if n == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    if n > 1:
        print("{} arguments:".format(n))
        for i in range(1, n + 1):
            print("{}: {}".format(i, sys.argv[i]))
