#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'treeConstruction' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER N
#  2. LONG_INTEGER X
#

T = int(input())
for t in range(T):
    n, x = map(int, input().split())
    ID = 1 #also how many nodes we already have
    children = [[]]
    dmap = {0: 0}
    while x > 0 and ID < n:
        d = min(ID, x)
        if ID+1<n and x-d < n-ID-1:
            # if we haven't used all edges and the remaining dist would require less than 1 dist per edge
            d = 1
        x-=d
        children[dmap[d-1]].append(ID)
        children.append([])
        dmap[d] = ID
        ID+=1
    if x != 0 or ID != n:
        print(-1, -1)
    else:
        for i, c in enumerate(children):
            for e in c:
                print(e+1, i+1)

