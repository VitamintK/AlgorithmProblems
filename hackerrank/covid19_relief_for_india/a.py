#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findMinimumCost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMinimumCost(arr):
    # Write your code here
    if len(arr) == 1:
        return 0
    goal = arr[-1]
    delt = goal - arr[-2]
    ans = abs(delt)
    for i in reversed(range(len(arr)-1)):
        print('have', arr[i] + delt, ', want', goal)
        num = goal - (arr[i] + delt)
        ans += abs(num)
        delt += num
        print(num)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = findMinimumCost(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
