#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    # Write your code here
    d = s[-2:]  # AM or PM

    if d == "PM":
        if s[:2] == "12":
            return s[: len(s) - 2]

        b = str(int(s[0]) + 1) + str(int(s[1]) + 2)
        return b + s[2 : len(s) - 2]

    # is AM
    if s[:2] == "12":
        return "00" + s[2 : len(s) - 2]

    return s[: len(s) - 2]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = timeConversion(s)

    fptr.write(result + "\n")

    fptr.close()
