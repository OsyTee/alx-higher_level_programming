#!/usr/bin/python3
comma = ","
for n in range(0, 100):
    if n < 10:
        print("{}{}".format(0, n), end=comma)
    else:
        if n == 99:
            comma = "\n"
        print("{}".format(n), end=comma)
