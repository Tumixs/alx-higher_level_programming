#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    x = dir(hidden_4)
    n = len(x)
    for i in range(n):
        if x[i][0] == "_":
            continue
        print(x[i])
