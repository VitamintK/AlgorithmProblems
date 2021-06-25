#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findShortestSubstring' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
from collections import Counter

def good(alps):
    return all([v <= 1 for v in alps.values()])

def findShortestSubstring(s):
    # Write your code here
    alps = Counter(s)
    l = 0
    r = 1
    ans = 112345
    if good(alps):
        return 0
    alps[s[0]] -= 1
    while not good(alps) and r < len(s):
        alps[s[r]] -= 1
        r += 1
        while good(alps) and l < r:
            ans = min(ans, r-l)
            alps[s[l]] += 1
            l += 1
        print(l,r,alps)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = findShortestSubstring(s)

    fptr.write(str(result) + '\n')

    fptr.close()
