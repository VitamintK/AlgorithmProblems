#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findMinimumEqualSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY listA
#  2. INTEGER_ARRAY listB
#

def findMinimumEqualSum(listA, listB):
    # Write your code here
    asum = sum(listA)
    bsum = sum(listB)
    azs = len([x for x in listA if x==0])
    bzs = len([x for x in listB if x==0])
    if bzs == 0 and azs+asum > bsum:
        return -1
    if azs == 0 and bzs+bsum > asum:
        return -1
    return max(azs+asum, bzs+bsum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    listA_count = int(input().strip())

    listA = []

    for _ in range(listA_count):
        listA_item = int(input().strip())
        listA.append(listA_item)

    listB_count = int(input().strip())

    listB = []

    for _ in range(listB_count):
        listB_item = int(input().strip())
        listB.append(listB_item)

    result = findMinimumEqualSum(listA, listB)

    fptr.write(str(result) + '\n')

    fptr.close()
