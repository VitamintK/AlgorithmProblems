#!/bin/python3

import math
import os
import random
import re
import sys

# same problem as B (with renamed variable name) from asian pacific american heritage month 2021 so I copied the solution from there


#
# Complete the 'simpleGame' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def simpleGame(scores):
    numSeq = scores
    # Write your code here
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