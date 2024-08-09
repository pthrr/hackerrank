#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    # Write your code here

    a = sorted(arr)
    al = [i for idx, i in enumerate(a) if idx < len(arr) - 1]
    ah = [i for idx, i in enumerate(reversed(a)) if idx < len(arr) - 1]
    print(f"{sum(al)} {sum(ah)}")


if __name__ == "__main__":

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
