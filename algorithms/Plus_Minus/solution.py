#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    l = len(arr)
    p = len([i for i in arr if i > 0])
    n = len([i for i in arr if i < 0])
    z = len([i for i in arr if i == 0])

    print(f"{p/l:.6f}")
    print(f"{n/l:.6f}")
    print(f"{z/l:.6f}")


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
