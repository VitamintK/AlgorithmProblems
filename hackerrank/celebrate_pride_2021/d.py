#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxDiff' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY coins
#

#bounds are small enough that we can just do N^2 instead of O(N) sliding window :P

def maxDiff(k, coins):
    # Write your code here
    coins.sort()
    # r = 1
    ans = 1
    # for l in range(len(coins)):
    #     while coins[r] 
    for i in range(len(coins)):
        for j in range(i+1, len(coins)):
            if coins[j] - coins[i] <= k:
                ans = max(ans, j-i + 1)
    return ans
if __name__ == '__main__':