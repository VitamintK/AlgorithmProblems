#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findMinimumEffort' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY developerSkill
#  2. INTEGER k
#

def findMinimumEffort(developerSkill, k):
    # Write your code here
    developerSkill.sort()
    n = len(developerSkill)
    l = sum(developerSkill[:(k+1)//2])
    r = sum(developerSkill[k//2:k])
    sz = (k+1)//2
    # if k is odd, midpoint is included in both
    ans = 112345678901234567889
    for i in range(k-1, n):
        if i != k-1:
            # update
            l -= developerSkill[i-k]
            l += developerSkill[i-k+sz]
            r -= developerSkill[i-sz]
            r += developerSkill[i]
        med = (developerSkill[i-k+sz] + developerSkill[i-sz+1])//2
        ans = min(ans, abs(med*sz - l) + abs(med*sz - r) )
        print(l, r, med, ans)
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    developerSkill_count = int(input().strip())

    developerSkill = []

    for _ in range(developerSkill_count):
        developerSkill_item = int(input().strip())
        developerSkill.append(developerSkill_item)

    k = int(input().strip())

    result = findMinimumEffort(developerSkill, k)

    fptr.write(str(result) + '\n')

    fptr.close()
