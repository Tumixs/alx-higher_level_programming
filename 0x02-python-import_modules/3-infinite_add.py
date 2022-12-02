#!/bin/usr/python3
import sys
n = len(sys.argv)
sums = 0
if __name__ == "__main__":
    for i in range(1, n):
        sums = int(sys.argv[i]) + sums
    print("{}".format(sums))
