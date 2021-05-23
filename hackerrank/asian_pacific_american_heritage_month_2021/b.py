#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getScoreDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY numSeq as parameter.
#

def getScoreDifference(numSeq):
    n = len(numSeq)
    scores = [0,0]
    rev = False
    l, r = 0,0
    for i in range(len(numSeq)):
        if rev:
            picked = numSeq[n-1-r]
            r+=1
        else:
            picked = numSeq[l]
            l += 1
        scores[i%2] += picked
        if picked%2 == 0:
            rev = not rev
    return scores[0] - scores[1]
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numSeq_count = int(input().strip())

    numSeq = []

    for _ in range(numSeq_count):
        numSeq_item = int(input().strip())
        numSeq.append(numSeq_item)

    result = getScoreDifference(numSeq)

    fptr.write(str(result) + '\n')

    fptr.close()
