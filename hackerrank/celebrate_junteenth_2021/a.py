#!/bin/python3

import math
import os
import random
import re
import sys


from collections import defaultdict
#
# Complete the 'saleCost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY times
#  2. INTEGER_ARRAY ids
#

def saleCost(times, ids):
    ti = list(zip(times, ids))
    ti.sort()
    times, ids = zip(*ti)
    # Write your code here
    # l = 0
    r = 1
    d = defaultdict(int)
    d[ids[0]] += 1
    k = len(set(ids))
    ans = len(times)
    t = 1
    if k == 1:
        return 10
    for l in range(len(times)):
        if l > 0:
            d[ids[l-1]] -= 1
            if d[ids[l-1]] == 0:
                t -= 1
        while t < k and r < len(times):
            d[ids[r]] += 1
            if d[ids[r]] == 1:
                t += 1
            r += 1
        if t < k:
            break
        # print(l,r, r-l, ans, t)
        ans = min(ans, r-l)
    return ans * 10
if __name__ == '__main__':