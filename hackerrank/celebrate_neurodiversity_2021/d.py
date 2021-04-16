# diverse population pairs
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'interestingPairs' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER sumValue
#
from collections import Counter
def interestingPairs(arr, sumValue):
    #c = Counter(arr)
    #nums_smaller_or_equal = dict()
    #b = 0
    #for x in sorted(c.keys()):
    #    b += c[x]
    #    nums_smaller_or_equal[x] = b
    arr = [abs(a) for a in arr]
    nums = len(arr)
    ans = 0
    arr.sort()
    if sumValue%2 == 1:
        return 0
    for i in range(len(arr)):
        if sumValue//2 == arr[i]:
            ans += i
    return ans

if __name__ == '__main__':