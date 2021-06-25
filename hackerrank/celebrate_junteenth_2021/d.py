#!/bin/python3

import math
import os
import random
import re
import sys



import sys
sys.setrecursionlimit(100000)
#
# Complete the 'constructString' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY cost
#
from collections import defaultdict
from functools import lru_cache

cache = defaultdict(int)
def get_ans(last, krem, cost):
    if (last, krem) in cache:
        return cache[(last, krem)]
    for i in range(len(cost)):
        if krem - cost[last][i] < 0:
            continue
        if krem-cost[last][i] == 0:
            cache[(last,krem)] = i
            return i
        ans = get_ans(i, krem - cost[last][i], cost)
        if ans is not None:
            cache[(last,krem)] = i
            return i
    

def constructString(k, cost):
    # Write your code here
    t = len(cost)
    ans = []
    for i in range(len(cost)):
        if get_ans(i, k, cost) is not None:
            start = i
            ans.append(i)
            break
    krem = k
    while krem > 0:
        n = get_ans(start,krem,cost)
        ans.append(n)
        krem -= cost[start][n]
        start = n
    return ''.join(chr(97+x) for x in ans)
    
if __name__ == '__main__':